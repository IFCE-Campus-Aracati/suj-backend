from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["text", "author", "posted_on"]
