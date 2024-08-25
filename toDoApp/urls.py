from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home-page'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/',views.register, name='register'),
    path('delete/<str:name>/', views.deleteTask,name='delete'),
    path('update/<str:name>/', views.Update, name='update'),
]