from django.contrib import admin
from .models import *

admin.site.register(ordermodel)
admin.site.register(menumodel)
admin.site.register(usersetting)

class studentsadmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'First_Name', 'Last_Name', 'Signed_Up']

admin.site.register(student, studentsadmin)
