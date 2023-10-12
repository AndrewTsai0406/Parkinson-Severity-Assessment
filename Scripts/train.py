import numpy as np
import pandas as pd
import joblib

from sklearn.svm import SVR  
from sklearn.linear_model import *
from sklearn.metrics import make_scorer
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold,GridSearchCV,RandomizedSearchCV,GroupKFold
from sklearn.preprocessing import OrdinalEncoder,Normalizer,MinMaxScaler,StandardScaler

class train:
    """Train models for each target"""
    def __init__(self):
        pass
    
    def smape(self, y_true, y_pred):

        y_true += 1
        y_pred += 1
        
        numerator = np.abs(y_true - y_pred)
        denominator = (np.abs(y_true) + np.abs(y_pred)) / 2
        positive_index = (y_true!=0) | (y_pred!=0)
        smape = np.zeros(len(y_true))
        smape[positive_index] = numerator[positive_index] / denominator[positive_index]
        smape = 100 * np.mean(smape)
        return smape


    def train(self):

        sup = pd.read_csv('../data/raw/amp-parkinsons-disease-progression-prediction/supplemental_clinical_data.csv')
        train_set = pd.read_csv("../data/raw/amp-parkinsons-disease-progression-prediction/train_clinical_data.csv")
        train_set = pd.concat([train_set,sup],ignore_index=True).drop(['upd23b_clinical_state_on_medication'],axis=1)
        targets = ["updrs_1", "updrs_2", "updrs_3", "updrs_4"]

        model_pool = [Lars(),RandomForestRegressor(),SVR(),Lasso()]
        # model_pool = [Lars(),RandomForestRegressor(),SVR(),Lasso(),LGBMRegressor(),XGBRegressor()]


        for target in targets:
            # Drop NAs
            temp = train_set.dropna(subset=[target]) 

            # For updrs_3, dropping 0's improve results
            if target == 'updrs_3':
                temp = temp[temp[target] != 0]

            # Train data
            X = temp['visit_month'].values.reshape(-1,1)
            
            y = temp[target] 

            enc = OrdinalEncoder()
            groups = enc.fit_transform(pd.DataFrame(temp.patient_id)).reshape(1,-1)[0].tolist()
            cv = GroupKFold(n_splits=5)

            model_candidates = []
            scores = []
            for ind, model in enumerate(model_pool):
                model_candidates.append(
                    GridSearchCV(model,
                                {item[0]:[item[1]] for item in model.get_params().items()},
                                cv = cv.split(X, y, groups),
                                scoring=make_scorer(self.smape),
                                verbose = 1
                                ).fit(X,y)
                )
                scores.append((ind,model_candidates[-1].best_score_))
                print(target,str(model_candidates[ind].estimator).split('(')[0],model_candidates[-1].best_score_)

            winning_model = model_candidates[sorted(scores,key = lambda x:x[1])[0][0]]
            print(f"Pick best performing model for {target}:{str(winning_model.estimator).split('(')[0]}",'\n','-'*50)

            print(winning_model.best_score_)
            joblib.dump(winning_model.best_estimator_, f'../models/models_{target}.pkl')
            joblib.dump(winning_model.best_estimator_, f'../app-flask/models/models_{target}.pkl')
            joblib.dump(winning_model.best_estimator_, f'../app-lambda-function/models/models_{target}.pkl')


if __name__ == "__main__":
    train = train()
    train.train()