from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from.models import Dish, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def all_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'dishes/all_dishes.html', {'dishes': dishes})

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    return render(request, 'dishes/dish_detail.html', {'dish': dish})

def category_dishes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    dishes = category.dishes.all()
    return render(request, 'dishes/category_dishes.html', {'category': category, 'dishes': dishes})

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('all_dishes')
    return render(request, 'categories/add_category.html')

def add_dish(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)
        Dish.objects.create(name=name, description=description, price=price, category=category)
        return redirect('all_dishes')
    return render(request, 'dishes/add_dish.html', {'categories': categories})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.save()
        return redirect('all_dishes')
    return render(request, 'categories/edit_category.html', {'category': category})

def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        dish.name = request.POST.get('name')
        dish.description = request.POST.get('description')
        dish.price = request.POST.get('price')
        category_id = request.POST.get('category')
        dish.category = get_object_or_404(Category, id=category_id)
        dish.save()
        return redirect('all_dishes')
    return render(request, 'dishes/edit_dish.html', {'dish': dish, 'categories': categories})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('all_dishes')

def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.delete()
    return redirect('all_dishes')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')
