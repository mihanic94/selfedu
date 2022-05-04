from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass  # Здесь мы прописываем какие-то команды. Чтобы их запустить, пишем в терминале python manage.py <имя_файла>
              # Например, у нас это будет запускаться через: python manage.py run
