# Django-App
Aplicação básica para cadastro de usuários feita em Django com banco MySQL. Feita em 5 dias para uma vaga de estágio.

# Funções:
- Cadastro de usuários (email, cpf e nome);
  - Não permite cadastrar se já existir registro do email ou cpf.
- Listagem de todos os users no banco.


---------
# Requeriments:
Python3
-> Instalar requirements.txt e alterar a secret key.
```
pip install -r requirements.txt
```
Banco MySQL
-> É necessario criar um banco e em seguida mudar no código o nome do banco, user e senha;

-> Após o primeiro passo é necessário executar makemigrations e migrate para o banco ser configurado.
```
python manage.py makemigrations

python manage.py migrate
```


---------
# Executando:
```
pip manage.py runserver
```
Para parar aperte Ctrl+C no terminal
