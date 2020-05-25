from django.db import models

class ExamScore(models.Model):
    allsubject = (('คณิตศาสตร์','math'),
                    ('วิทยาศาสตร์','วิทยาศาสตร์'),
                    ('ศิลป','ศิลป'),
                    ('อังกฤษ','ภาษาอังกฤษ'),
                    ('ฟิสิกส์','ฟิสิกส์'),
                    ('ชีววิทยา','ชีววิทยา')
                 )
    subject = models.CharField(max_length=200, choices=allsubject, default='คณิตศาสตร์')
    student_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name +' '+ self.subject +' '+ str(self.score)

class AllStudent(models.Model):
    levelist = (('ม.1','ม.1'),
                 ('ม.2','ม.2'),
                 ('ม.3','ม.3'),
                 ('ม.4','ม.4'),
                 ('ม5','ม.5'),
                 ('ม.6','ม.6'))
    
    level = models.CharField(max_length=100, choices=levelist, default='ม.1')
    student_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=100)
    student_tel = models.CharField(max_length=100, blank=True, null=True)
    parent_name = models.CharField(max_length=200, blank=True, null=True)
    parent_tel = models.CharField(max_length=100, blank=True, null=True)
    other = models.TextField(blank=True, null=True)

    def __str__(self):
<<<<<<< HEAD
        return '{}-{}-{}'.format(self.student_id,self.student_name,self.student_tel)
=======
        return self.student_name+' ชั้น '+ self.level+' โทร.'+ self.student_tel +' ผู้ปกครอง '+ self.parent_name +' โทร. '+ self.parent_tel
>>>>>>> 4596d35ae8ae9ba37200cfb91b36b6150ac0253a
