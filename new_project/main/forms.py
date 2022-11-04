from django import forms
from .models import Film, Director
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from . import models


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'director': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'producer': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if models.Film.objects.filter(title=title).count() > 0:
            raise ValidationError("Film already exists!!!")
        return title


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(title=name).count() > 0:
            raise ValidationError('такой director уже есть!')
        return name
