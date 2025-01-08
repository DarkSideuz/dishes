from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Dish, Category, Comment
from .forms import UserRegistrationForm, DishForm, CategoryForm, SearchForm, LoginForm
from django.contrib.auth import views as auth_views

def home(request):
    form = SearchForm()
    results = []
    
    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Dish.objects.filter(name__icontains=query)  

    return render(request, 'home.html', {'form': form, 'results': results})

def all_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'dishes/all_dishes.html', {'dishes': dishes})

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.views += 1
    dish.save() 
    return render(request, 'dishes/dish_detail.html', {'dish': dish})

@login_required
def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
    else:
        form = DishForm()
    return render(request, 'dishes/add_dish.html', {'form': form})

@login_required
def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_detail', dish_id=dish.id)
    else:
        form = DishForm(instance=dish)
    return render(request, 'dishes/edit_dish.html', {'form': form, 'dish': dish})

@login_required
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        dish.delete()
        return redirect('all_dishes')
    return render(request, 'dishes/delete_dish.html', {'dish': dish})

def category_dishes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    dishes = Dish.objects.filter(category=category)
    return render(request, 'dishes/category_dishes.html', {'category': category, 'dishes': dishes})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')

def search(request):
    query = request.GET.get('q')
    dishes = Dish.objects.filter(name__icontains=query)
    return render(request, 'dishes/search_results.html', {'dishes': dishes})

@login_required
def add_comment(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(user=request.user, dish=dish, text=text)
        return redirect('dish_detail', dish_id=dish.id)
    return render(request, 'dishes/dish_detail.html', {'dish': dish})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
    else:
        form = CategoryForm()
    return render(request, 'categories/add_category.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
