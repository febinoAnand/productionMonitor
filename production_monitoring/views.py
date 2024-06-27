from rest_framework import generics
from .models import ProductionCount,Machine
from .serializers import *
from rest_framework import viewsets



class ProductionCountListCreateView(viewsets.ModelViewSet):
    queryset = ProductionCount.objects.all()
    serializer_class = ProductionCountSerializer
    http_method_names = ["get"]

# class MissingDetailsViewSet(viewsets.ModelViewSet):
#     queryset = MissingDetails.objects.all()
#     serializer_class = MissingDetailsSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
