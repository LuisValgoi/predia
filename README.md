# Context

This repository contains the Machine Learning Model & the WebAPI of the PREDIA – Modelo Híbrido Multifatorial for my final paper @ Unisinos. You can access the WebAPI which consumes the model @ [predia.herokuapp.com](https://predia.herokuapp.com/). All the work starts with the OneHotEncoding technique being applied to the dataset. After that, Exploratory Data Analysis, and more specific, Correlation Analysis were made to find the features that were deacreasing the models perfomance. Then, the model building starts with the selection of 3 heterogenous algorithms, where each one of them, makes a prediction following a pipeline composed of: Feature Engineering + Permutation Importance + Randomized Search & Feature Scaling (w/ MinMaxScaler). Once the pipeline is finished, the technique of Ensemble Learning called Aggregation is made, generating a final number of sales to be sold in the next day. The final model has a RMSE of 18.92 which represents less than 7% of the sales mean. 

# Status
![Heroku](https://pyheroku-badge.herokuapp.com/?app=predia&style=flat)

# Techniques
- **OneHotEncoding**: to optimize the algorithms prediction by transforming the dataset.
- **Exploratory Data Analysis**: to check how my data is structured.
- **Correlational Feature Analaysis**: to clean and remove the features which has no meaning.
- **Cross Validation**: to use all the dataset instead of only one period.
- **Permutation Importance**: to identify what are the most important feature for each algorithm.
- **MinMaxScaler**: to scale the dataset from 0 to 1 so all the algorithms do not suffer from its deviation.
- **Randomized Search**: to identify the best hyperparameters for each algorithm.
- **Ensemble Learning**: to aggregate the results of each model into one to increase the perfomance.

# Tooling

For this project, I have used:
- **Python**: as the main language.
- **Jupyter Notebook**: as the IDE to develop the model.
- **SKLearn**: as the ML library.
- **Keras**: as the deep learning library.
- **Streamlit**: as the framework to build the frontend.
- **Heroku**: as the server to host the entire model & frontend.

# App Image Sample 
![Screen Shot 2020-09-20 at 15 35 23](https://user-images.githubusercontent.com/8363610/93719111-e969b680-fb56-11ea-9bab-d94f007c9887.png)

# Components Diagram
![03_Components](https://user-images.githubusercontent.com/8363610/93719289-e0c5b000-fb57-11ea-807e-1e223dad1534.png)

# Architecture Basic Diagram

![03_Steps](https://user-images.githubusercontent.com/8363610/94078669-9e5cd700-fdd4-11ea-980e-6afa44c18601.png)

# Architecture Detail Diagram
![04_Architecture_Detail](https://user-images.githubusercontent.com/8363610/94084066-02829980-fddb-11ea-9eb8-cdf4bb8f0904.png)

# Sales History
![image](https://user-images.githubusercontent.com/8363610/94081715-9d787500-fdd5-11ea-89d7-87c1982bfe7a.png)

# Algorithms Prediction Combined
![image](https://user-images.githubusercontent.com/8363610/94083521-c0a52380-fdd9-11ea-9294-14a483701aa8.png)

# WebAPI - Getting Started

```
pipenv shell
pip install streamlit
pip install plotly
pip install sklearn
pip install keras
pip install tensorflow
streamlit run app.py
```

# Jupyter Notebook - Getting Started

```
cd predia
jupyter notebook
```

# Heroku - Getting Started

```
heroku login
...
git push heroku master
heroku logs --tail
```
