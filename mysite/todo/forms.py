from django import forms
from .models import Todo

#inherit from ModelForm, so Django will build the form from the model
class TodoForm(forms.ModelForm):
    #Configure what to build
    class Meta:
        #Model to use
        model = Todo
        #What to display. You can say fields=['title', 'date'] 
        #for specifics
        fields = "__all__"

        # HELLO WORLD, THIS IS A NEW CHANGE