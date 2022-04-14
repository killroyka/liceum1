from django import forms
from raitng.models import Raiting


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Raiting
        fields = ("star",)
