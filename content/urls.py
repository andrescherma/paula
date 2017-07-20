from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^processos$', views.processes),
	url(r'^obras$', views.works),
	url(r'^obras/(?P<serie_slug>[\w-]+)$', views.serie),
	url(r'^obras/(?P<serie_slug>[\w-]+)/(?P<work_slug>[\w-]+)$',
		views.view_work),
    url(r'^admin', admin.site.urls),
 ]