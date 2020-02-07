from . import models
from django import forms

class CreateBlog(forms.ModelForm):
    class Meta:
        model=models.Blog           
        fields=['title','content','slug','category','img']