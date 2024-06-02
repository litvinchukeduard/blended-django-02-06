from django.urls import path
from trip_app import views

app_name = 'trip_app'

urlpatterns = [
    path("", views.main, name='main'),
]
