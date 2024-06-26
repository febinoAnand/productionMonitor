
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductionCountListCreateView, MissingDetailsViewSet

router = DefaultRouter()
router.register('missing_details', MissingDetailsViewSet, basename='missing-details')

urlpatterns = [
    path('production_counts/', ProductionCountListCreateView.as_view(), name='production-count-list-create'),
    path('', include(router.urls)),
]
