Project Parkinson
==============================

This repository was created as part of the Data-zoomcamp ML engineering course by Andrew Tsai. This project has been submitted as the midterm project for the course.

I chose this dataset because I'd been tackling a problem from Kaggle competition for a while back, and I wanted to see if I could apply what I'd learned in the course to a real-world scenario and deploy a model to the cloud. 


## Parkinson Severity Assessment- the problem we are trying to solve 


Parkinson’s disease (PD) is a disabling brain disorder that affects movements, cognition, sleep, and other normal functions. Unfortunately, there is no current cure—and the disease worsens over time. It's estimated that by 2037, 1.6 million people in the U.S. will have Parkinson’s disease, at an economic cost approaching $80 billion. Research indicates that protein or peptide abnormalities play a key role in the onset and worsening of this disease. Gaining a better understanding of this—with the help of data science—could provide important clues for the development of new pharmacotherapies to slow the progression or cure Parkinson’s disease.

Current efforts have resulted in complex clinical and neurobiological data on over 10,000 subjects for broad sharing with the research community. A number of important findings have been published using this data, but clear biomarkers or cures are still lacking.

Competition host, the Accelerating Medicines Partnership® Parkinson’s Disease (AMP®PD), is a public-private partnership between government, industry, and nonprofits that is managed through the Foundation of the National Institutes of Health (FNIH). The Partnership created the AMP PD Knowledge Platform, which includes a deep molecular characterization and longitudinal clinical profiling of Parkinson’s disease patients, with the goal of identifying and validating diagnostic, prognostic, and/or disease progression biomarkers for Parkinson’s disease.

Your work could help in the search for a cure for Parkinson’s disease, which would alleviate the substantial suffering and medical care costs of patients with this disease.


The goal of this competition is to predict MDS-UPDR scores, which measure progression in patients with Parkinson's disease. The Movement Disorder Society-Sponsored Revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS) is a comprehensive assessment of both motor and non-motor symptoms associated with Parkinson's. You will develop a model trained on data of protein and peptide levels over time in subjects with Parkinson’s disease versus normal age-matched control subjects.

Your work could help provide important breakthrough information about which molecules change as Parkinson’s disease progresses.

## Navigating the project repository 

Where to find the files for evaluation:

-  **Exploratory Data Analysis**  
    I ran one notebook to do the analysis. A copy of it is in the [repository](notebooks/EDA.ipynb).

