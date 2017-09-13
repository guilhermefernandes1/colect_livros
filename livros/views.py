from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods

from .models import Livros


def show_livros(request):
    template = 'livros/show_books.html'
    template_negado = 'livros/negado.html'

    if 'username' not in request.session or request.session['username'] is None:
        return render(request, template_negado)

    else:
        book_list = Livros.objects.all()
        context = {
            'book_list': book_list,
        }
        return render(request, template, context)


@require_http_methods(["GET", "POST"])
def login(request):
    template_nao_logado = 'livros/login.html'
    template_logado = 'livros/show_books.html'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, template_nao_logado, context={})

        else:
            request.session['username'] = username
            return render(request, template_logado, context={})

    else:
        return render(request, template_nao_logado, context={})


def logout(request):
    request.session['email'] = None
    template = 'livros/logout.html'

    return render(request, template)
