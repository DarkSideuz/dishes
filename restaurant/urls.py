from django.urls import path
from django.contrib.auth.views import LoginView
from .views import all_dishes, dish_detail, category_dishes, add_category, add_dish, edit_category, edit_dish, delete_category, delete_dish, register, home

urlpatterns = [
    path('', home, name='home'),
    path('dishes/', all_dishes, name='all_dishes'),
    path('dishes/<int:dish_id>/', dish_detail, name='dish_detail'),
    path('categories/<int:category_id>/dishes/', category_dishes, name='category_dishes'),
    path('categories/add/', add_category, name='add_category'),
    path('dishes/add/', add_dish, name='add_dish'),
    path('categories/<int:category_id>/edit/', edit_category, name='edit_category'),
    path('dishes/<int:dish_id>/edit/', edit_dish, name='edit_dish'),
    path('categories/<int:category_id>/delete/', delete_category, name='delete_category'),
    path('dishes/<int:dish_id>/delete/', delete_dish, name='delete_dish'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),
]