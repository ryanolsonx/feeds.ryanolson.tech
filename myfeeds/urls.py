from django.urls import path

from myfeeds import views

urlpatterns = [
    path('', views.index, name='index')
]