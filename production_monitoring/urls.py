
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductionCountListCreateView, MachineViewSet

router = DefaultRouter()
router.register('machine', MachineViewSet, basename='machine-details')
router.register('production',ProductionCountListCreateView)

urlpatterns = [
    # path('production_counts/', ProductionCountListCreateView.as_view(), name='production-count-list-create'),
    path('', include(router.urls)),
]
