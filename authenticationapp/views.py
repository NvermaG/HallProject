from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet


# Create your views here.



class RegisterApi(ModelViewSet):
    serializer_class = RegisterSerializer
    http_method_names = ["get", "post", "put", "delete","patch"]

    def register(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
