from django.contrib import admin

from .models import Batch,Student,Dorm,User

admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(Dorm)
admin.site.register(User)