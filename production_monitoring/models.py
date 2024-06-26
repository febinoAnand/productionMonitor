from django.db import models
from datetime import datetime

class ProductionCount(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    production = models.IntegerField()

    def __str__(self):
        return f"Production Count: {self.production} on {self.date} at {self.time}"


class MissingDetails(models.Model):
    production_count = models.ForeignKey(ProductionCount, on_delete=models.CASCADE)
    description = models.TextField()
    missing_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"Missing Details for Production Count: {self.production_count.production} on {self.missing_date}"
