# djangoschool
- study from uncle engineer
# install VS Code
- https://code.visualstudio.com/download

# extensions
- python -> ms-python.python Microsoft
- Bootstrap 4, Font awesome 4 -> Ashok Koyi
- Bracket Pair Colorizer -> CoenraadS
- Django -> Baptiste Darthenay
- vscode-icons -> VSCode Icons Team

# settings
- Commonly Used
- files Auto Save
- onFocusChange
- Ctrl+Shift+P
- python -> Select Linter -> pylint

# install python 3.8
<br>set user environment on top
<br>C:\Python38\
<br>C:\Python38\Scripts\
<br>C:\Python38\Lib\site-packages\

* upgrade pip
<br> python -m pip install --upgrade pip

* install pylint
<br>pip install pylint
<br>pip install --upgrade pylint
<br>
* install wheel
<br>pip install wheel
<br>pip install --upgrade wheel
<br>
* install virtualenv
<br>pip install virtualenv
<br>
* upgrade virtualenv 
<br>pip install --upgrade virtualenv
<br>
* สร้าง virtualenv ชื่อว่า venv
<br>virtualenv venv
<br>
* activate virtualenv
<br> .\venv\scripts\activate

<br>จะได้ => (venv) C:\folder's name>

# install django 3.0
<br>pip install django==3.0

* create project
<br>django-admin startproject djangoschool

* run server local
<br>cd djangoschool
<br>python manage.py runserver 127.0.0.1:80
<br>Ctrl + C = stop server

# create database
* python manage.py migrate
* python manage.py createsuperuser
<br>user:admin
<br>password:xxxxx
<br>localhost/admin

# create template website
<br>https://www.w3schools.com/bootstrap4/
* create folder template under app folder
* create folder same name as app's name -> school
* create html file -> base.html 
<br>https://www.dropbox.com/s/rzc5lldcrfdmpwy/base.html?dl=0
<br>and in the body 
<br>  put this code
<br><div class="container">
<br>{% block content %}
	<br>
	<br>put your content here
        <br>
<br>{% endblock content %}
<br></div>

# create home.html in template
<br>{% extends 'school/base.html' %} 
<br> extends from template base.html
<br>{% block content %}
<br><div class="container">
  <br><h1>Welcome to Django Framework</h1>
  <br><p>Learn Python Django From Uncle Engineer</p> 
  <br><img src="url image" width="800"></img>
<br></div>
<br>{% endblock content %}

# views.py
<br>from django.shortcuts import render
<br>
<br>def HomePage(request):
    <br>return render(request,'school/home.html')
<br>	
<br>def AboutPage(request):
    <br>return render(request,'school/about.html')
<br>
<br>def ContactUs(request):
    <br>return render(request,'school/contactus.html')

# urls.py djangoschool
<br>from django.contrib import admin
<br>from django.urls import path, include
<br>from django.contrib.auth import views as auth_views
<br>
<br>urlpatterns = [
    <br>path('admin/', admin.site.urls),
    <br>path('',include('school.urls'))
<br>]
<br>
# urls.py school
<br>from django.urls import path
<br>from .views import HomePage, AboutPage, ContactUs
<br>
<br>urlpatterns = [
    <br>path('',HomePage, name='home-page'),
    <br>path('about/', AboutPage, name='about-page'),
    <br>path('contact/', ContactUs, name='contact-page')
<br>]

# settings.py
<br>add your app on top
* INSTALLED_APPS = [
  <br>  'school',
<br>]	
<br>
<br>add template's path to DIRS
<br>
<br>TEMPLATES = [
    <br>{
        <br>'BACKEND': 'django.template.backends.django.DjangoTemplates',
        <br>'DIRS': [os.path.join(BASE_DIR, 'school/template')],
<br>]
<br>
- for static use this
--Static files (CSS, JavaScript, Images)
--https://docs.djangoproject.com/en/3.0/howto/static-files/
--https://docs.djangoproject.com/en/3.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development
<br>
<br>STATIC_URL = '/static/'
<br>
# create models
# models.py
<br>from django.db import models
<br>
<br>class ExamScore(models.Model):
    <br>allsubject = (('math','คณิตศาสตร์'),
          <br>         ('sci','วิทยาศาสตร์'),
          <br>         ('art','ศิลป'),
          <br>         ('eng','ภาษาอังกฤษ'),
          <br>         ('physics','ฟิสิกส์'),
          <br>         ('bio','ชีววิทยา')
                <br> )
    <br>subject = models.CharField(max_length=200, choices=allsubject, default='math')
    <br>student_name = models.CharField(max_length=200)
    <br>score = models.IntegerField(default=0)
# put this to show table's name
    <br>def __str__(self):
        <br>return self.student_name +' '+ self.subject +' '+ str(self.score)
<br>		
* add model to admin backends
# admin.py
<br>from django.contrib import admin
<br>from .models import ExamScore
--Register your models here.
<br>admin.site.register(ExamScore)




