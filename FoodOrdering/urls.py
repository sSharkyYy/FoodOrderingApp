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

from FoodOrdering.Views.Cart.Add import AddToCart
from FoodOrdering.Views.Cart.Clear import ClearCart
from FoodOrdering.Views.Cart.List import ListCartItems
from FoodOrdering.Views.Order.Create import CreateOrder
from FoodOrdering.Views.Restaurant.Dishes.AddDish import AddDish
from FoodOrdering.Views.Restaurant.Dishes.EditDish import EditDish
from FoodOrdering.Views.Restaurant.FilterOrders import FilterOrders
from FoodOrdering.Views.Restaurant.Types.AddType import AddType
from FoodOrdering.Views.Restaurant.Types.ListTypes import ListTypes
from FoodOrdering.Views.Restaurant.Edit import EditRestaurant
from FoodOrdering.Views.Restaurant.Dishes.ListDishes import ListDishes
from FoodOrdering.Views.Restaurant.ListRestaurants import ListRestaurants
from FoodOrdering.Views.Restaurant.Types.UpdateType import UpdateType
from FoodOrdering.Views.Restaurant.Types.DeleteType import DeleteType
from FoodOrdering.Views.Courier.Edit import EditCourierTimeInt
from FoodOrdering.Views.Courier.Orders.ListOrders import ListOrders
from FoodOrdering.Views.Courier.Orders.UpdateOrders import UpdateOrders

app_name = 'FoodOrdering'
urlpatterns = [
    path('', ListRestaurants.as_view(), name='home'),
    path('restaurants/edit/', EditRestaurant.as_view(), name='edit_restaurant'),
    path('restaurants/dishes/add', AddDish.as_view(), name='add_dish'),
    # path('restaurants/editCategory/', EditCategories.as_view(), name='list_categories'),
    path('restaurants/types/<int:pk>/edit', UpdateType.as_view(), name='edit_categories'),
    path('restaurants/types/<int:pk>/delete', DeleteType.as_view(), name='delete_categories'),
    # path('car/<int:pk>/delete', login_required(CarDeleteView.as_view()), name='car-delete'),
    path('restaurants/types', ListTypes.as_view(), name='list_types'),
    path('restaurants/types/add', AddType.as_view(), name='add_type'),
    # path('restaurants/<int:pk>/delete', DeleteType.as_view(), name='delete_type'),
    path('restaurants/<int:pk>/dishes/', ListDishes.as_view(), name='list_dishes'),
    path('restaurants/<int:pk>/dishes/edit', EditDish.as_view(), name='edit_dish'),
    path('restaurants/<int:pk>/dishes/remove', ListDishes.as_view(), name='remove_dish'),
    path('cart/', ListCartItems.as_view(), name='cart'),
    path('add-to-cart/<int:dish>/', AddToCart.as_view(), name='add_to_cart'),
    path('clear-cart/', ClearCart.as_view(), name='clear_cart'),
    # path('remove-from-cart/<int:dish>/', AddToCart.as_view(), name='remove-from-cart'),
    # path('update-quantity/<int:dish>/', AddToCart.as_view(), name='update-quantity'),

    path('courier/edit/', EditCourierTimeInt.as_view(), name='edit_courier_timeinterval'),
    path('courier/orders', ListOrders.as_view(), name='list_orders'),
    path('courier/orders/setstatus', UpdateOrders.as_view(), name='set_status'),



    path('order/', CreateOrder.as_view(), name='order'),
    path('list-orders/', FilterOrders.as_view(), name='filter_orders'),

]
