from rest_framework import serializers
from .models import ProductionCount,MissingDetails

class ProductionCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCount
        fields = ['id', 'date', 'time', 'production']

class MissingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingDetails
        fields = ['id', 'production_count', 'description', 'missing_date']
