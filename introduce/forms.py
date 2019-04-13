from django import forms
from .models import Introduce_Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Introduce_Post
        fields={'title','text','author',}

#class PostForm(forms.form):
    #title = forms.CharField(label='제목',max_lengh=100)
    #text=forms.CharField(label='제목',widget=forms.Textarea)