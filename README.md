# WFRP-API

REST API for WFRP 4th edition campaign handling.

## Description

The project is built on top of **django** + **REST_framework**. 

### Main features:
 Provides models with REST CRUD support for:
 a. Campaign
 b. Journal Entries
 c. PlayableCharacters
 d. Spells
 e. Talent
 f. Item
2. 


## Dev env etup steps:
1. Clone repo & cd to root of the project
2. Make sure you have installed a modern python 3 in your current environment
3. Create `venv` or use virtual environment manager of your preference (conda, pyenv, etc...), then install dependencies. eg:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
4. cd to `django_project` and create a symlink between dev_env_vars and .env file (or just copy and rename):
```
ln dev_env_vars .env
```
5. create initial migrations
```
python manage.py makemigrations wfrp
python manage.py migrate
```
6. run development server
```
python manage.py runserver
```


## Some useful information:
- main app is wfrp
- url filtering is setup inside ViewSets using django-filters

