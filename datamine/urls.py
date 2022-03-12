#datamine URL Configuration


from django.contrib import admin
from django.urls import path
from django.urls.conf import include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yt.urls')),
    path('user/',include('users.urls')),
    #path('accounts/', include('allauth.urls'))

]

