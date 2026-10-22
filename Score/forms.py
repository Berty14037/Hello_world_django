from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = '__all__'

class DeleteScoreForm(forms.Form):
    name = forms.CharField(max_length=100)