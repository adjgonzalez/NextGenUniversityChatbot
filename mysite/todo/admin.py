from django.contrib import admin

from todo.models import Todo

# Register your models here.
#so you can CRUD it on Admin site
admin.site.register(Todo)