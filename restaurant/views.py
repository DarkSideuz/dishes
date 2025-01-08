from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Dish, Category, Comment
from .forms import UserRegistrationForm, DishForm, CategoryForm, SearchForm, LoginForm
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View

class DishListView(ListView):
    model = Dish
    template_name = 'dishes/all_dishes.html'
    context_object_name = 'dishes'

class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/dish_detail.html'
    context_object_name = 'dish'

class HomeView(View):
    def get(self, request):
        form = SearchForm()
        results = []
        
        if 'query' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                query = form.cleaned_data['query']
                results = Dish.objects.filter(name__icontains=query)

        return render(request, 'home.html', {'form': form, 'results': results})

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
        return render(request, 'registration/register.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect('home')

class ProfileView(View):
    def get(self, request):
        return render(request, 'registration/profile.html')

class SearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        dishes = Dish.objects.filter(name__icontains=query)
        return render(request, 'dishes/search_results.html', {'dishes': dishes})

class AddCommentView(View):
    def post(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        text = request.POST.get('text')
        Comment.objects.create(user=request.user, dish=dish, text=text)
        return redirect('dish_detail', dish_id=dish.id)

class AddCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'categories/add_category.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
        return render(request, 'categories/add_category.html', {'form': form})

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

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'dishes/add_dish.html'
    success_url = reverse_lazy('all_dishes')

class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = 'dishes/edit_dish.html'
    success_url = reverse_lazy('all_dishes')

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'dishes/delete_dish.html'
    success_url = reverse_lazy('all_dishes')
