from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns_api  = [
    
]

urlpatterns_panel_admin_redirect = [
    path('api/', RedirectView.as_view(url='/api/swagger/', permanent=False)),
]

schema_view = get_schema_view(
    openapi.Info(
        title="040 Automarcas API",
        default_version='v1',
        description="Descrição da API",
        contact=openapi.Contact(email=''),
        license=openapi.License(name="BSD License"),
    ),
    patterns=urlpatterns_api,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
        path('', include('backend.urls')),

        path('admin/', admin.site.urls)] + \
             urlpatterns_api + \
        [ 
            re_path(r'api/swagger/$', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
            re_path(r'system-status-v0qw/', include('health_check.urls'))
        ] + \
            urlpatterns_panel_admin_redirect