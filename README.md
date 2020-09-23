# Context

This repository contains the Machine Learning Model & the WebAPI of the PREDIA – Modelo Híbrido Multifatorial for my final paper @ Unisinos.

You can access the WebAPI which consumes the model @ [predia.herokuapp.com](https://predia.herokuapp.com/)

![Heroku](https://pyheroku-badge.herokuapp.com/?app=predia&style=flat)

![Screen Shot 2020-09-20 at 15 35 23](https://user-images.githubusercontent.com/8363610/93719111-e969b680-fb56-11ea-9bab-d94f007c9887.png)

# Components Diagram
![03_Components](https://user-images.githubusercontent.com/8363610/93719289-e0c5b000-fb57-11ea-807e-1e223dad1534.png)

# Architecture Basic Diagram

![03_Steps](https://user-images.githubusercontent.com/8363610/94078669-9e5cd700-fdd4-11ea-980e-6afa44c18601.png)

# Architecture Detail Diagram
![04_Architecture_Detail](https://user-images.githubusercontent.com/8363610/94083241-1fb66880-fdd9-11ea-8326-825508605249.png)

# EDA - Sales History
![image](https://user-images.githubusercontent.com/8363610/94081715-9d787500-fdd5-11ea-89d7-87c1982bfe7a.png)

# EDA - Sales History Monthly

![image](https://user-images.githubusercontent.com/8363610/94081770-be40ca80-fdd5-11ea-8ea0-f6a645617570.png)

# EDA - Sales History Quarterly  

![image](https://user-images.githubusercontent.com/8363610/94081806-d6b0e500-fdd5-11ea-8495-ba39b8b69035.png)

# EDA - Sales Mean
![image](https://user-images.githubusercontent.com/8363610/94081832-ed573c00-fdd5-11ea-8f8d-186141bdd3de.png)

# EDA - Kernel Density Sales
![image](https://user-images.githubusercontent.com/8363610/94081882-0a8c0a80-fdd6-11ea-96ff-5dffd77a4c73.png)

# Prediction
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
