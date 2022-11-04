from django.shortcuts import render, get_object_or_404#404 - покажет либо нужный объект, а если его нет покажет 404
from .models import Post

# Create your views here.
def showblog(request):
	posts = Post.objects
	return render(request, 'blog/blog.html', {'posts':posts})
	#функция будет возвращать страницу blog.html - в папке cars-project/blog/templates/blog/blog.html, для отображения информации из класса пост создали словарь, с ключём post

def specific_post(request, post_id):#функция для отдельного поста
	post = get_object_or_404(Post, pk=post_id)#Post - класс, pk - основной ключ в базе данных
	return render(request, 'blog/specific_post.html', {'post':post})