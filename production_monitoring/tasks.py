
from celery import shared_task
import random
from .models import ProductionCount,Machine
from datetime import datetime, timedelta 

@shared_task
def generate_random_production_count(args):
    production_count = random.randint(1, 50)
    machineList = list(Machine.objects.all())
    machineRandom = random.choice(machineList)
    ProductionCount.objects.create(production=production_count,machine = machineRandom)
    print("Succesfully Created!!")

# @shared_task
# def delete_old_data():
#     ten_days_ago = datetime.now() - timedelta(days=10)
#     ProductionCount.objects.filter(date__lt=ten_days_ago.date()).delete()
#     print("Successfully Deleted Old Data!!")