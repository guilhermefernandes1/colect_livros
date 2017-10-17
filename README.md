# collect_livros
Simples repositório para treinar o uso da autenticacao no Django framework

App terá apenas uma página para listar livros cadastrados em uma base de dados. Esta lista será mostrada se o usuário
estiver autenticado. Caso contrario fará um render da pagina de login.

Objetivo é testar uso de sessions para autenticacao.

# Variaveis de ambiente:
export DJANGO_DB_ENGINE='django.db.backends.postgresql_psycopg2'

export DJANGO_DB_NAME='colect_livros'

export DJANGO_DB_USER='postgres'

export DJANGO_DB_PASSWORD=<password>

export DJANGO_DB_HOST='127.0.0.1'

export DJANGO_DB_PORT='5432'

