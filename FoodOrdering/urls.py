"""PyShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from FoodOrdering.Views.Restaurant.Dishes.AddDish import AddDish
from FoodOrdering.Views.Restaurant.Edit import EditRestaurant
from FoodOrdering.Views.Restaurant.Dishes.ListDishes import ListDishes
from FoodOrdering.Views.Restaurant.ListRestaurants import ListRestaurants

app_name = 'FoodOrdering'
urlpatterns = [
    path('', ListRestaurants.as_view(), name='home'),
    path('restaurants/edit/', EditRestaurant.as_view(), name='edit_restaurant'),
    path('restaurants/dishes/add', AddDish.as_view(), name='add_dish'),
    path('restaurants/<int:pk>/dishes/', ListDishes.as_view(), name='list_dishes'),
    path('restaurants/<int:pk>/dishes/edit', ListDishes.as_view(), name='edit_dish'),
    path('restaurants/<int:pk>/dishes/remove', ListDishes.as_view(), name='remove_dish'),
]
