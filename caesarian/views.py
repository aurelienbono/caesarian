from django.shortcuts import render 

# Create your views here.



def index(request) : 
	return render(request, 'pages/index.html')


def prediction(request) : 
	user_data  = []
	pregnant_woman = [] 
	all_data   = []

	if request.method =='POST' : 
		for element in request.POST : 
			all_data.append(request.POST[element])

		# I retrieve user data on all data provided in the form
		user_data = all_data[2:6]

		#I recover the pregnant woman's data on all the data provided in the form
		pregnant_woman = all_data[6:-2]

	print(user_data)
	print(pregnant_woman)
	print(all_data)



	return render(request, 'pages/prediction.html')

	

def login(request) : 
	return render(request, 'pages/login.html')

def register(request) : 
	return render(request, 'pages/register.html')