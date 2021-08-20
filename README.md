# gestor_cursos_django

Sistema de gestão de cursos desenvolvido em Python utilizando Django.  
Veja ele funcionando [aqui](https://django-gestor-cursos.herokuapp.com).


![badge github branch main](https://github.com/wfoschiera/gestor_cursos_django/actions/workflows/projeto_django.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/wfoschiera/gestor_cursos_django/branch/main/graph/badge.svg?token=hOrdm18erU)](https://codecov.io/gh/wfoschiera/gestor_cursos_django)
[![Python 3](https://pyup.io/repos/github/wfoschiera/gestor_cursos_django/python-3-shield.svg)](https://pyup.io/repos/github/wfoschiera/gestor_cursos_django/)
[![Updates](https://pyup.io/repos/github/wfoschiera/gestor_cursos_django/shield.svg)](https://pyup.io/repos/github/wfoschiera/gestor_cursos_django/)  

Para instalar, digite no terminal:

```sh
pip install poetry
poetry install
```

O poetry instalará todas as dependências do projeto. Para utilizar o projeto, copie o arquivo `contrib/env-sample` para
a pasta do projeto, renomeando-o para `.env`. Configure as variáveis de ambiente locais, bem como as variáveis de
ambiente do heroku, caso queira fazer uso para a entrega contínua.

Para executar o servidor:
```shell
python manage.py runserver
```
Caso seja desenvolvedor, instale a dependências e habilite o pre-commit hook para facilitar a verificação do código.
```shell
pre-commit install
```
O app rodará na porta padrão do localhost, acessível em: [127.0.0.1:8000](127.0.0.1:8000).

