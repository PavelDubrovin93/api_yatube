from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):

    group = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Group.objects.all(),
                                         required=False)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'post', 'created')
        model = Comment
        read_only_fields = ('author', 'post')
