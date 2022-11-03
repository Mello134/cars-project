from django.contrib import admin
from .models import Event
#импортировали наш класс из models.py
admin.site.register(Event)
#Добавили наш класс Event в админку, теперь в админке можем добавлять кртинки с текстом, бедем использовать на домашней странице
# Register your models here.
