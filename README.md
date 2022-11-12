Admin Area
user: admin password: onlyme519353

Prerequisites
Python
virtualenv pip install virtualenv
Installing
Passo a passo para a geração de um novo executável, caso venham a ser feita modificações no código.

Criar ambiente virtual: python -m venv venv

Ativar ambiente virtual: .\venv\Scripts\activate

(Desativar quando necessário) deactivate

Instalar dependências pip install -r .\requirements.txt

Criar executável python setup.py build

Após isso será criado um repositório build, onde ficará o executável e as suas dependências. Os arquivos necessários para o funcionamento do programa são todos os que estão dentro da pasta build

Execução do portal: python manage.py runserver

Depois executa o main.py