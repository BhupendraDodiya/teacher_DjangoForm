from django.contrib import admin
from .models import Teacher
# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','dob','gender','hobby','image']