from django.urls import path, include
from rest_framework_nested import routers

from . import views


def get_nested_posts_router(parent_router, parent_name=''):
    """
    Given a parent router and its routing key, this will return a nested
    router that will allow posts to be nested under the parent descriptive URLs
    """
    posts_router = routers.NestedDefaultRouter(parent_router, parent_name, lookup='user')
    posts_router.register('posts', views.PostViewSet, base_name='user-posts')
    return posts_router


router = routers.SimpleRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    path('feed', views.FeedView.as_view()),
    path('', include(router.urls)),
]