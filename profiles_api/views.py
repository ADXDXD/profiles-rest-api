# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditonal Django View',
            'Give good control over logic',
            'mapped manually to URL'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
