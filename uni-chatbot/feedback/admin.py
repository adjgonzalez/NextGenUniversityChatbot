from django.contrib import admin

from .models import Feedback, AnonymousFeedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'type' , 'time'] 

@admin.register(AnonymousFeedback)
class AnonymousFeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'type' , 'time']
