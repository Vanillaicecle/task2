from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('task2/admin/', admin.site.urls),  # Админка доступна через /task2/admin/
    path('task2/accounts/', include('django.contrib.auth.urls')),  # Авторизация через /task2/accounts/
    path('task2/', include('blogs.urls')),  # Всё приложение через /task2/
]