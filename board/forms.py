from django.forms import ModelForm
from django import forms
from Login.models import Post, PostComment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title","thumbails","intro","body")
        labels = {
            'title':'',
            'thumbails': 'Load Image',
            'intro': '',
            'body': '',
        }
        widgets = {
            'body': SummernoteWidget(attrs={
                "width":"1000",

            }),
            'title':forms.TextInput(attrs={
                "class":"id-title border-0",
                "placeholder": "Enter a Post title"
            }),
            'intro': forms.Textarea(attrs={
                "rows": '3',
                "cols": '100',
                "class":"id-title border-0 fs-6",
                "placeholder": "Enter a short description of your post"
            }),
            'thumbails': forms.FileInput(attrs={
                "hidden":'',
            })
        }

class CommentForm(ModelForm):
    class Meta:
        model = PostComment
        fields = ("body",)
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                "rows": '3',
                "class":"border-0 fs-5 p-3 cmt",
                "placeholder": "Enter your comments"
            })
        }