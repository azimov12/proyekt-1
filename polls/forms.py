from django import forms
from .models import NewsModel


class NewsForm(forms.ModelForm):
    tittle_uz = forms.CharField()
    tittle_en = forms.CharField()
    tittle_ru = forms.CharField()

    body_uz = forms.CharField()
    body_en = forms.CharField()
    body_ru = forms.CharField()

    class Meta:
        model = NewsModel
        exclude = ('tittle', 'body')