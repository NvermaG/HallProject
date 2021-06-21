from django.urls import path,include
from . import views
from django.conf.urls import url
from django.urls import path, include
from .views import RegisterApi
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('api/register',views.RegisterApi.as_view({'post':'register'})),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
