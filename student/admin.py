from django.contrib import admin
from student.models import user


class userAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','address','bio','degree','dp')
    
admin.site.register(user,userAdmin)
 
# Register your models here.
