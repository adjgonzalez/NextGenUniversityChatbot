from django.shortcuts import render 
from .forms import FeedbackForm, AnonymousFeedbackForm
from django.contrib import messages

def feedback_form(request):
    form_class = FeedbackForm if request.user.is_authenticated else AnonymousFeedbackForm
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            
            if request.user.is_authenticated:
                feedback.user = request.user
            
            feedback.save()
            
            messages.success(request, "Feedback sent successfully!")
            
            context = {
                'form': form_class()  
            }
            return render(request, 'feedback/feedback_form.html', context)
        

    else:
        
        form = form_class()

    context = {
        'form': form 
    }
    return render(request, 'feedback/feedback_form.html', context)
