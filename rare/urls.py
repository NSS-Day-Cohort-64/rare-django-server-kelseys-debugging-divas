from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
from rareapi.views import register_user
from django.conf.urls import include
from rest_framework import routers

from rest_framework import routers
from rareapi.views import login_user

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('register', register_user)
    path('', include(router.urls))
]
