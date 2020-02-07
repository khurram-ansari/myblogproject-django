from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # declare the fields you will show
    username = forms.CharField(label="Your Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    # first password field
    password1 = forms.CharField(label="Your Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # confirm password field
    password2 = forms.CharField(label="Repeat Your Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = "Email Address",widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label = "Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Surname",widget=forms.TextInput(attrs={'class':'form-control'}))
    
    
    # this sets the order of the fields
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2", )
 
    # this redefines the save function to include the fields you added
    def save(self, commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit: 
            user.save()

        return user
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords not matching")
        return password2