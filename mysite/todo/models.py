from django.db import models
from django.utils import timezone

# Create your models here.

# All classes that will be represented on db must inherit from 
# models.Model

#classes that inherit from models.Model become a table in db
class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title    
    
# After making a change here, to see it reflected on db
# you must run 
#       # This lets django see that models changed and what
#       python manage.py makemigrations
#       # This applies the changes to the db
#       python manage.py migrate