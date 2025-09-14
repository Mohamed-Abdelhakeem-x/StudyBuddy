from django.urls import path
from . import views

urlpatterns = [ 
    path('Login/', views.loginPage, name = "Login"),
    path('Logout/', views.logoutUser, name = "Logout"),
    path('register/', views.registerPage, name = "register"),
    path('', views.home, name = "home"),
    path('room/<str:pk>/', views.room, name = "room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('create-room/', views.createRoom, name = "create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name = "update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name = "delete-room"),
    path('edit-message/<str:pk>/', views.updateMessage, name="edit-message"),
    path('delete-message/<str:pk>/', views.deleteMessage, name = "delete-message"),
]