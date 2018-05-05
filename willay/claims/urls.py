from django.urls import path

from . import views


app_name = 'claims'

urlpatterns = [
    path('map/', views.MapView.as_view(), name='claim-map'),
    path('map/data/', views.MapDataView.as_view(), name='claim-map-data'),
    path('claims/', views.ClaimListView.as_view(), name='claim-list'),
    path('claims/create/', views.ClaimCreateView.as_view(), name='claim-create'),
    path('claims/<int:id>/', views.ClaimDetailView.as_view(), name='claim-detail'),
]
