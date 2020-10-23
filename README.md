# Projetos para seletiva de trainee na empresa Direction Systems

Como proposta para seleção criei alguns projetos e adcionei outros que estavam em andamento, para serem avaliados nessa fase da seletiva.
Para obter os códigos e projetos basta clonar o repositório ou fazer download em modo ZIP indicados na imagem.
>![inicio](https://user-images.githubusercontent.com/49026950/96831190-feb25900-1412-11eb-87a8-636b22e97300.png)

## Liguagens, ferramentas e frameworks usados
[![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
![HTML5](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
[![BOOTSTRAP](https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

## Projetos
- Formulário de cadastro com HTML, CSS e validações em JavaScript
- CRUD de pacientes com Python e Django
- Consumindo API do Youtube com Python e Django
- Sitema para agendamentos de postagens em redes sociais (Syscron)

## Formulário de cadastro com HTML, CSS e validações em JavaScript
Desenvolvido com HTML e CSS, a validação deste formulário é feita em JavaScript. Tentando aplicar as boas praticas do Clean Code, todo script que faz a
validação foi feito com conceitos de orientação a objetos.
>![cad-valid02](https://user-images.githubusercontent.com/49026950/96935326-344e5500-149a-11eb-8fe2-725eb5eb31ff.png)
>![cad-valid03](https://user-images.githubusercontent.com/49026950/96935348-43350780-149a-11eb-90ae-ad12513ca3e1.png)

## CRUD de pacientes com Python e Django
Sistema simples para fazer operações CRUD, criado para estudos na linguagem Python e o framework Django. Para rodar o sistema é necessário ter a versão 3.7 do python
e criar uma virtual environment. Códigos para criar um ambiente virtual:
```
$ cd proj-ecope
$ pipenv install
```
Para instalar o Django
```
$ pipenv install django
```
Criando o banco de dados e fazendo as migrações e iniciando o server
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
>![crud-py01](https://user-images.githubusercontent.com/49026950/96938397-ab86e780-14a0-11eb-8228-ed714740e301.png)
>![crud-py02](https://user-images.githubusercontent.com/49026950/96938735-8f377a80-14a1-11eb-9276-293466f111e5.png)
>![crud-py03](https://user-images.githubusercontent.com/49026950/96938772-9fe7f080-14a1-11eb-8119-bef6edb9d8a2.png)

## Consumindo API do Youtube com Python e Django
Aprimorando conhecimentos na linguagem e framework utilizados, realizei um pequeno trecho de código que consome a API do Youtube.
O sistema pesquisa uma playlist no youtube e retorna os vídeos na página especificada. Também é necessário criar um ambiente virtual.
```
$ pipenv install
$ python manage.py runserver
```
>![youtube-data-api](https://user-images.githubusercontent.com/49026950/96939329-25b86b80-14a3-11eb-81c7-a5cddba1e674.png)

## Sitema para agendamentos de postagens em redes sociais (Syscron)
Projeto criado com o intuito de agendar posts nas redes sociais e ser comercializado. Para divulgação de produtos, games e entre outros
o Syscron vai ser integrado com a principal rede social que é o Facebook. Totalmente feito em Python e Django, ainda está em sua fase de pré-projeto mas ja possui
uma boa autenticação de usuários com cadastro, login e recuperação de senha. Também precisa criar um ambiente virtual, e instalar as dependencias do projeto.

Para rodar o Syscron é necessário ter o Docker, pois estou utilizando containers para desenvolver com o banco de dados Postgres. Dando início no projeto, segue os códigos:
```
$ cd projetosys
$ pipenv install
$ cd syslab
$ docker-compose up
```
Feito isso, irá criar e subir o banco. Agora basta fazer as migrações no django e rodar o server
```
$ python manage.py migrate
$ python manage.py runserver
```
>![syscron01](https://user-images.githubusercontent.com/49026950/96942821-93b56080-14ac-11eb-944c-5d678eaa1c44.png)
>![syscron02](https://user-images.githubusercontent.com/49026950/96942826-9748e780-14ac-11eb-96de-ea551fa19994.png)
>![syscron03](https://user-images.githubusercontent.com/49026950/96942832-9adc6e80-14ac-11eb-9977-a7646fe8e976.png)
>![syscron04](https://user-images.githubusercontent.com/49026950/96942841-9f088c00-14ac-11eb-8922-ed7ef667a66b.png)
>![syscron05](https://user-images.githubusercontent.com/49026950/96942848-a3cd4000-14ac-11eb-879d-46b8a8989aa2.png)
