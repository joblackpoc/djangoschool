from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ExamScore, AllStudent


def HomePage(request):
    return render(request,'school/home.html')


def AboutPage(request):
    return render(request,'school/about.html')


def ContactUs(request):
    return render(request,'school/contactus.html')    


def ShowScore(request):
    score = ExamScore.objects.all()
    context = {'score':score}
    return render(request,'school/showscore.html', context)

def Register(request):

    if request.method=='POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()  
        return redirect('home-page')
    return render(request,'school/register.html')

##########Search Page############
    #MODELS.objects.all() ดึงค่าทั้งหมด
    #MODELS.objects.get(student_id='')ดึงค่าตัวเดียว หากเกินจะ error
    #MODELS.objects.filter(level='ม.1.')ดึงหลายค่า
    #search = AllStudent.objects.get(student_id=)
#################################
@login_required(login_url='login')
def SearchStudent(request):

    if request.method == 'POST':
        data = request.POST.copy()
        searchid = data.get('search')
        print(searchid, type(searchid))
        try:
            result = AllStudent.objects.get(student_id=searchid)
            print('RESULT',result)
            context = {'result':result, 'checked':'found'}
        except:
            context = {'result':'No Data Please put student id','checked':'notfound'}

        return render(request, 'school/search.html', context)

    return render(request, 'school/search.html')












