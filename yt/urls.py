#yt
from django.conf import settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "app" 
urlpatterns = [
    path('start/', views.start,name= 'start'),
    path('main', views.dashboard,name= 'main'),
    path('', views.house,name= 'house'),
    path('yt/', views.youtube,name= 'yt'),
    path('instagram/', views.insta,name= 'insta'),
    path('linkedin/', views.linked,name= 'linked'),
    path('client-new/', views.add_new,name= 'showclients'),
    path('client-del/<int:id>/',views.delete_data, name='deletedata'),
    path('client-update/<int:id>/',views.update_client, name='updatedata')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


    