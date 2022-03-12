#user 
from django.urls import path
from . import views

app_name = "main"   

urlpatterns = [
  path('home/', views.homepage, name="homepage"),
  path("", views.register, name="register"),
  path('login/',views.loginUser,name = 'login'),
  path('logout/',views.logoutUser ,name = 'logout')

]