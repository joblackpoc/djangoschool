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

    def __str__(self):
        return self.student_name +' '+ self.subject +' '+ str(self.score)