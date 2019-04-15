from django.shortcuts import render, redirect


#The index view
def index(request):

	#Redirect to the app index	
	return redirect('/Music/')