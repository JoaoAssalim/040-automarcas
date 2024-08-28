from django.shortcuts import render, redirect
from django.views import View
from backend.models import Service, Part

class SignInView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)
    
class ServicesList(View):
    template_name = 'services-list.html'

    def get(self, request):
        context = {
            "services": Service.objects.all()
        }
        print(context)
        return render(request, self.template_name, context=context)
    
class ServicesCreate(View):
    template_name = 'services-create.html'

    def get(self, request):
        return render(request, self.template_name)
    

class PecasCreate(View):
    template_name = 'pecas-create.html'

    def get(self, request):
        return render(request, self.template_name)
    
class PecasList(View):
    template_name = 'pecas-list.html'

    def get(self, request):
        context = {
            "parts": Part.objects.all()
        }
        return render(request, self.template_name, context=context)


    