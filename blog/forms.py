from django import forms
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
from .models import Comment,Post
class MyModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image']
class CommentForm(forms.ModelForm):
  # class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']  # Specify the fields you want in the form
        
        # Define widgets for customizing the form fields
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'rows': 4,  # Set the number of rows (height)
                    'cols': 40,  # Set the number of columns (width)
                    'placeholder': 'Enter your comment here...',  # Add a placeholder
                    'class': 'form-group',  # Add CSS class for styling
                }
            )
        }