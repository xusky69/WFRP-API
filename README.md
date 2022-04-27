# WFRP-APP

A befautiful web app for managing D&D-like tabletop campaigns based off the Warhammer Fantasy universe.

## Description

WFRP-APP is a Progressive Web App (**PWA**) **frontend** **+** fully-fledged **backend** for managing Warhammer Fantasy Roleplaying Game (**WFRP**) 4th edition campaigns.  

### Main features:
- **Blazing-fast** frontend built on top of Next.js + TailwindCSS
- Native-like **PWA** experience made possible by Next.js PWA template
- Beautiful user experience thanks to the amazing [daisyUI](https://daisyui.com/) component library
- Fully-featured Django **REST API** for performing CRUD operations on several relational data models described by the WFRP 4eth edition rulebook such as **Campaigns, Characters, Spells, Items, Enemies, etc**.
- Integration with **AWS S3** (via django-storages) for storing & serving **user media** such as character avatars and bestiary illustrations.
- Complete **dungeon-master panel** thanks to the Django admin panel
- Full **docker** & compose support so you can host your own campaigns locally.
- Secure **stateless authentication** handled via [iron-session](https://github.com/vvo/iron-session)

### To be done
- Dungeon-master panel on the frontend side
- Desktop UI layout support
- Dice rolling tool

## Setting up development environment
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

## Setting up docker environment

## Some useful information:
- main app is wfrp
- url filtering is setup inside ViewSets using django-filters

## Environment variables

## F.A.Q.

## About this project

This project arose out of the need to provide our dungeon master an easy way to manage our WFRP campaign. 

It eventually morphed into a native-like PWA that can be used by any party of adventurers who might want to simplify their adventures on the  
