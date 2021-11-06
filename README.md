# drf
Django rest framework CRUD todo API.

### Setup

###### Dependencies
- Python 3.9
- Django 3.2

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed the django apps run on Windows, you should have little problem getting up and running.

```
https://github.com/fsfaysalcse/drf.git
cd drf
virtualenv venv --python=python3.9
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
