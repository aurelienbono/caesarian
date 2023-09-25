
About
=====

Caesarean section prediction project

The aim of this project is to develop a machine learning model capable of predicting whether or not a woman will have a caesarean section, based on her age, delivery number, time of delivery, blood pressure and cardiac status.

The data set

The dataset used in this project is a classification dataset. It contains 1000 observations, each with 6 characteristics and a target variable.

The features

The characteristics of the dataset are as follows:

Age: the woman's age in years.
Delivery number: The number of previous deliveries of the woman.
Time of delivery: The time of delivery, classified as premature, timely or late.
Blood pressure: The woman's blood pressure, classified as low, normal or high.
Heart problem: whether the woman has a heart problem, classified as yes or no.
The target variable

The target variable for the dataset is as follows:

Caesarean section: whether the woman had a caesarean section, classified as yes or no.


Installation
============
- Create virtualenv - `virtualenv venv`

- Enter it `source venv/bin/activate`

- Install required packages `pip install -r requirements.txt`

- Run it: `python app.py runserver`

- Run it: `python manage.py makemigrations`

- Run it: `python manage.py migrate`

- For more - reference Django documentation

Route
=====
`/` est la page d'accueil du projet
`/login` permet aux utilisateurs de se connecter au projet
`/register`


