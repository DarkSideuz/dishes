from django.urls import path, include
from .views import (
    all_dishes,
    dish_detail,
    add_dish,
    edit_dish,
    delete_dish,
    category_dishes,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    HomeView,
    RegisterView,
    LogoutView,
    ProfileView,
    SearchView,
    AddCommentView,
    AddCategoryView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dishes/', DishListView.as_view(), name='all_dishes'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('dishes/add/', DishCreateView.as_view(), name='add_dish'),
    path('dishes/<int:pk>/edit/', DishUpdateView.as_view(), name='edit_dish'),
    path('dishes/<int:pk>/delete/', DishDeleteView.as_view(), name='delete_dish'),
    path('categories/<int:category_id>/', category_dishes, name='category_dishes'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('search/', SearchView.as_view(), name='search'),
    path('dishes/<int:dish_id>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('categories/add/', AddCategoryView.as_view(), name='add_category'),
]