from django.shortcuts import render

from cron_test_app.models import People


def home(request):
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        if person_name == '':
            person_name = "default"
        person_age = request.POST.get('person_age')
        if person_age == '':
            person_age = int(100)
        new_person = People(name=person_name, age=person_age)
        new_person.save()

    people = People.objects.all().order_by('-id')

    return render(request, 'index.html', {'people': people})
