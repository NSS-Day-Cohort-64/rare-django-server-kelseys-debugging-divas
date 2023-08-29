from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rareapi.models import Post



class PostView(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        posts = Post.objects.all()

        user = request.query_params.get("author_id", None)
        if user == str(request.auth.user.id):# Check if user ID matches authenticated user's ID
            posts = posts.filter(author=request.auth.user)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    





class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'title', 'publication_date',
                'image_url', 'content', 'approved', 'reactions', 'tags')