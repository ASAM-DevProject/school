from django.contrib import admin
from .models import *

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'date']
    search_fields = ['name', 'unit']
    list_filter = ['date', 'created', 'unit', 'updated', 'id']
    ordering = ['-date']

class TermAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    list_filter = ['date', 'created', 'updated', 'id']
    search_fields = ['name']
    ordering = ['-date']

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'status']
    list_filter = ['status', 'date', 'created', 'updated', 'id']
    search_fields = ['user']
    ordering = ['-date']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'status']
    list_filter = ['status', 'date', 'created', 'updated', 'id']
    search_fields = ['user']
    ordering = ['-date']

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'status']
    list_filter = ['status', 'date', 'created', 'updated', 'id']
    search_fields = ['user']
    ordering = ['-date']

class PresentationAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'term', 'date', 'status']
    list_filter = ['status', 'date', 'created', 'updated', 'id']
    search_fields = ['user', 'course', 'term']
    ordering = ['-date']

class GetAdmin(admin.ModelAdmin):
    list_display = ['presentation', 'date', 'status']
    list_filter = ['status', 'date', 'created', 'updated', 'id']
    search_fields = ['presentation']
    ordering = ['-date']

admin.site.register(CourseModel, CourseAdmin)
admin.site.register(TermModel, TermAdmin)
admin.site.register(ProfessorModel, ProfessorAdmin)
admin.site.register(StudentModel, StudentAdmin)
admin.site.register(ManagerModel, ManagerAdmin)
admin.site.register(PresentationModel, PresentationAdmin)
admin.site.register(GetModel, GetAdmin)