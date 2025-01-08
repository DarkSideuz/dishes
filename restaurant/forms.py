from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Dish, Category

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone_number')

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SearchForm(forms.Form):
    query = forms.CharField(label='Qidiruv', max_length=100)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Foydalanuvchi nomi', max_length=150)
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)