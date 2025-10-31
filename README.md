# LoopersIT fullstack web application

**Every time when you start the pc** </br>

```dj
sudo service postgresql start
source ptv/bin/activate
python manage.py runserver

```

**daatabase setup command step by step** </br>

```dj
sudo service postgresql start
sudo -u postgres createdb litdb
sudo -i -u postgres
psql
\password
```

**add password 1294** </br>
**exit the postgres by following commands or open a new terminal and cd to the /kathberali** </br>

```dj
\q
exit
```

**Every time run manage.py commad add the following flags** </br>

```dj
 python manage.py runserver --settings=config.settings.dev
 python manage.py makemigrations --settings=config.settings.dev
 python manage.py migrate --settings=config.settings.dev
 python manage.py createsuperuser --settings=config.settings.dev

```

**Every time run manage.py commad add the following flags for production** </br>

```dj
 python manage.py runserver --settings=config.settings.pro
 python manage.py makemigrations --settings=config.settings.pro
 python manage.py migrate --settings=config.settings.pro
 python manage.py collectstatic --settings=config.settings.pro
 python manage.py createsuperuser --settings=config.settings.pro

```

**OR (Reccomended) you can run the command in the terminal and use manag.py as usual ** </br>

```dj
 export DJANGO_SETTINGS_MODULE=config.settings.dev
 python manage.py runserver
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser

```
