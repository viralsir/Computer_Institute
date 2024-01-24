from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models.functions import TruncMonth
from django.http.response import JsonResponse

# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        print("method post")
        if form.is_valid():
            form.save()
            print("data is saved")
            username=form.cleaned_data["username"]
            messages.success(request,f"account is created for {username} you can now login ")
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,"users/register.html",{
        "form":form
    })


#@login_required(login_url='login')
# def profile(request):
#     if request.method == 'POST' :
#         u_form = UserUpdateForm(request.POST,instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f" profile is updated  ")
#             return redirect('profile')
#         else:
#             return render(request, "users/profile.html", {
#                 "u_form": u_form,
#                 "p_form": p_form
#             })
#
#     u_form=UserUpdateForm(instance=request.user)
#     p_form=ProfileUpdateForm(instance=request.user.profile)
#     return render(request, "users/profile.html", {
#         "u_form":u_form,
#         "p_form":p_form
#     })

