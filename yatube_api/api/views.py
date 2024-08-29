from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404

from posts.models import Post, Group
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import OwnerOrAuthReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrAuthReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrAuthReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        )
