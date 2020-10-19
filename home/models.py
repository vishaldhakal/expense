from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class Project(models.Model):
    name = models.CharField(max_length = 500)
    members = models.ManyToManyField(User,blank=True)
    description = models.TextField()

    def calculateIncomings(self):
        reports = Report.objects.filter(Q(project=self) & Q(money_choice="Incoming"))
        tot = 0
        for rep in reports:
            tot = tot+rep.amount
        return tot
    
    def calculateOutgoings(self):
        reports = Report.objects.filter(Q(project=self) & Q(money_choice="Outgoing"))
        tot = 0
        for rep in reports:
            tot = tot+rep.amount
        return tot

class Report(models.Model):
    MONEY_CHOICES = [
    ('Incoming','Incoming'),
    ('Outgoing','Outgoing')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sdd")
    description = models.TextField()
    topic = models.CharField(max_length = 500)
    money_choice = models.CharField(max_length=200,choices=MONEY_CHOICES)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="sd",blank=True)
    amount = models.FloatField(default=0)

    def getFiles(self):
        getfiles = FileReport.objects.filter(report=self)
        return getfiles

class FileReport(models.Model):
    file = models.FileField()
    report = models.ForeignKey(Report,on_delete=models.CASCADE)