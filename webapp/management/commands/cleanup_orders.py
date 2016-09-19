from django.core.management.base import BaseCommand, CommandError
from webapp.models import ordermodel

class Command(BaseCommand):
    help = 'Resets all orders to 0'

    def handle(self, *args, **options):
        print "RESETTING ORDERS!"
        ordermodel.objects.all().update(value = 0)