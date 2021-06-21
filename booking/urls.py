from django.urls import path
from . import views


urlpatterns = [
    path('list/hall',views.BookingView.as_view({'get':'list'})),
    path('range_list/hall',views.RangeView.as_view({'post':'listrange'})),
    path('create/hall',views.BookingView.as_view({'post':'create'})),
    path('<int:pk>/update/hall',views.BookingView.as_view({'put':'update'})),
    path('<int:pk>/delete/hall',views.BookingView.as_view({'delete':'destroy'})),
]
