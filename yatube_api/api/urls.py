from rest_framework.authtoken import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(
    'posts',
    PostViewSet
)
router.register(
    'groups',
    GroupViewSet
)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
