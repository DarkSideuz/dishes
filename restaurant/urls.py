from django.urls import path, include
from .views import (
    add_category,
    home,
    all_dishes,
    dish_detail,
    add_dish,
    edit_dish,
    delete_dish,
    category_dishes,
    register,
    logout,
    profile,
    search,
    add_comment,
    add_category,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('dishes/', all_dishes, name='all_dishes'),
    path('dishes/<int:dish_id>/', dish_detail, name='dish_detail'),
    path('dishes/add/', add_dish, name='add_dish'),
    path('dishes/<int:dish_id>/edit/', edit_dish, name='edit_dish'),
    path('dishes/<int:dish_id>/delete/', delete_dish, name='delete_dish'),
    path('categories/<int:category_id>/', category_dishes, name='category_dishes'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('categories/add/', add_category, name='add_category'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),
    path('search/', search, name='search'),
    path('dishes/<int:dish_id>/comment/', add_comment, name='add_comment'),
]