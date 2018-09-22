from django.urls import path

from . import views

app_name = 'fav'
urlpatterns = [
    path('', views.ListFavoriteView.as_view(), name='index'),
    path('create/', views.CreateFavoriteView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateFavoriteView.as_view(), name='update'),
]
