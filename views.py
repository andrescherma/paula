from django.shortcuts import render

def about(request):
	return render(request, 'about.jade')

def contact(request):
	return render(request, 'contact.jade')
