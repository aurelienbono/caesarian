from django.shortcuts import render , redirect
from caesarian.data import TransformData
import joblib
from . import models
import numpy as np 


# Create your views here.


# THE LANDING PAGE 
def index(request) : 
	return render(request, 'pages/landing.html')

#AUTHS PAGE REGISTER
def register(request) : 
	return render(request, 'pages/register.html')

## UI FOR THE COLLECTION 
def apps(request) : 
	return render(request, 'pages/apps.html')

## SEND EMAIL
def sendmail(request): 
	pass 
	## les mails qui dois etre envoyé pour le feedback au niveau du forms dans la landing page





#AUTHS PAGE LOGIN 
def login(request) : 
	user_login = []
	if request.method == 'POST' : 
		for element in request.POST : 
			user_login.append(request.POST[element])
		user_login = user_login[1:]
		print(user_login)

	return render(request, 'pages/login.html')



#AUTHS PAGE REGISTER
def register(request) : 
	user_register = []
	if request.method == 'POST' : 
		for element in request.POST : 
			user_register.append(request.POST[element])
		user_register = user_register[1:]


		user = models.User(name=user_register[0], email=user_register[1] , password=user_register[2])
		user.save()

		return redirect('apps')

	return render(request, 'pages/register.html')








# PREPROCESS PREDICTION DATA 
def makeprediction(X_test):

    #Load the joblib
    model = joblib.load('caesarian/ml_models/CaesarianModel_logisticregre_models_0_1_0.joblib')
    # Make predictions on new data

    y_pred = model.predict([X_test])
    y_pred_prob = model.predict_proba([X_test]).tolist()

    if y_pred[0] == 0: 
    	return ['Non',0, y_pred_prob[0][0],y_pred_prob[0][1]  ] 
    else : 
    	return ['Oui',1,y_pred_prob[0][1] , y_pred_prob[0][0] ]





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
										Age  			    = pregnant_woman_transform[1], 
										Delivery_Number     = pregnant_woman_transform[2],
										Delivery_Time 	    = pregnant_woman_transform[3],
										Blood_Of_Pressure   = pregnant_woman_transform[4],
										Heart_Problem	    = pregnant_woman_transform[5],
										Caesarian_Predict   = pregnant_woman_transform[6],
										Caesarian_Label_Yes = round(y_pred[2] *100 , 2),
										Caesarian_Label_NO  = round(y_pred[3] *100 , 2)

										)
		woman.save()




		print(y_pred)

		content = {  
			'name':  request.POST.get('name'),
			'decision' : y_pred[0] , 
			'true_proba' : round(y_pred[2] *100 , 2), 
			}


	return render(request, 'pages/prediction.html' , content)

