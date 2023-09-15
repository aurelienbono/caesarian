from django.shortcuts import render 
from caesarian.data import TransformData
import joblib
from . import models
import numpy as np 



# Create your views here.

def index(request) : 
	return render(request, 'pages/index.html')


def login(request) : 
	return render(request, 'pages/login.html')

def register(request) : 
	return render(request, 'pages/register.html')




def makeprediction(X_test):

    #Load the joblib
    model = joblib.load('caesarian/ml_models/CaesarianModel_logisticregre_models_0_1_0.joblib')
    # Make predictions on new data

    y_pred = model.predict([X_test])

    if y_pred[0] == 0: 
    	return ['Non',0] 
    else : 
    	return ['Oui',1] 





def prediction(request) : 
	user_data  = []
	pregnant_woman = [] 
	all_data   = []

	if request.method =='POST' : 
		for element in request.POST : 
			all_data.append(request.POST[element])

		# I retrieve user data on all data provided in the form
		user_data = all_data[2:6]

		# saving userData to the database
		user = models.UserData(user_name=user_data[0], phone_number_user=user_data[1], contry_user=user_data[2], gender_user=user_data[3])
		user.save()
		

		# I recover the pregnant woman's data on all the data provided in the form
		pregnant_woman = all_data[6:-2]


		# transformation of pregnant woman data for prediction

		transformer = TransformData()
		pregnant_woman_transform =  transformer.transform(pregnant_woman)
		print(user_data)


		y_pred = makeprediction(pregnant_woman_transform[1:])


		#append the prediction in array after in db 
		pregnant_woman_transform.append(y_pred[1])

		woman = models.PregnantWomanData( 
										Age  			   = pregnant_woman_transform[1], 
										Delivery_Number    = pregnant_woman_transform[2],
										Delivery_Time 	   = pregnant_woman_transform[3],
										Blood_Of_Pressure  = pregnant_woman_transform[4],
										Heart_Problem	   = pregnant_woman_transform[5],
										Caesarian_Predict  = pregnant_woman_transform[6],

										)


		print(y_pred)



	return render(request, 'pages/prediction.html')

