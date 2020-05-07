# djangoschool
- study from uncle engineer
- install VS Code
- https://code.visualstudio.com/download

* extensions
- python -> ms-python.python Microsoft
- Bootstrap 4, Font awesome 4 -> Ashok Koyi
- Bracket Pair Colorizer -> CoenraadS
- Django -> Baptiste Darthenay
- vscode-icons -> VSCode Icons Team

* settings
- Commonly Used
- files Auto Save
- onFocusChange
- Ctrl+Shift+P
- python -> Select Linter -> pylint


* install python 3.8

set user environment on top
C:\Python38\
C:\Python38\Scripts\
C:\Python38\Lib\site-packages\

upgrade pip
python -m pip install --upgrade pip

install pylint
pip install pylint
pip install --upgrade pylint

install wheel
pip install wheel
pip install --upgrade wheel

install virtualenv
pip install virtualenv

upgrade virtualenv 
pip install --upgrade virtualenv

สร้าง virtualenv ชื่อว่า venv
virtualenv venv

activate virtualenv
.\venv\scripts\activate

จะได้ => (venv) C:\folder's name>

install django 3.0
pip install django==3.0

create project
django-admin startproject djangoschool



run server local
cd djangoschool
python manage.py runserver 127.0.0.1:80

Ctrl + C = stop server
create database
python manage.py migrate
python manage.py createsuperuser
user:admin
password:*****
localhost/admin

create template website
https://www.w3schools.com/bootstrap4/
create folder template under app folder
create folder same name as app's name -> school
create html file -> base.html 
https://www.dropbox.com/s/rzc5lldcrfdmpwy/base.html?dl=0
and in the body 
put this code
<div class="container">
{% block content %}
	-put your content here-
{% endblock content %}
</div>

create home.html in template
{% extends 'school/base.html' %} -> extends from template base.html
{% block content %}
<div class="container">
  <h1>Welcome to Django Framework</h1>
  <p>Learn Python Django From Uncle Engineer</p> 
  <img src="image address" width="800"></img>
</div>
{% endblock content %}

**views.py
from django.shortcuts import render

def HomePage(request):
    return render(request,'school/home.html')
	
def AboutPage(request):
    return render(request,'school/about.html')


def ContactUs(request):
    return render(request,'school/contactus.html')

*urls.py djangoschool
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('school.urls'))
]

**urls.py school
from django.urls import path
from .views import HomePage, AboutPage, ContactUs

urlpatterns = [
    path('',HomePage, name='home-page'),
    path('about/', AboutPage, name='about-page'),
    path('contact/', ContactUs, name='contact-page')
]

*settings.py
add your app on top
INSTALLED_APPS = [
    'school',
]	

add template's path to DIRS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'school/template')],
]

for static use this
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# https://docs.djangoproject.com/en/3.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development

STATIC_URL = '/static/'

create models
**models.py
from django.db import models

class ExamScore(models.Model):
    allsubject = (('math','คณิตศาสตร์'),
                    ('sci','วิทยาศาสตร์'),
                    ('art','ศิลป'),
                    ('eng','ภาษาอังกฤษ'),
                    ('physics','ฟิสิกส์'),
                    ('bio','ชีววิทยา')
                 )
    subject = models.CharField(max_length=200, choices=allsubject, default='math')
    student_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
#put this to show table's name
    def __str__(self):
        return self.student_name +' '+ self.subject +' '+ str(self.score)
		
add model to admin backends
**admin.py
from django.contrib import admin
from .models import ExamScore
# Register your models here.
admin.site.register(ExamScore)




