"""
URL configuration for foodwaste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request,'404.html',status=404)
def custom_500_view(request):
    return render(request,'500.html',status=500)
def custom_403_view(request, exception):
    return render(request,'403.html',status=404)
def custom_400_view(request, exception):
    return render(request,'400.html',status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('donate.urls'))
]

handler404=custom_404_view
handler500=custom_500_view
handler403=custom_403_view
handler400=custom_400_view