from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import Dish, Category, Comment
from .forms import CustomUserCreationForm, DishForm, CategoryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseForbidden

def home(request):
    top_dishes = Dish.objects.order_by('-views')[:3]
    return render(request, 'home.html', {'top_dishes': top_dishes})

def all_dishes(request):
    dishes = Dish.objects.all()
    categories = Category.objects.all()
    return render(request, 'dishes/all_dishes.html', {'dishes': dishes, 'categories': categories})

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.views += 1
    dish.save()
    comments = dish.comments.all()

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(dish=dish, text=comment_text)
            return redirect('dish_detail', dish_id=dish.id)

    return render(request, 'dishes/dish_detail.html', {'dish': dish, 'comments': comments})

@login_required
@permission_required('restaurant.add_dish', raise_exception=True)
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
@permission_required('restaurant.change_dish', raise_exception=True)
def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
    else:
        form = DishForm(instance=dish)
    return render(request, 'dishes/edit_dish.html', {'form': form, 'dish': dish})

@login_required
@permission_required('restaurant.delete_dish', raise_exception=True)
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def add_category(request):
    if not request.user.has_perm('restaurant.add_category'):
        messages.error(request, "You don't have permission to add a category.")
        return redirect('home')

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect('all_dishes')
    else:
        form = CategoryForm()
    return render(request, 'categories/add_category.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def search(request):
    query = request.GET.get('q')
    results = Dish.objects.filter(name__icontains=query)
    return render(request, 'dishes/search_results.html', {'results': results})

@login_required
def add_comment(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(dish=dish, user=request.user, text=text)
        return redirect('dish_detail', dish_id=dish.id)
