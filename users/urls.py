from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path("login/", views.loginuser, name='login_user'),
    path("logout/", views.logoutuser, name='logout_user'),
]
