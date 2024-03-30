#
# DJango esperando a que la base de datos este disponible
#
import time
from typing import Any
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
 
class Command(BaseCommand):
 
    def handle(self, *args: Any, **options: Any):
        self.stdout.write('Esperando por la base de datos..')
        db_up = False
        
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Base de datos aun no disponible, esperando 1 segundo')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Base de datos disponible'))