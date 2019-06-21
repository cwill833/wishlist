from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.ItemCreate.as_view(), name='items_create'),
    path('<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
    # path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
]