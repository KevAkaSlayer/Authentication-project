from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name = 'home'),
    path('signup/', views.signup , name = 'signup'),
    path('profile/', views.profile , name = 'profile'),
    path('login/', views.user_login , name = 'login'),
    path('logout/', views.user_logout , name = 'logout'),
    path('passchng/', views.pass_change , name = 'passchng'),
    path('passchng2/', views.pass_change2 , name = 'passchng2'),
    path('Update/', views.change_user_data , name = 'update'),
]