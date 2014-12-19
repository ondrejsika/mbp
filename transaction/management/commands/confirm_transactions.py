# django
from django.core.management.base import BaseCommand

# project
from transaction.models import Transaction


class Command(BaseCommand):
    help = u'Process transaction from blockchain.info API'

    def handle(self, *args, **options):
        Transaction.confirm_transactions()

