from django.contrib import admin
from .models import Project,Report,FileReport

admin.site.register(Project)
admin.site.register(Report)
admin.site.register(FileReport)