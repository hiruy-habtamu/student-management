from django.contrib import admin

from .models import Batch,Student,Dorm

admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(Dorm)