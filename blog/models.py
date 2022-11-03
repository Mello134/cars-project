from django.db import models

class Post(models.Model):#создаём модель для постов
	title = models.CharField(max_length=300)#поле ввода для заголовка 300символов макс
	data = models.DateTimeField()#стандартная фича джанго, дата время
	text = models.TextField()#Для большого текста, например сама статья
	image = models.ImageField(upload_to='event_images/')#фото будут загружатся в ту папку
	

# Create your models here.
