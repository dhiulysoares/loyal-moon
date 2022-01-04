<h1>Loyalt program</h1>

<p>
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/dhiulysoares/loyal-moon.svg">

  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/dhiulysoares/loyal-moon.svg">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/dhiulysoares/loyal-moon.svg">

  <a href="https://github.com/dhiulysoares/loyal-moon/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/dhiulysoares/loyal-moon.svg">
  </a>

  <a href="https://github.com/dhiulysoares/loyal-moon/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/dhiulysoares/loyal-moon.svg">
  </a>

  <img alt="GitHub" src="https://img.shields.io/github/license/dhiulysoares/loyal-moon.svg">
</p>

<p>
  <a href="#como-usar">Como Usar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#endpoints">Endpoints</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licença">Licença</a>
</p>

## Como usar

Para clonar e desenvolver essa aplicação você vai precisar do [Git](https://git-scm.com) e [Django](https://docs.djangoproject.com/en/3.2/topics/install/) instalados no computador. No seu terminal:

```bash
git clone https://github.com/dhiulysoares/loyal-moon
```

Abra o projeto no seu editor preferido.

Crie sua [variável de ambiente](https://docs.python.org/pt-br/3/library/venv.html).

Instale as dependências:

```bash
pip install -r requirements.txt
```

Em seguida, rode os comandos a seguir para configurar o banco:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crie seu usuário:

```bash
python manage.py createsuperuser
```

Após criar o usuário rode a aplicação:

```bash
python manage.py runserver
```

Abra em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Endpoints


```bash
GET - http://127.0.0.1:8000/Client/
POST - http://127.0.0.1:8000/Client/
GET - http://127.0.0.1:8000/Indication/
POST - http://127.0.0.1:8000/Indication/
```

## Licença

Esse projeto usa a licença [MIT](https://github.com/dhiulysoares/loyal-moon/blob/master/LICENSE).
