from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth')
    list_filter = ('date_of_birth',)  # filter by DOB
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Student, StudentAdmin)