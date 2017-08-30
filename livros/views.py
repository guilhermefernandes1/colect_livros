from django.shortcuts import render
from .models import Livros

def show_livros(request):
	book_list = Livros.objects.all()

	template = 'livros/show_books.html'
	context = {
		'book_list': book_list,
	}
	return render(request, template, context)
