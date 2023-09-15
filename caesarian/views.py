from django.shortcuts import render 
from caesarian.data import TransformData
import joblib
from . import models

# Create your views here.

def index(request) : 
	return render(request, 'pages/index.html')


def login(request) : 
	return render(request, 'pages/login.html')

def register(request) : 
	return render(request, 'pages/register.html')




	


def prediction(request) : 
	user_data  = []
	pregnant_woman = [] 
	all_data   = []

	if request.method =='POST' : 
		for element in request.POST : 
			all_data.append(request.POST[element])

		# I retrieve user data on all data provided in the form
		user_data = all_data[2:6]

		#saving userData to the database
		user = models.UserData(user_name=user_data[0], phone_number_user=user_data[1], contry_user=user_data[2], gender_user=user_data[3])
		user.save()
		


		#I recover the pregnant woman's data on all the data provided in the form
		pregnant_woman = all_data[6:-2]


		# transformation of pregnant woman data for prediction

		transformer = TransformData()
		pregnant_woman_transform =  transformer.transform(pregnant_woman)
		print(user_data)



	return render(request, 'pages/prediction.html')

