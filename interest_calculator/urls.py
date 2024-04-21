"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('calculator.urls')),   # This is to include the apps urls in this
]
"""

# urls.py
from django.contrib import admin
from django.urls import path,include
from calculator.views import index, delete_calculation  # Import the delete_calculation view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('calculator.urls')),
    path('', index, name='index'),
    path('delete/<int:calculation_id>/', delete_calculation, name='delete_calculation'),  # Define the URL pattern for delete_calculation
]
