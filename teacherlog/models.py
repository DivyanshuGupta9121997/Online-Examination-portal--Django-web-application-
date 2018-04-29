from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ExamDetail(models.Model):
    date=models.DateField(blank=True,)
    Deptt=models.CharField(max_length=55,default=None,choices=(('Computer Science & Engineering','cse'),('Mathematics & Computing','mnc'),('Electronics Engineering','ece'),('Electrical Engineering','eee')))
    sem = models.CharField(max_length=10,default=None,choices=(('I', '1'), ('II', '2'), ('III', '3'),('IV', '4')))
    Exam_Code=models.CharField(max_length=40,default=None)
    ccode = models.CharField(max_length=10,default=None,choices=(('C1', '1'), ('C2', '2'), ('C3', '3'),('C4', '4'), ('C5', '5'),('C6', '6')))
    scode = models.CharField(max_length=50,default=None,choices=(('Engg. Mech', '1'), ('Discrete Mathematics', '2'), ('Computer System Organisation', '3'),('ITW', '4'), ('Probability & Statistics', '5'),('Education & Self', '6')))

    def __str__(self):
        return str(Exam_Code)+ ":-" + str(date)