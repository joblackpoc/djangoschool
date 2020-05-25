from django.contrib import admin
from .models import ExamScore, AllStudent
# Register your models here.
admin.site.register(ExamScore)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['level','student_id','student_name','student_tel']
    list_filter = ['level']
    list_editable = ['student_tel']

admin.site.register(AllStudent, StudentAdmin)