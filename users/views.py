from django.shortcuts import render,redirect
from .models import CustomUser
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserForm,ProfileUpdateForm
from django.contrib import messages
# Create your views here.

class RegisterView(View):
    def get(self, request):
        create_form = CustomUserForm()
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        create_form = CustomUserForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, 'Registration successful!')             
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            messages.error(request,'Something is wrong! \nTry again')
            return render(request, 'register.html', context=context)


# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'register.html')
#
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
#         last_name = request.POST['last_name']
#         first_name = request.POST['first_name']
#
#         user = CustomUser.objects.create_user(
#             username=username,
#             email=email,
#             first_name=first_name,
#             last_name=last_name
#         )
#         user.set_password(password)
#         user.save()
#
#         return redirect('users:login')


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'form': login_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in') 
            return redirect('home:landing_page')
        else:
            context = {
                'form': login_form
            }
            return render(request, 'login.html', context=context)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('home:landing_page')

class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'profile.html',{"user": request.user})
    
class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        update_form = ProfileUpdateForm(instance=request.user)
        context = {
            'form': update_form
        }
        return render(request, 'update_profile.html', context=context)
    
    def post(self, request):
        update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('users:profile')
        else:
            context = {
                'form': update_form
            }
            return render(request, 'update_profile.html', context=context)