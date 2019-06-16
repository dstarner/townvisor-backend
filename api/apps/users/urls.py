from django.urls import path, include
from rest_framework_nested import routers

from api.apps.posts.urls import get_nested_posts_router

from . import views

router = routers.SimpleRouter()
router.register('', views.UserViewSet)

posts_router = get_nested_posts_router(router)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]