from django.contrib import admin
from .models import MenuItem

# Регистрация модели MenuItem в админке Django
admin.site.register(MenuItem)