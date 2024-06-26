from rest_framework import serializers
from .models import ProductionCount,Machine



# class MissingDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MissingDetails
#         fields = ['id', 'production_count', 'description', 'missing_date']

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ["machineID","name","manufacture","model","line"]

class ProductionCountSerializer(serializers.ModelSerializer):
    machine = MachineSerializer()
    class Meta:
        model = ProductionCount
        fields = ['id', 'date', 'time', 'production','machine']