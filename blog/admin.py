from django.contrib import admin

from .models import Post
#из blog\models.py импортировали класс Post, чтобы добавить его в админку
admin.site.register(Post)



# Register your models here.

# from .models import Post #Импортировалм наш Post class. Нашу модель Post
							
# admin.site.register(Post)	