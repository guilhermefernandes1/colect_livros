from django.shortcuts import render
from .models import Livros


def show_livros(request):
    template = 'livros/show_books.html'
    template_negado = 'livros/negado.html'

    if 'email' not in request.session or request.session['email'] is None:
        return render(request, template_negado)

    else:
        book_list = Livros.objects.all()
        context = {
            'book_list': book_list,
        }
        return render(request, template, context)


def login(request):
    request.session['email'] = 'guilhermefernandes1@gmail.com'
    template = 'livros/login.html'

    return render(request, template)


def logout(request):
    request.session['email'] = None
    template = 'livros/logout.html'

    return render(request, template)
