from django.db import transaction

from cron_test_app.models import People


def remove_people():
    all_people = People.objects.all()

    try:
        with transaction.atomic():
            for people in all_people:
                people.delete()
    except Exception as ex:
        print ex
