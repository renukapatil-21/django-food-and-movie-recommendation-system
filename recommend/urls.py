from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.index, name='index'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('watch/', views.watch, name='watch'),
    path('recommend/', views.recommend, name='recommend'),
    path('food/', views.food, name='food'),
    path('food/watch2/', views.watch2, name='watch2'),
    path('food/<int:movie_id>/', views.detail2, name='detail2'),
    path('food/recommend2/', views.recommend2, name='recommend2')

]