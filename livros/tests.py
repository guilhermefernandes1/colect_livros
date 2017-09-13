from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LivroIndexViewTests(TestCase):

    def test_sem_livros_cadastrados(self):
        """
        Se nao houverem livros cadastrados, deve-se retornar uma mensagem informando
        :return:
        """

        session = self.client.session
        session['username'] = 'guilhermefernandes1@gmail.com'
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
        session['username'] = None
        session.save()

        response = self.client.get(reverse('livros:show_livros'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livros/negado.html')


class LivroLoginViewTests(TestCase):

    def test_user_nao_existe_deve_continuar_tela_login(self):
        """
        Caso o usuario nao exista, deve permanecer na tela de login
        :return:
        """

        response = self.client.post(reverse('livros:login'), data={'username': 'teste',
                                                                   'password': 'teste'
                                                                   })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livros/login.html')

    def test_se_user_existe_ir_home(self):
        """
        Caso o usuario exista, deve ser redirecionado para a
        lista de livros
        :return:
        """

        user = User.objects.create_user(username='teste_guilherme',
                                        email='lennon@thebeatles.com',
                                        password='teste')
        user.save()

        response = self.client.post(reverse('livros:login'), data={'username': 'teste_guilherme',
                                                                   'password': 'teste'
                                                                   })

        self.assertTemplateUsed(response, 'livros/show_books.html')
