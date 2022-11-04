from django.shortcuts import render
from .models import Event

#request - это запрос, то есть что будет запрашивать в браузере
#render - это то что будем отдавать/показывать/выполнять в ответ на запрос
def home(request):#создаём функцию домашней страницы
	events = Event.objects
	return render(request, 'home/home.html', {'events':events})
	#вывод home.html  в ответ на запрос
	#будет искать cars-project/home/templates/home/home.html




# Create your views here.
