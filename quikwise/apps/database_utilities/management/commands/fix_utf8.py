from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fix utf8 column in mysql'

    def handle(self, *args, **options):
        from django.db import connection

        cursor = connection.cursor()
        tables = connection.introspection.table_names()

        for table in tables:
            sql = "ALTER TABLE `%s` CONVERT TO CHARACTER SET utf8mb4;" % (table)

            cursor.execute(sql)

        self.stdout.write(self.style.SUCCESS('Successfully converted all tables to utf8mb4'))
