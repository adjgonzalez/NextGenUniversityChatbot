# from django import forms

# from .models import Feedback, AnonymousFeedback

# class FeedbackForm(forms.ModelForm):
#    class Meta:
#        model = Feedback
#        exclude = ('user',)

# class AnonymousFeedbackForm(forms.ModelForm):
#    class Meta:
#        model = AnonymousFeedback
#        exclude = ('user',)


from django import forms

from .models import AnonymousFeedback, Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ("user",)
        # --- ADD THIS WIDGETS SECTION ---
        widgets = {
            "type": forms.Select(attrs={"class": "form-select form-select-lg"}),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                    "rows": 7,
                    "placeholder": "Let us know how we can improve...",
                }
            ),
        }


class AnonymousFeedbackForm(forms.ModelForm):
    class Meta:
        model = AnonymousFeedback
        exclude = ("user",)
        # --- ADD THIS WIDGETS SECTION ---
        widgets = {
            "type": forms.Select(attrs={"class": "form-select form-select-lg"}),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                    "rows": 7,
                    "placeholder": "Let us know how we can improve...",
                }
            ),
        }
