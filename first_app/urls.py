from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.home,name='homepage'),
   path('singup/',views.singup,name='singup'),
   path('profile/',views.profile,name='profile'),
   path('login/',views.user_login,name='login'),
   path('logout/',views.userlogout,name='logout'),
   path('passwordchange1/',views.pass_change,name='passwordchange1'),
   path('passwordchange2/',views.pass_change2,name='passwordchange2'),

   
]