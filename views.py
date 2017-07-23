from django.shortcuts import render

def home(request):
	return render(request, 'home.jade')

def about(request):
	return render(request, 'about.jade')

def contact(request):
	return render(request, 'contact.jade')
