from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add-project/',views.add_project,name="add_project"),
    path('project-edit/<int:id>',views.project_edit,name="project_edit"),
    path('remove-project/',views.remove_project,name="remove_project"),
    path('overview/',views.overview,name="overview"),
    path('edit-report/<int:id>',views.edit_report,name="edit_report"),
    path('delete-report/<int:id>',views.delete_report,name="delete_report"),
    path('update-report/<int:id>',views.update_report,name="update_report"),
    path('project-single/<int:id>',views.project_single,name="project_single"),
    path('report-single/<int:id>',views.report_single,name="report_single"),
    path('report-submit/<int:id>',views.report_submit,name="report_submit"),
    path('settings/',views.settings,name="settings"),
]
