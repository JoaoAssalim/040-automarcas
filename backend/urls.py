from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), 
    path('signup/', SignInView.as_view(), name='signup'), 
    path('services-list/', ServicesList.as_view(), name='services-list'), 
    path('services-create/', ServicesCreate.as_view(), name='services-create'), 
    path('pecas-create/', PecasCreate.as_view(), name='pecas-create'),
    path('pecas-list/', PecasList.as_view(), name='pecas-list'),
]