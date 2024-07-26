from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm , UserChangeForm ,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class PasswordsChangeview(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    #success_url = reverse_lazy('home')

def password_success(request):
    return render(request, 'registration/password_success.html', {} )

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
   
    def get_object(self):
        return self.request.user
