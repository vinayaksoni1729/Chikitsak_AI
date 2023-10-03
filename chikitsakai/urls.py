from chikitsak import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.new, name="home"),
    path("outputnew",views.outputnew,name="outputnew")
]
