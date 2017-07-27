from django.conf.urls import url
from . import views
#from django.contrib import admin

urlpatterns = [
    url(r'^$', views.welcome, name="welcome"),
    url(r'^main$', views.main, name="main"),
    url(r'^login$', views.login, name="login"),
    url(r'^destroy$',views.logout ,name ='destroy'),
    url(r'^create$', views.createUser, name="create"),
    url(r'^index$', views.index, name="my_index"),
    url(r'^client/add$', views.new, name="new"),
    url(r'^client$', views.create, name="create"),
    url(r'^client/(?P<id>\d+)$',views.show, name = 'show_page'),
    url(r'^client/(?P<id>\d+)/addproject$',views.add_project, name = 'add_project'),
    url(r'^client/(?P<id>\d+)/projectpage$',views.project_page, name = 'project_page'),
    url(r'^show/projects/(?P<id>\d+)$',views.proj_show, name = 'show_project'),
    url(r'^client/(?P<id>\d+)$',views.back, name = 'back'),
    url(r'^client/remove/(?P<id>\d+)$',views.remove, name = 'delete'),
    url(r'^client/remove_project/(?P<id>\d+)$',views.remove_project, name = 'remove'),
    url(r'^client/edit/(?P<id>\d+)$',views.edit, name = 'edit'),
    url(r'^client/update/(?P<id>\d+)$',views.update, name = 'update'),
    url(r'^client/ProjectNoteEdit/(?P<id>\d+)$',views.edit_proj_note, name = 'edit_proj_note'),
    url(r'^client/update_projectnote/(?P<id>\d+)$',views.update_proj_note, name = 'update_proj_note'),




]
