# Pocket recipes

## Setting up application
### Create local_settings.py and add there your secret key like this one
`SECRET_KEY = 'django-insecure-*jbh!@9g8=kn#o2y22a1&5)eg#*k&s!3#1fls#_aw#*+@hn^az'`

### Install requirements
Before this in location /static/ change path to public on yours
`$ pip install -r requirements.txt`

## Start project

### Make migrations
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

### Run project
`$ python3 manage.py runserver`
`127.0.0.1:8000/aaa/bb?c=11&d=17`

## Create superuser
`$ python3 manage.py createsuperuser`