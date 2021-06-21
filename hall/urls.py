from django.urls import path
from . import views


urlpatterns = [
    path('list/hall',views.hallapi.as_view({'get':'list'})),
    path('create/hall',views.hallapi.as_view({'post':'create'})),
    path('<int:pk>/update/hall',views.hallapi.as_view({'put':'update'})),
    path('<int:pk>/delete/hall',views.hallapi.as_view({'delete':'destroy'})),
]
