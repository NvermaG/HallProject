from django.shortcuts import render
from hall.serializers import hallserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import hall

# Create your views here.
class hallapi(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = hall.objects.all()
    model = hall
    serializer_class = hallserializer

    http_method_names = ["get", "post", "put", "delete"]


    def list(self, request):
        if request.method == 'GET':
            obj = hall.objects.all()
            serializer = self.get_serializer(obj,many=True)
            # for i in serializer.data:
                # for j in i:
                    # print(j,i[j])

            return Response(serializer.data)

    def create(self,request):
        if request.method == 'POST':
            serializer = hallserializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)

    def update(self,request,*args, **kwargs):
        if request.method == 'PUT':
            instance = self.get_object()
            data = request.data
            serializer = hallserializer(instance,data=data, partial=True)
            serializer.is_valid()
            print(serializer.validated_data['hallName'])

            serializer.save()
            return Response("Object updated")
