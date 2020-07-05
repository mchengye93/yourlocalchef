"""yourlocalchef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
import foods.views
import foods.api_views

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('api/v1/users/', foods.api_views.UserList.as_view()),
    path('api/v1/users/new', foods.api_views.UserCreate.as_view()),
    path('api/v1/fooditems/', foods.api_views.FoodItemList.as_view()),
    path('api/v1/fooditems/new', foods.api_views.FoodItemCreate.as_view()),
    path('api/v1/fooditems/<int:id>/', foods.api_views.FoodItemRetrieveUpdateDestroy.as_view()),
    path('admin/', admin.site.urls),
    path('foods', foods.views.homepage, name='homepage'),
]

 
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
