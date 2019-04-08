from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','text','author',]

#class PostForm(forms.Form):
    #title=forms.charField(label='제목',max_length=100)
    #text=forms.charField(label='제목',widget=form.Textarea)
    