from django import forms
from .models import Club , Trophy 
class CreateCelebrities(forms.Form):
    name = forms.CharField(max_length=100)
    image = forms.ImageField()
    profession = forms.CharField(max_length=100)
    discription = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=forms.DateInput, )
    
    club = forms.ModelChoiceField(queryset = Club.objects.all())
    trophy = forms.ModelMultipleChoiceField(queryset=Trophy.objects.all() , widget=forms.CheckboxSelectMultiple)


class SearchForm(forms.Form):
    search = forms.CharField(required=False)
    club = forms.ModelMultipleChoiceField(queryset=Club.objects.all(),required=False)
    trophy = forms.ModelMultipleChoiceField(queryset=Trophy.objects.all(), required= False)
