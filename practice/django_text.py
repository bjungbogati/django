sudo apt-get update
sudo apt-get install python3


command-line
$ mkdir djangogirls
$ cd djangogirls



 sudo apt-get install python3-venv


### create virtual environment ###

python3 -m venv myvenv

### activate django ###

source myvenv/bin/activate


### Install Django ###

pip install --upgrade pip 

pip install django

### Create Django Project ###

django-admin startproject mysite .

### Project Hierachy ###
djangogirls
├───manage.py
└───mysite
        settings.py
        urls.py
        wsgi.py
        __init__.py


### mysite/settings.py ###

TIME_ZONE = 'Asia/Kathmandu'



### mysite/settings.py ###


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

### mysite/settings.py ###

### Leave it blank [] if you're running locally ###

ALLOWED_HOSTS = ['127.0.0.1', '<your_username>.pythonanywhere.com']


### Set up a database mysite/settings.py ###

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


### ENTER this in terminal ###

python manage.py migrate


### Starting the web server ###

python manage.py runserver (UNIX)

python manage.py runserver 0:8000 (for Windows)


### Browse it ###

http://127.0.0.1:8000/  , or

http://localhost:8000/


### Django Model ###

### Create an application ###

python manage.py startapp blog


### Create Django Model ###

djangogirls
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py



### mysite/settings.py ###

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]


### Creating a blog/models.py ###


from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


### Create tables for models in your database ###

python manage.py makemigrations blog


python manage.py migrate blog



### Django Admin ###

from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)


### Django url patterns ###
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]


















































djangogirls
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


### Tell django to use the  new app has ben installed ###

### mysite/settings.py ###

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', ### ADD this line ###
]









