from django.contrib import admin

from .models import process_file_repo,Project

# Register your models here.
admin.site.register(process_file_repo)
admin.site.register(Project)