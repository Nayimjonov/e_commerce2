from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Categories
from .serializers import CategoryModelSerializer


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    