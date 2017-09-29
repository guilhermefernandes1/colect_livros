from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Livros


@login_required(login_url='/livros/login/')
def show_livros(request):
    template = 'livros/show_books.html'

    book_list = Livros.objects.all()
    context = {
        'book_list': book_list,
    }
    return render(request, template, context)


@require_http_methods(["GET", "POST"])
def log_in(request):
    template_nao_logado = 'livros/login.html'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, template_nao_logado, context={})

        else:
            login(request, user)
            return redirect('livros:show_livros')

    else:
        return render(request, template_nao_logado, context={})


def log_out(request):
    logout(request)

    return redirect('livros:show_livros')
