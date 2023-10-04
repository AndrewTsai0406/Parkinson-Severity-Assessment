Project Parkinson
==============================

Deploy code from Kaggle competition for data-zoomcamp ML engineering course



## Project

* Think of a problem that's interesting for you and find a dataset for that
    ```Context
    Parkinson’s disease (PD) is a disabling brain disorder that affects movements, cognition, sleep, and other normal functions. Unfortunately, there is no current cure—and the disease worsens over time. It's estimated that by 2037, 1.6 million people in the U.S. will have Parkinson’s disease, at an economic cost approaching $80 billion. Research indicates that protein or peptide abnormalities play a key role in the onset and worsening of this disease. Gaining a better understanding of this—with the help of data science—could provide important clues for the development of new pharmacotherapies to slow the progression or cure Parkinson’s disease.

    Current efforts have resulted in complex clinical and neurobiological data on over 10,000 subjects for broad sharing with the research community. A number of important findings have been published using this data, but clear biomarkers or cures are still lacking.

    Competition host, the Accelerating Medicines Partnership® Parkinson’s Disease (AMP®PD), is a public-private partnership between government, industry, and nonprofits that is managed through the Foundation of the National Institutes of Health (FNIH). The Partnership created the AMP PD Knowledge Platform, which includes a deep molecular characterization and longitudinal clinical profiling of Parkinson’s disease patients, with the goal of identifying and validating diagnostic, prognostic, and/or disease progression biomarkers for Parkinson’s disease.

    Your work could help in the search for a cure for Parkinson’s disease, which would alleviate the substantial suffering and medical care costs of patients with this disease.
    ```

* Describe this problem and explain how a model could be used
    ```Goal of the Competition
    The goal of this competition is to predict MDS-UPDR scores, which measure progression in patients with Parkinson's disease. The Movement Disorder Society-Sponsored Revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS) is a comprehensive assessment of both motor and non-motor symptoms associated with Parkinson's. You will develop a model trained on data of protein and peptide levels over time in subjects with Parkinson’s disease versus normal age-matched control subjects.

    Your work could help provide important breakthrough information about which molecules change as Parkinson’s disease progresses.

    ```
* Prepare the data and doing EDA, analyze important features
    ```
    amp-eda-models.ipynb
    ```
* Train multiple models, tune their performance and select the best model
    ```
    groupkfold-supplement-median-model-competition.ipynb
    ```
* Export the notebook into a script
* Put your model into a web service and deploy it locally with Docker
* Bonus points for deploying the service to the cloud

## Deliverables

For a project, you repository/folder should contain the following:

* `README.md` with
  * Description of the problem
  * Instructions on how to run the project
* Data
  * You should either commit the dataset you used or have clear instructions how to download the dataset
* Notebook (suggested name - `notebook.ipynb`) with
  * Data preparation and data clearning
  * EDA, feature importance analysis
  * Model selection process and parameter tuning
* Script `train.py` (suggested name)
  * Training the final model
  * Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)
* Script `predict.py` (suggested name)
  * Loading the model
  * Serving it via a web serice (with Flask or specialized sofware - BentoML, KServe, etc)
* Files with dependencies
  * `Pipenv` and `Pipenv.lock` if you use Pipenv
  * `bentofile.yaml` if you use BentoML
  * or equivalents: conda environment file, requirements.txt or pyproject.toml
* `Dockerfile` for running the service
* Deployment
  * URL to the service you deployed or
  * Video or image of how you interact with the deployed service


## Peer reviewing

To evaluate the projects, we'll use peer reviewing. This is a great opportunity for you to learn from each other.

* To get points for your project, your need to evaluate 3 projects of your peers
* You get 3 extra points for each evaluation

Tip: you can use https://nbviewer.org/ to render notebooks if GitHub doesn't work


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

## Resources

### Datasets


* [A list with datasets from our Data Engineering course](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_7_project/datasets.md)
* https://www.kaggle.com/datasets and https://www.kaggle.com/competitions
* https://archive.ics.uci.edu/ml/index.php
* https://data.europa.eu/en
* https://www.openml.org/search?type=data
* https://www.tensorflow.org/datasets/catalog/overview
* [Soocer data](https://github.com/statsbomb/open-data)
* https://newzealand.ai/public-data-sets
* [OECD database](https://stats.oecd.org/index.aspx?lang=en)
* [deeplake](https://datasets.activeloop.ai/docs/ml/datasets/)
* Add more data here!

### Projects Gallery

Explore a collection of projects completed by members of our community. The projects cover a wide range of topics and utilize different tools and techniques. Feel free to delve into any project and see how others have tackled real-world problems with data, structured their code, and presented their findings. It's a great resource to learn and get ideas for your own projects.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://datatalksclub-projects.streamlit.app/)

### Zoomcamp 2022

* [Midterm project](../cohorts/2022/projects.md#midterm-project)
* [Capstone 1](../cohorts/2022/projects.md#capstone-1)
* [Capstone 2](../cohorts/2022/projects.md#capstone-2)


### Zoomcamp 2021

* [Midterm project](../cohorts/2021/07-midterm-project/)
* [Capstone 1](../cohorts/2021/12-capstone/)
* [Capstone 2](../cohorts/2021/14-project/)




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
