from django.shortcuts import render

# Create your views here.

def processes(request):
	return render(request, 'content/processes.jade')

def works(request):
	return render(request, 'content/works.jade')

def serie(request, serie_id):
	return render(request, 'content/serie.jade')

def view_work (request, work_id):
	return render(request, 'content/serie.jade')

