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

def get_nested_comments_router(parent_router, parent_name='', lookup='post'):
    """
    Given a parent router and its routing key, this will return a nested
    router that will allow comments to be nested under the parent descriptive URLs
    """
    comments_router = routers.NestedDefaultRouter(parent_router, parent_prefix=parent_name, lookup=lookup)
    comments_router.register('comments', views.CommentViewSet, base_name=f'{lookup}-comments')
    return comments_router


router = routers.SimpleRouter()
router.register('comments', views.CommentViewSet)
router.register('', views.PostViewSet)

comments_router = get_nested_comments_router(router)


urlpatterns = [
    path('feed/', views.FeedView.as_view()),
    path('', include(router.urls)),
    path('', include(comments_router.urls)),
]