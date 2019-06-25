from .models import Profile,Image,Comments
from django import forms

# profile form
class getProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['infor']

# uploading a picture
class uploadPhoto(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']

# commentig form
class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        exclude =['user', 'picture']
