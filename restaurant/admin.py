from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html
from .models import Category, Dish, Comment

class CustomAdminSite(AdminSite):
    site_header = 'Taomxona Admin'
    site_title = 'Taomxona Admin Paneli'
    index_title = 'Boshqaruv paneli'

    def get_urls(self):
        urls = super().get_urls()
        return urls

    def each_context(self, request):
        context = super().each_context(request)
        context['admin_css'] = 'css/admin_custom.css'
        return context

admin_site = CustomAdminSite(name='custom_admin')

admin_site.register(Dish)
admin_site.register(Category)
admin_site.register(Comment)