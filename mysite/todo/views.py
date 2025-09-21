from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    #Get all items on Todo table. Sort descending by date
    item_list = Todo.objects.order_by("-date")
    
    #if the request received was a post
    if request.method == "POST":
        #Create new form
        form = TodoForm(request.POST)
        #Validate it (max chars in Charfield etc)
        if(form.is_valid()):
            #Insert to db
            form.save()
            #Refresh the page with new data
            return redirect('todo')
    #else show empty form
    form = TodoForm()

    #creates data to pass to the template
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO_LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed!!!")
    return redirect('todo')