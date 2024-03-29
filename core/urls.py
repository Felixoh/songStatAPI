"""SpotAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from argparse import Namespace
from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from spotAPI.admin import musicApp

urlpatterns = [

    # admin urls
    path('admin/', admin.site.urls),
    path('musicapAdmin/',musicApp.urls),

    # documentation for the System as stated above.
    path('docs/', TemplateView.as_view(template_name='documentation.html',extra_context={'schema_url':'api_schema'}
    ), name='swagger-ui'),
    path('api_schema/',get_schema_view(title="Music stats API",description="api documentation"),name="api_schema"),

    #authentication endpoints with JWT authentication system:
    path('api/users/',include('users.urls',namespace='users')),

    # apps endpoints with their necessary endpoints identified below.
    path('api/',include('spotAPI.urls')),
    path('api/subs/',include('Subs.urls')),

    # authentication URLS as stated below in the project explanation as seen  below , 
    path('api-auth/',include('rest_framework.urls')),

]
