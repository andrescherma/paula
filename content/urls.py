from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'obras?', views.works, name='works'),
	url(r'obras/(P?<serie_id>[\d+])$', views.serie, name='serie'),
	url(r'obras/(P?<work_id>[\d+])$', views.view_work, name='view_work'),
	url(r'processos$', views.processes, name='processes'),
]