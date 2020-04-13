# Django Practice

When creating a project, first set your environment via,

    $ pipenv install django

Then create your project by typing

    $ django-admin startproject {project_name}

After creating a project, then make an application (In Django, applications are modules of the project)

    $ python manage.py startapp {application_name}

And serve your project by using

    $ python manage.py runserver

Add your apps in the settings.py in `INSTALLED_APPS`, 

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        '{appName}.apps.{AppConfigClassName}'
    ]

You can now add migrations of the model by typing

    $ python manage.py makemigrations {app_name_in_installed_apps}