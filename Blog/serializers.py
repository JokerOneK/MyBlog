from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    posts = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['theme', 'post_text', 'pub_date', 'author', 'posts']