from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Заголовок поста', 'text': 'Текст поста'}
        widgets = {'title': forms.TextInput(),
                   'text': forms.Textarea(attrs={'cols':80})}