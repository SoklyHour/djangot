from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view for the root URL
def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', home),  # This is for the root URL
]
