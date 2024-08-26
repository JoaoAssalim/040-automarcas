from django.shortcuts import render, redirect
from django.views import View

class SignInView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)