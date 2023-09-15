from django.db import models

# Create your models here.


class UserData(models.Model) : 

	user_name 		   = models.CharField(max_length=100,null=False) 
	phone_number_user  = models.CharField(max_length=100,null=False)  
	contry_user 	   = models.CharField(max_length=100,null=False)
	gender_user  	   = models.CharField(max_length=100,null=False)


class PregnantWomanData : 
	Age  				= models.IntegerField(null=False)
	Delivery_Number 	= models.IntegerField(null=False)
	Delivery_Time	 	= models.IntegerField(null=False)
	Blood_Of_Pressure   = models.IntegerField(null=False)
	Heart_Problem 		= models.IntegerField(null=False)
	Caesarian_Predict	= models.IntegerField(null=False)