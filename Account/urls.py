"""
URL configuration for PollApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.manage_account, name="account"),
    path('signout',views.sign_out, name="signout"),
    path('signin',views.sign_in, name="signin"),
    path('signup',views.sign_up, name="signup"),
    path('account-deletion',views.delete_account, name="delacc"),
    path('change-Icon',views.change_icon, name="changeIcon"),
]
