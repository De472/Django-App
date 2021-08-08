# Django-App
Aplicação básica para cadastro de usuários feita em Django com banco MySQL. Feita em 5 dias para uma vaga de estágio.

# Funções:
- Cadastro de usuários (email, cpf e nome);
  - Não permite cadastrar se já existir registro do email ou cpf.
- Listagem de todos os users no banco.


---------
# Requeriments:
Python3
-> Instalar requirements.txt
```
pip install -r requirements.txt
```
-> Alterar no código (settings.py) a secret key, allowed hosts->[]

Banco MySQL
-> É necessario criar um banco e em seguida mudar no código (settings.py) o nome do banco, host, user e senha;

-> Após o primeiro passo é necessário executar makemigrations e migrate para o banco ser configurado com segurança.
```
python manage.py makemigrations

python manage.py migrate
```


---------
# Executando:
```
python manage.py runserver
```
Para parar aperte Ctrl+C no terminal.
