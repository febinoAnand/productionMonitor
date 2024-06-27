
from celery import shared_task
import random
from .models import ProductionCount 
from datetime import datetime, timedelta 

@shared_task
def generate_random_production_count(args):
    from .models import ProductionCount
    production_count = random.randint(1, 50)
    ProductionCount.objects.create(production=production_count)
    print("Successfully Created!!")


@shared_task
def delete_old_data(args):
    from .models import ProductionCount
    ten_days_ago = datetime.now() - timedelta(days=10)
    ProductionCount.objects.filter(date__lt=ten_days_ago.date()).delete()
    print("Successfully Deleted Old Data!!")