-  **Scripts**  
    [train.py](./Scripts/train.py) runs the training for the final models. Predictions can be ran within either a [lambda handler](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html) (the predict function can be found within [lambda.py](app-lambda-function/lambda_function.py)) or a [Gunicorn local service](https://docs.gunicorn.org/en/stable/deploy.html) (the predict function can be found within [predict.py](app-flask/predict.py)).
-  **Deployment**  
    The lambda function is deployed on [AWS Lambda](https://aws.amazon.com/lambda/) with an [API Gateway](https://aws.amazon.com/api-gateway/) sat in front of it. This end point will remain available until the end of the evaluation period.
    
    
    *Example request to the Lambda Gateway API in python script:*

    ``` python
    import requests
    url = 'https://x8ee6c4ds4.execute-api.ap-southeast-2.amazonaws.com/test/predict'
    data = {'data': [1,2,3,4]}
    print(requests.post(url, json=data).json())
    ```

    *Example response*

    ```
    {'updrs_1': 4.899986842559807, 'updrs_2': 6.644429461169236, 'updrs_3': 20.466737232954546, 'updrs_4': 0.09874205289906657}
    ```


## Running the project ▶️




### Prepare the repository 📂

```sh
git clone https://github.com/AndrewTsai0406/project-parkinson.git
```
  or
```
Download ZIP
```


### Requirements ⚙️

I advise using a virtual environment for running this project, below are instructions for doing so using [Conda](https://www.anaconda.com/) which helps one manage multiple envirnoments. Additionally if you would like to run the analysis notebooks or the app in Docker you will need to have [Docker](https://docs.docker.com/get-docker/) installed.
### Start a virtual environment 🌐

```sh
# create virtual environment
conda create -n project-parkinson python=3.10

# start the virtual environment
conda activate project-parkinson

# install requirements
pip install -r requirements.txt
```

### Data 💽

The data used for this project is gathered from [Kaggle](https://www.kaggle.com/competitions/amp-parkinsons-disease-progression-prediction/data) and has the [CC BY-SA 3.0 License](https://creativecommons.org/licenses/by-sa/3.0/). It consists of protein abundance values derived from mass spectrometry readings of cerebrospinal fluid (CSF) samples gathered from several hundred patients. Each patient contributed several samples over the course of multiple years while they also took assessments of PD severity.


Download this data (including the three CSVs) and put it in to a `./data` directory. The directory should look like this:

------------
    data
    ├── raw               
    │   ├── amp_pd_peptide  <- Files that enable the API. Expect the API to deliver all of the data (less than 1,000 additional patients) in under five minutes and to reserve less than 0.5 GB of memory. A brief demonstration of what the API delivers is available here.
    │   ├── amp_pd_peptide_310
    │   ├── example_test_files <- Data intended to illustrate how the API functions. Includes the same columns delivered by the API (ie no updrs columns).
    │   ├── supplemetnal_clinical_data.csv <- Clinical records without any associated CSF samples. This data is intended to provide additional context about the typical progression of Parkinsons. Uses the same columns as train_clinical_data.csv.
    │   ├── train_clinical_data.csv
    │   ├── train__peptides.csv <- Mass spectrometry data at the peptide level. Peptides are the component subunits of proteins.
    │   ├── train_proteins.csv <- Protein expression frequencies aggregated from the peptide level data.

------------


### Training & saving the models🏋️‍♀️

To run the training script and save the mdoels, use the one script inside `./scripts`: `train.py` with the command:

```sh
python train.py
```

The final models, which corresponds to each score, will be saved in the `.models` directory.

### Running the app locally for prediction


#### Run the lambda server

To build and run the lambda server I use the following docker commands.

```sh
cd ./app-lambda-function
docker build -t project-parkinson .
docker run -p 8080:8080 project-parkinson
```

Test with script:
```python
import requests
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
data = {'data': [1,2,3,4]}
print(requests.post(url, json=data).json())
```

#### Run the Gunicorn server

To build and run the Gunicorn server I use the following docker commands.

```sh
cd ./app-flask
docker build -t project-parkinson .
docker run -p 6969:80 project-parkinson
```

Test with script:
```python
import requests
url = 'http://0.0.0.0:6969/predict'
data = {'data': [1,2,3,4]}
print(requests.post(url, json=data).json())
```

## Evaluation Criteria

The project will be evaluated using these criteria:

* Problem description
* EDA
* Model training
* Exporting notebook to script
* Model deployment
* Reproducibility
* Dependency and environment management
* Containerization
* Cloud deployment

[Criteria](https://docs.google.com/spreadsheets/d/e/2PACX-1vQCwqAtkjl07MTW-SxWUK9GUvMQ3Pv_fF8UadcuIYLgHa0PlNu9BRWtfLgivI8xSCncQs82HDwGXSm3/pubhtml)


## Cheating and plagiarism

Plagiarism in any form is not allowed. Examples of plagiarism

* Taking somebody's else notebooks and projects (in full or partly) and using it for the capstone project
* Re-using your own projects (in full or partly) from other courses and bootcamps
* Re-using your midterm project from ML Zoomcamp in capstone
* Re-using your ML Zoomcamp from previous iterations of the course

Violating any of this will result in 0 points for this project.

## FAQ


**Q**: Can I use poetry / virtual env for managing dependencies; catboost for boosting and FastAPI for creating a web service?

> Yes, you can use any library you want. But please make sure to document everything and clearly explain what you use.
> Think of your peers who will review it - they don't necessarily know what these libraries are. 
> Please give them enough context to understand your project.

**Q**: Can multiple people use the same dataset?

> Yes, there's no way to control it or enforce. So it's totally okay if you and somebody else use the same dataset. 

**Q**: For peer reviewing, do I have to run the code and make sure it works?

> It's recommended that you do that, but you don't _have_ to do it.

**Q**: What if I see an error? What if I run something and it doesn't work?

> If you spot an error somewhere and you see that the code clearly doesn't work, then you
> give 0 points to the respective criterium. E.g. if you see an error in Dockerfile,
> then you give 0 points to the "containerization" dimension.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
