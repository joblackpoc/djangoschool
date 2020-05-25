from django.contrib import admin
<<<<<<< HEAD
from .models import ExamScore, AllStudent
# Register your models here.
admin.site.register(ExamScore)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['level','student_id','student_name','student_tel']
    list_filter = ['level']
    list_editable = ['student_tel']

admin.site.register(AllStudent, StudentAdmin)
=======
from .models import *
# Register your models here.
admin.site.register(ExamScore)
admin.site.register(AllStudent)
>>>>>>> 4596d35ae8ae9ba37200cfb91b36b6150ac0253a
