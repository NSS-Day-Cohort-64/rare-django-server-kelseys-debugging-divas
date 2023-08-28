from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post



class PostView(ViewSet):

    def list(self, request):
        posts = posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    





class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'title', 'publication_date',
                'image_url', 'content', 'approved', 'reactions', 'tags')