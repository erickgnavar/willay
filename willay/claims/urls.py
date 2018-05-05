from django.urls import path

from . import views


app_name = 'claims'

urlpatterns = [
    path('claims/', views.ClaimListView.as_view(), name='claim-list'),
    path('claims/create/', views.ClaimCreateView.as_view(), name='claim-create'),
    path('claims/<int:id>/', views.ClaimDetailView.as_view(), name='claim-detail'),
]
