from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegForm
from django.urls import reverse_lazy
from django.contrib.auth import login,logout

# Create your views here.
class UserReg(FormView):
    template_name='account/user_reg.html'
    form_class = UserRegForm
    success_url = reverse_lazy('/login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    