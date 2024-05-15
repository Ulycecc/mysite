from .models import Comment
from django import forms


class EmailPostForm(forms.Form):
    '''
    Форма для отсылки поста по почте
    '''
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    '''
    Форма для комментариев
    '''
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
