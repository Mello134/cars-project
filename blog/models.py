from django.db import models

class Post(models.Model):#создаём модель для постов
	title = models.CharField(max_length=300)#поле ввода для заголовка 300символов макс
	data = models.DateTimeField()#стандартная фича джанго, дата время
	text = models.TextField()#Для большого текста, например сама статья
	image = models.ImageField(upload_to='event_images/')#фото будут загружатся в ту папку

	def get_summary(self):
		return self.text[:300]
		#функция возвращающая 70 символоа из переменной текст (краткая инфа)

	def __str__(self):#в админке будет выводить имя поста место postobjects(1)
		return self.title
	

# Create your models here.
