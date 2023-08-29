from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import login_user, register_user, TagView, CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tags', TagView, 'tag')
router.register(r'categories', CategoryView, 'tag')

urlpatterns = [
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('', include(router.urls))
]
