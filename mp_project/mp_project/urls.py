
from django.contrib import admin
from django.urls import path, include
# from logapp.views import index
from auapp.views import user_signup, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("logapp.urls")),
    path("auth/", include("auapp.urls")),
]
