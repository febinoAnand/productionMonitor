from rest_framework import generics
from .models import ProductionCount,MissingDetails
from .serializers import ProductionCountSerializer,MissingDetailsSerializer
from rest_framework import viewsets



class ProductionCountListCreateView(generics.ListCreateAPIView):
    queryset = ProductionCount.objects.all()
    serializer_class = ProductionCountSerializer

class MissingDetailsViewSet(viewsets.ModelViewSet):
    queryset = MissingDetails.objects.all()
    serializer_class = MissingDetailsSerializer
