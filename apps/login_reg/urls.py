from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$',views.index ,name ='login_index'),
    url(r'^success$',views.new ,name ='new'),
    url(r'^create$',views.createUser ,name ='create'),
    url(r'^logout$',views.logout ,name ='logout'),
    url(r'^login$',views.login ,name ='login'),
    #url(r'^',include('apps.formtest.urls')),
]
