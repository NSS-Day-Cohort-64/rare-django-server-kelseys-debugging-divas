
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import login_user, TokenView, register_user, UserView, TagView, CategoryView, PostView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tags', TagView, 'tag')
router.register(r'categories', CategoryView, 'category')
# Register the PostView with the router
router.register(r'posts', PostView, 'post')
router.register(r'users', UserView, 'user')
router.register(r'tokens', TokenView, 'token')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls)),  # Include the router's URLs
]
