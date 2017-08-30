# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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

