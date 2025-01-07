import sys
import os
from django.db import transaction

# Add the parent directory (project/) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_project.settings.settings_local')

import django
django.setup()



from weather.models import County

counties = []
with open("C:/Users/adamk/Desktop/programovani/projects/weather/scripts/counties.txt", 'r', encoding="utf-8") as file:
    for line in file:
        title, latitude, longitude = line.strip().rstrip(",").split(",")
        counties.append(County(title=title, latitude=latitude, longitude=longitude))

with transaction.atomic():
    County.objects.all().delete()
    County.objects.bulk_create(counties)

print("counties created")
