from __future__ import unicode_literals

from django.db import models


class Livros(models.Model):
    nome = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'livros'


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
