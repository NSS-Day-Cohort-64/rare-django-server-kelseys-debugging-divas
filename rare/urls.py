from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rareapi.views import login_user

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
