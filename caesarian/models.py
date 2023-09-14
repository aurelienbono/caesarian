from django.db import models

# Create your models here.


class UserData(models.Model) : 

	user_name 		   = models.CharField(max_length=100,unique=True) 
	phone_number_user  = models.CharField(max_length=100,unique=True)  
	contry_user 	   = models.CharField(max_length=100,unique=True)
	gender_user  	   = models.CharField(max_length=100,unique=True)


class PregnantWomanData : 
	Age  				= models.IntegerField(null=False)
	Delivery_Number 	= models.IntegerField(null=False)
	Delivery_Time	 	= models.IntegerField(null=False)
	Blood_Of_Pressure   = models.IntegerField(null=False)
	Heart_Problem 		= models.IntegerField(null=False)
	Caesarian_Predict	= models.IntegerField(null=False)