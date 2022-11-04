from django.urls import path
#из джанго импортируем встроенную функцию path

from . import views #импортируем файл views из этой же папки myblog/blog/
urlpatterns = [
	path('', views.showblog, name='showblog'),
	path('<int:post_id>/', views.specific_post, name='specific_post'),
]
#cоздали список urlpatterns с путями, добавили путь к функции showblog из файла views.py(функцию создадим далее)