# django-traders-app

Instalar para cargar las variables de entorno

<code>pip install python-dotenv</code>

En raiz del proyecto crear el archivo .env y agregar la variable SECRET_KEY

<code>SECRET_KEY = 'aqui_va tu SECRET_KEY'</code>
  
Ejecutar las migraciones e inicializar el servidor!

<code>python manage.py migrate
  
  python manage.py runserver
</code>

La App se ejecutara en  http://127.0.0.1:8000
