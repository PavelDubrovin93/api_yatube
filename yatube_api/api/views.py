from rest_framework import viewsets
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import OwnerOrAuthReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrAuthReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    permission_classes = (OwnerOrAuthReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=Post.objects.get(id=self.kwargs.get("post_id"))
                        )
