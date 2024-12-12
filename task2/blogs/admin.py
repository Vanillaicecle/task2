from django.contrib import admin
from .models import BlogPost

# Регистрируем модель BlogPost в админке
admin.site.register(BlogPost)
