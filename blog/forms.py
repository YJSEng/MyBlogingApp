from django import forms
class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={'class': 'form-group', 'placeholder': 'Enter your name'}
        )
    )
    to = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-group', 'placeholder': 'Enter recipient email'}
        )
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-group',
                'rows': 4,  # Adjust the number of rows for the textarea
                'placeholder': 'Enter your comments here...'
            }
        )
    )
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
            ),
            'email': forms.EmailInput(
                attrs={
                  
                    'placeholder': 'Enter your email here...',  # Add a placeholder
                    'class': 'form-group',  # Add CSS class for styling
                }
            ),
            'name': forms.TextInput(
                attrs={
                  
                    'placeholder': 'Enter your name here...',  # Add a placeholder
                    'class': 'form-group',  # Add CSS class for styling
                }
            )
        }



class SubmitForm(forms.ModelForm):
  # class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image','author','email']  # Specify the fields you want in the form
        
        # Define widgets for customizing the form fields
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'rows': 4,  # Set the number of rows (height)
                    'cols': 40,  # Set the number of columns (width)
                    'placeholder': 'Enter your comment here...',  # Add a placeholder
                    'class': 'form-group',  # Add CSS class for styling
                }
            ),
            'email': forms.EmailInput(
                attrs={
                  
                    'placeholder': 'Enter your email here...',  # Add a placeholder
                    'class': 'form-group',  # Add CSS class for styling
                }
            ),
            'title': forms.TextInput(
                attrs={
                  
                    'placeholder': 'Enter your title here...',  # Add a placeholder
                    'class': 'form-group',  # Add CSS class for styling
                }
            ),
            'author': forms.TextInput(
                attrs={
                  
                    'placeholder': 'Enter your name here...',  # Add a placeholder
                    'class': 'form-group',  # Add CSS class for styling
                }
            ),
            'body': forms.Textarea(
                attrs={
                     'rows':9,
                     'cols':110,
                    'placeholder': 'Enter your body here...',  # Add a placeholder
                    'class': 'form-group',  # Add CSS class for styling
                }
            )
        }