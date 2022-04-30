# WFRP-APP
---

![wfrp-app-preview](https://i.imgur.com/DDXg05H.jpeg)

A web app for managing D&D-like tabletop campaigns based off the Warhammer Fantasy universe. 

This app is a work-in-progress and currently needs to be set up by a person with knowledge in web development/docker; although after set-up can be used by anyone with a smartphone and a wi-fi connection.

## Description
---
WFRP-APP is a Progressive Web App (**PWA**) **frontend** **+** fully-fledged **backend** for managing Warhammer Fantasy Roleplaying Game (**WFRP**) 4th edition campaigns.  

- [[link]](https://github.com/xusky69/WFRP-API) **Backend repo**
- [[link]](https://github.com/xusky69/WFRP-Front) **Frontend repo**

### User features:

- Visualize your character sheet, party details, bestiary, etc
- Dungeon master panel for managing every single detail of your campaign
- Register important moments of your campaign using the *campaign journal*, or upload them as pictures using the *memories* system
- Can be installed in your phone to be used like a native app 

### Techinal features:

- **Blazing-fast** frontend built on top of Next.js + TailwindCSS
- Native-like **PWA** experience made possible by the excellent Next.js PWA template, with offline content support
- **Beautiful** user interface thanks to the amazing [daisyUI](https://daisyui.com/) component library
- Fully-featured Django **REST API** for performing CRUD operations on several relational data models described by the WFRP 4eth edition rulebook such as **Campaigns, Characters, Spells, Items, Enemies, etc**; with support for querystring filtering
- Integration with **AWS S3** (via django-storages) for storing & serving **user media** such as character avatars and bestiary illustrations
- Total control over your campaign via the **dungeon-master panel** thanks to the Django admin panel
- Secure **stateless authentication** handled via [iron-session](https://github.com/vvo/iron-session)
- Full **docker** & compose support so you can host your own campaigns locally

## To be done
---
by order of priority:
- Dungeon-master panel on the frontend side
- User Registration on the frontend side
- Campaign creation on the frontend side
- User panel for managing campaigns and players
- Dice rolling tool
- Skill-check tool
- Desktop UI layout support

After all the above is done, the idea is to release the app on a powerful-enough production environment, ideally financed by a patreon/crowdsourcing strategy, so that all users can access the app for free directly from one single url.

## F.A.Q.
---
**Q:** Do you plan on doing this for D&D? 
**A:** Would be cool but would need some help! I'm currently learning the D&D 5th edition systems

**Q:** Why no typescript? 
**A:** Had some issues with iron-session ts support during early stages of this project, so I stuck with js for the meantime


## Environment variables
---

### Backend

| Name | Description |
| ------------- | ------------- |
| TIME_ZONE | server timezone |
| DEBUG | django debug flag |
| DOCKER | flag used in `settings.py` to enable the docker postgres db |
| HEROKU | flag used in `settings.py` to enable the heroku postgres db |
| CLOUD_MEDIA | flag used in `settings.py` to enable the AWS S3 media storage |
| DB_NAME | postgres DB name. Used by docker & heroku |
| DB_USER | postgres username. Used by docker & heroku |
| DB_PSWD | postgres password. Used by docker & heroku |
| DB_HOST | postgres DB host. Used by docker & heroku |
| DB_PORT | postgres DB port. Used by heroku |
| HEROKU_URL | used in `settings.py` to add the heroku url to ALLOWED_HOSTS |
| PROJECT_PATH | used by the heroku subdir buildpack to point the location of the django project |

The following environment variables are sentitive and should be stored in a `django_project/local_env_vars` file for development or directly in your cloud provider settings when deploying the project.

| Name | Description |
| ------------- | ------------- |
| AWS_ACCESS_KEY_ID | AWS S3 credential, used by django-storages if `CLOUD_MEDIA=='TRUE'`  |
| AWS_S3_REGION_NAME | AWS S3 bucket region, used by django-storages if `CLOUD_MEDIA=='TRUE'` |
| AWS_SECRET_ACCESS_KEY | AWS S3 credential, used by django-storages if `CLOUD_MEDIA=='TRUE'` |
| AWS_STORAGE_BUCKET_NAME | AWS S3 bucket name, used by django-storages if `CLOUD_MEDIA=='TRUE'` |

### Frontend

loaded from `WFRP_FRONT/.env.development` by the local dev server, from `WFRP_FRONT/.env.production` by the local build server and by the project environmnent variables when deploying to vercel.

| Name | Description |
| ------------- | ------------- |
| NEXT_PUBLIC_API_URL | REST API url |

## Setting up dev environment
---
### Setting up the backend

1. Clone the backend repo & cd to root of the project
2. Make sure you have installed a modern python 3 (>3.7) in your current environment
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
6. populate db with default data
```
python manage.py runscript wfrp.scripts.populate_db
```
7. run development server
```
python manage.py runserver
```
The backend will be served at localhost:8000

**Warning:** database data is stored at volume `django_project/db.sqlite3` & user media at volume `django_project/media`. If you delete any of these, you will lose your campaign data.

### Setting up the frontend

1. cd to the `WFRP-Front` located in the root of the backend repo and clone the frontend repo in the root of such folder 
```
git clone https://github.com/xusky69/WFRP-Front .
```
2. run `npm install` to install the required dependencies
3. run `npm run dev` to run the development server

The frontend will be server at localhost:3000

Remember that anyone connected to your wifi network should be able to connect to the frontend at `<your_pc_local_ip>:3000`, so you can host your campaign locally.

## Setting up docker environment
---
The docker environment is ideal for testing production-like environments; and also for hosting campaigns on your local wi-fi network using a pc connected to such network as a server and with minimal setup. **Currently, the Docker environment only works in linux-based operating systems**.

1. Clone the backend repo & cd to root of the project
2. cd to the `WFRP-Front` located in the root of the backend repo and clone the frontend repo in the root of such folder 
```
git clone https://github.com/xusky69/WFRP-FrontREPO_URL .
```
3. build docker images and compose-up:
```
docker-compose up --build
```
4. run the initial migrations
```
docker-compose exec django python manage.py makemigrations users
docker-compose exec django python manage.py makemigrations wfrp
docker-compose exec django python manage.py migrate
```
5. populate the db with default data 
```
docker-compose exec django python manage.py runscript wfrp.scripts.populate_db
```

Now you can just run the project via `docker-compose up` and turn it off via `docker-compose down`. 

The backend will be served at `localhost:8000` and the frontend at `localhost:3000`

Remember that anyone connected to your wifi network should be able to connect to the frontend at `<your_pc_local_ip>:3000`, so you can host your campaign locally.

**Warning:** database data is stored at volume `./postgres_data` & user media at volume `docker_media_root`. If you delete any of these folders, you will lose your campaign data.

## Deploying the project
---
This project can be deployed using the free tiers of Vercel, Heroku + Heroku Postgres and AWS S3. 

Environment variables are prepared in both the frontend and backend in order to transition seamlessly from the development environment to a production one that uses the aforementioned services (read the environment variables section)

An example architecture of a production environment is the following:

![wfrp-app-arch](https://i.imgur.com/JAFwPXD.png)

**Useful info**
- When deploying the API to heroku, you must use the `heroku/python` and the `heroku-subdir` (https://github.com/timanovsky/subdir-heroku-buildpack.git) buildpacks, then setup the required environment variables in the heroku ui.
- When deploying the frontend to Vercel, remember to setup the `NEXT_PUBLIC_API_URL` environment variable in the Vercel UI. Also, **you must add the Vercel project url** to the `domains` array in your `next.config.js` file, e.g:
```
  images: {
    domains: ['localhost', 'wfrp-api.s3.amazonaws.com'],
  },
```
- In order to populate the heroku db with the default data, you must connect to the API dyno via `heroku run bash --app YOUR_APP_NAME` and manually run the django script

## How to use
---
After populating the database with the default data:
1. head to `localhost:8000/admin` and login with username `admin` & password `123`. In the users section you can change your password and manage the user accounts of the default characters. **This will be your dungeon master panel**. 
2. Head to `localhost:8000/` and click campaigns, write down the uuid of your campaign.
3. users can login via the app frontend, served at `localhost:3000`. They must input their user data (defined by you in the dungeon master panel) and the campaign uuid.
4. Enjoy!

## About this project
---
This project arose out of the need to provide our dungeon master an easy way to manage our WFRP 4th edition campaign. 

It eventually morphed into a web tool that can be used by any party of adventurers who might need some help during their adventures in the grim darkness of the Old World. 

## Contributing
---
Please use the corresponding frontend/backend repos to PR any changes/features you wish to contribute. Any help is highly appreciated!

This project is licensed under the copyleft GPLv3 license and I'm personally against releasing it comercially. If you do release a commercial, lucrative implementation of this project, I will ask you to publish the entire source code.

## Disclaimer
---
This open-source project **does not intend to replace** the official Warhammer Fantasy RPG 4th edition material published by Cubicle 7 and licensed by Games Workshop. Instead, it acts as a **supplement** to the above, with the intent to **facilitate WFRPG campaigns**, specially to novice players & dungeon masters.

The assets used by the default content database population scripts were extracted from the WFRPG 4th edition digital starter pack.
