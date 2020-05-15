from django.urls import path
from SOC import views

urlpatterns = [
    path('',views.index,name='index'),
    path('seasons/',views.seasons,name='seasons'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
]
