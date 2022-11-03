from django.db import models

# Create your models here.
class Event(models.Model):#создали класс Event, применили все свойства встроенные в Models джанги
	event_image = models.ImageField(upload_to='event_images/')
	#Это поле для загрузки изображений, в админке. Будет загружать в ..
	event_text = models.CharField(max_length=900)
	#Поле для ввода текста, ограничено 900 символов