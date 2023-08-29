
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from rareapi.views import register_user, login_user, PostView
from rest_framework import routers

# Create a router instance
router = routers.DefaultRouter(trailing_slash=False)

# Register the PostView with the router
router.register(r'posts', PostView, 'post')

# Define the urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls)),  # Include the router's URLs
]
