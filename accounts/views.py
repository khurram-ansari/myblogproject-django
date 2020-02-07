from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm
from django.contrib.auth import login,logout
from blogapp.views import all_cat
# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
        else:
            return render(request,'signup.html',{"categories":all_cat,"frm":form})

    else:
        form=RegisterForm()
        return render(request,'signup.html',{"categories":all_cat,"frm":form})
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                #  getting value from input named next
                return redirect(request.POST.get('next'))  
            else:
                return redirect('blog:allblogs')
        else:
            return render(request,'login.html',{"categories":all_cat,"loginfrm":form})

    else :
        form=AuthenticationForm()
        return render(request,'login.html',{"categories":all_cat,'loginfrm':form})
    
def logout_view(request):
    logout(request)
    return redirect('blog:allblogs')


