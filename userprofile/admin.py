from django.contrib import admin
from .models import *

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','dob','phone']


    

admin.site.register(Member,MemberAdmin)