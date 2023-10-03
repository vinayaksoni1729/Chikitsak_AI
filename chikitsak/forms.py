from django import forms
from .models import ProblemInput
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, CharField


class add_data(forms.ModelForm):
    class Meta:
        model = ProblemInput
        fields = ["problem"]
        widgets = {
            "problem": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 50vw; min-width:50vw; background:#3C3C3C; margin-bottom:10px; border:none; font-size:20px;color: white; opacity:0.8; padding:10px;border-radius:20px",
                    "placeholder": "Name",
                }
            )
        }
