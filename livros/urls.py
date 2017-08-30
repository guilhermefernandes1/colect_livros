from django.conf.urls import url

from . import views


app_name = 'livros'

urlpatterns = [
    url(r'^$', views.show_livros, name = 'show_livros'),
]
