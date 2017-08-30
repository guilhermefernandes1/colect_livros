from django.conf.urls import url

from . import views


app_name = 'livros'

urlpatterns = [
    url(r'^$', views.show_livros, name = 'show_livros'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^logout/$', views.logout, name = 'logout'),
]
