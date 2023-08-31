from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category
\


class CategoryView(ViewSet):
    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        categories = Category.objects.all().order_by('label')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests for creating a new category

        Returns:
            Response -- JSON serialized category record
        """

        new_category = Category()
        new_category.label = request.data["label"]
        new_category.save()

        serialized = CategorySerializer(new_category, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single category

        Returns:
            Response -- JSON serialized category record
        """

        category = Category.objects.get(pk=pk)
        serialized = CategorySerializer(category, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)
    


    def destroy(self, request, pk):
        """Handle DELETE requests for categories

        Returns:
            Response -- Empty body with 204 status code
        """
        

        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Category
        fields = ('id', 'label',)
