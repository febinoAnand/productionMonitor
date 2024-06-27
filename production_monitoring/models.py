from django.db import models
import uuid
from datetime import datetime



# class MissingDetails(models.Model):
#     production_count = models.ForeignKey(ProductionCount, on_delete=models.CASCADE)
#     description = models.TextField()
#     missing_date = models.DateField(default=datetime.now)

#     def __str__(self):
#         return f"Missing Details for Production Count: {self.production_count.production} on {self.missing_date}"

class Machine(models.Model):
    machineID = models.UUIDField(max_length=15,unique=True, blank=False, default=uuid.uuid1)
    name = models.CharField(max_length=50,blank=False)
    manufacture = models.CharField(max_length=50)
    model = models.CharField(max_length=10)
    line = models.CharField(max_length=10)
    def __str__(self):
        return (self.name + " - " + str(self.machineID))
    
class ProductionCount(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    production = models.IntegerField()
    machine = models.ForeignKey(Machine,on_delete=models.CASCADE)
    def __str__(self):
        return f"Production Count: {self.production} on {self.date} at {self.time}"
    