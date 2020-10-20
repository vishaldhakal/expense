from django.shortcuts import render,redirect
from .models import Project,Report,FileReport
from django.contrib.auth.models import User
from django.http import HttpResponse
import os.path
import csv
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _handle_uploaded_file(file):
    destination = open(os.path.join(BASE_DIR, 'media/{}'.format(file.name)), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

def index(request):
    return render(request, 'index.html')

def add_project(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        neww = Project.objects.create(name=name,description=description)
        neww.save()

    projects_list = Project.objects.all()
    ctx = {
        'projects':projects_list
    }
    return render(request, 'add_project.html',ctx)

def project_edit(request,id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        players = request.POST.getlist('members')
        project.members.clear()
        for pll in players:
            userrr = User.objects.get(id=pll)
            project.members.add(userrr)
        project.name = name
        project.description = description
        project.save()
        return redirect('add_project')
    else:
        allusers = User.objects.all()
        ctx = {
            'users':allusers,
            'project':project,
        }
        return render(request, 'edit_project.html',ctx)

def remove_project(request):
    return render(request, 'remove_credit.html')

def overview(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    projects_list = Project.objects.all()
    referer = str(request.META.get('HTTP_REFERER'))
    ctx = {
        'projects':projects_list,
        'back_page':referer
    }
    return render(request, 'overview.html',ctx)

def project_single(request,id):
    proj = Project.objects.get(id=id)
    reports = Report.objects.filter(project=proj)
    referer = str(request.META.get('HTTP_REFERER'))

    ctx = {
        'reports':reports,
        'project':proj,
        'back_page':referer
    }
    return render(request, 'project_single.html',ctx)

def report_submit(request,id):
    proj = Project.objects.get(id=id)
    if request.method == "POST":
        topic = request.POST['topic']
        amount = request.POST['amount']
        moneytype = request.POST['moneytype']
        cashtype = request.POST['cashtype']
        description = request.POST['description']
        files = request.FILES.getlist('file')
        user = User.objects.get(id=request.user.id)
        inst = Report.objects.create(user=user,topic=topic,project=proj,description=description,money_choice=moneytype,amount=amount,money_method=cashtype)
        inst.save()
        for afile in files:
            _handle_uploaded_file(afile)
            fil = FileReport.objects.create(file=afile,report=inst)
            fil.save()
    return redirect('project_single',id)

def report_single(request,id):
    report = Report.objects.get(id=id)
    referer = str(request.META.get('HTTP_REFERER'))

    ctx = {
        'report':report,
        'back_page':referer
    }
    return render(request, 'report_single.html',ctx)
    
def edit_report(request,id):
    report = Report.objects.get(id=id)
    referer = str(request.META.get('HTTP_REFERER'))

    ctx = {
        'report':report,
        'back_page':referer
    }
    return render(request, 'edit_report.html',ctx)

def delete_report(request,id):
    report = Report.objects.get(id=id)
    idd = report.project.id
    report.delete()
    return redirect('project_single',idd)

def update_report(request,id):
    report = Report.objects.get(id=id)
    referer = str(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        topic = request.POST['topic']
        amount = request.POST['amount']
        moneytype = request.POST['moneytype']
        cashtype = request.POST['cashtype']
        description = request.POST['description']    
        report.topic=topic
        report.description=description
        report.money_choice=moneytype
        report.money_method=cashtype
        report.amount=amount
        report.save()

    proj = report.project.id 
    return redirect('project_single',proj)

def lab(request):
    return render(request, 'lab.html')  

def project_task(request,id):
    project = Project.objects.get(id=id)
    referer = str(request.META.get('HTTP_REFERER'))
    ctx = {
        'project':project,
        'back_page':referer
    }
    return render(request, 'projects_task.html',ctx) 

def settings(request):
    return render(request, 'settings.html')  

def export_csv(request,id):
    project = Project.objects.get(id=id)
    reports = Report.objects.filter(project=project)
    response = HttpResponse(content_type='text/csv')
    response["Content-Disposition"] = 'attachment; filename=Reports'+'for'+str(project.name)+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['User','Description','Topic','Type','Amount'])
    for report in reports:
        writer.writerow([report.user,report.description,report.topic,report.money_choice,report.amount])

    return response