from ast import Delete
from rest_framework import viewsets


from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from .models import Car, Employer
from .serializers import CarSerializier, EmployerSerializier

class MyApiView(APIView):
    
    def get(self, request):
        data = {"message": "Hello, World!"}
        print("Это Get запрос: ", data)
        return Response(data=data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        print("Это Post запрос: ", data)
        return Response(data=data, status=status.HTTP_201_CREATED)


class MyGenericEmplyerAPIViews(GenericAPIView, CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializier

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 
