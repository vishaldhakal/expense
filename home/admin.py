from django.contrib import admin
from .models import Project,Report,FileReport,Tools

admin.site.register(Project)
admin.site.register(Report)
admin.site.register(FileReport)
admin.site.register(Tools)