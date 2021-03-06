import sys
from django.core.management.base import BaseCommand
from django.conf import settings
from dimagi.utils.couch.database import get_db
from logistics_project.apps.ewsghana import loader

class Command(BaseCommand):
    help = "Set ProductStock.use_auto_consumption to be True, and update all auto_monthly_consumptions"

    def handle(self, *args, **options):
        from logistics.models import ProductStock
        stocks = ProductStock.objects.all()
        for stock in stocks:
            stock.use_auto_consumption = True
            stock.update_auto_consumption()
            stock.save()
   
