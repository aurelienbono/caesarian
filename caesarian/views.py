from django.shortcuts import render 

# Create your views here.



def index(request) : 
	return render(request, 'pages/index.html')


def prediction(request) : 
	return render(request, 'pages/prediction.html')
	

def login(request) : 
	return render(request, 'pages/login.html')

def register(request) : 
	return render(request, 'pages/register.html')