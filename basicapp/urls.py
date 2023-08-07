from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('user_login', views.login, name='user_login'),
]
