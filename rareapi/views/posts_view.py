from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rareapi.models import Post, Category, Author, PostTag, Reaction
from rest_framework.authtoken.models import Token
from django.utils import timezone


class PostView(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        now = timezone.now()
        
        posts = Post.objects.filter(
            approved=True,
            publication_date__lte=now
        ).order_by('-publication_date')

        token = request.query_params.get("token", None)
        if token:
            user = Token.objects.get(key=token).user
            posts = posts.filter(author=user).order_by('-publication_date')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        author_id = request.data['author']  # Assuming you're sending the author ID in the request data
        author = User.objects.get(id=author_id)

        category = Category.objects.get(pk=request.data['category'])

        post = Post.objects.create(
            author=author,
            category=category,
            title=request.data['title'],
            publication_date=request.data['publication_date'],
            image_url=request.data['image_url'],
            content=request.data['content'],
            approved=request.data['approved'],
        )

        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'label')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class PostSerializer(serializers.ModelSerializer):
    category = PostCategorySerializer(many=False)
    author = UserSerializer(many=False)

    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'title', 'publication_date',
                  'image_url', 'content', 'approved', 'reactions', 'tags')
