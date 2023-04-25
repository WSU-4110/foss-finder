venv:
    python -m venv env
    env/bin/pip install -r requirements.txt


database:
    env/bin/python manage.py migrate
    env/bin/python manage.py loaddata initial_data.json

test:
    env/bin/python manage.py test


server:
    env/bin/python manage.py runserver
