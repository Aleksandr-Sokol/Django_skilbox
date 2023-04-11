from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """
    Create new admin user
    """

    def handle(self, *args, **options):
        admin_username = 'admin'
        admin_email = 'admin@mail.ru'
        admin_password = 'admin'
        if not len(User.objects.filter(username='root').all()):
            User.objects.create_superuser(admin_username, admin_email, admin_password)
            print(f'New admin user {admin_username} has been created')
