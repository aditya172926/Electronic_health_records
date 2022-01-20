
from django.contrib import admin
from django.urls import path
from logapp.views import home
from auapp.views import user_signup, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home, name="home"),
    path("user_signup", user_signup, name="user_signup"),
    path("user_login", user_login, name="user_login"),
    path("user_logout", user_logout, name="user_logout"),

]
