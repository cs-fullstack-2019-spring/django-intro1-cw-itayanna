


# importing the fils from the app for the server to read

from django.contrib import admin
from django.urls import include, path

#
# linking the paths from the appto the servers

urlpatterns = [
    path('', include('classworkApp1.urls')),
    path('admin/', admin.site.urls),
]
