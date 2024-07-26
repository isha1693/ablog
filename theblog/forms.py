from django import forms
from .models import Post  ,Category ,Comment

choices = Category.objects.all().values_list('name', 'name') 
choice_list =[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author','category','body', 'header_image')

        widgets= {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is a Title placeholder'}),
            'author' : forms.Select( attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets= {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is a Title placeholder'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']