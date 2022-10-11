"""crypto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from crypto.views.CryptoView import CryptoView
from crypto.views.HelloWorld import hello, get_asset_price
from crypto.views.AlertView import AlertView, get_all_al, send_email_with_password


urlpatterns = [
    path('api/cryptocurrency/value/', CryptoView.as_view()),
    path('api/alert/', AlertView.as_view()),
    path('', hello),
    path('api/alert/get_all', get_all_al),
    path('asset/', get_asset_price),
    path('send_password/', send_email_with_password)
]
