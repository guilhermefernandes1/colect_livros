from django.test import TestCase
from django.urls import reverse

from .models import Livros


class LivroIndexViewTests(TestCase):

    def test_sem_livros_cadastrados(self):
        """
        Se nao houverem livros cadastrados, deve-se retornar uma mensagem informando
        :return:
        """

        session = self.client.session
        session['email'] = 'guilhermefernandes1@gmail.com'
        session.save()

        response = self.client.get(reverse('livros:show_livros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nenhum livro encontrado')

        self.assertQuerysetEqual(response.context['book_list'], [])

    def test_sem_sessao(self):
        """
        Caso nao haja o campo email na sessao, deve retornar a pagina de acesso negado
        :return:
        """

        response = self.client.get(reverse('livros:show_livros'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livros/negado.html')

    def test_email_none_sessao(self):
        """
        Caso o campo email esteja vazio na sessao, deve retornar a pagina de acesso negado
        :return:
        """

        session = self.client.session
        session['email'] = None
        session.save()

        response = self.client.get(reverse('livros:show_livros'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livros/negado.html')
