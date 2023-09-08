from django.contrib import admin
from rabbi_001.models import teacher 

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 't_id', 't_name', 't_email')
admin.site.register(teacher, TeacherAdmin)
