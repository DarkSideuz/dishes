from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Ensure this is imported
from .models import Dish, Category
from .validators import validate_phone_number, validate_username

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(validators=[validate_phone_number], required=False)

    class Meta:
        model = User  # Ensure this is set to the default User model
        fields = ('username', 'email', 'password1', 'password2', 'phone_number')

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'category']  # Ensure price is included

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SearchForm(forms.Form):
    query = forms.CharField(label='Qidiruv', max_length=100)