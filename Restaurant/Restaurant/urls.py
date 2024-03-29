
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name='home'),
    path("show_items/",include("meal.urls")),
    path("about/",include("about_us.urls")),
]
