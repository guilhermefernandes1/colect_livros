from django import forms

from .models import User
from .models import Livros


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }


class AddBookForm(forms.ModelForm):

    class Meta:
        model = Livros
        fields = ('nome', 'descricao', )
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do Livro',
                                           'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'placeholder': 'Descrição do Livro',
                                                'class': 'form-control'}),
        }
