from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
   path('',views.index,name="index"),
   path('movies/<int:id>',views.detailview,name='details_page'),
   path('add_movie',views.add_movie,name='add_movie'),
   path('update/<int:id>/',views.update,name='update'),
   path('delete/<int:id>',views.delete,name="delete"),


]