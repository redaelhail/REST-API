from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View."""

    serializer_class = serializers.HelloSerializer

    def post(self,request):
        "Create a hello message with my name"

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


    def get(self, request,format=None):
        """returns a list of API view features"""
        an_apiview=[
        "Uses HTTP methods as function: get,post,patch,put,delete",
        "Is similar to a traditional django view",
        "Gives you the most control of your application logic",
        "Is mapped manually to urls"
        ]
        return Response({'message':'Hello Reda', 'an_apiview':an_apiview})

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class
