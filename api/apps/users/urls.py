from django.urls import path, include
from rest_framework_nested import routers

from api.apps.posts.urls import get_nested_posts_router, get_nested_comments_router

from . import views

router = routers.SimpleRouter()
router.register('', views.UserViewSet)

posts_router = get_nested_posts_router(router)
comments_router = get_nested_comments_router(router, parent_name='', lookup='user')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
    path('', include(comments_router.urls)),
]