import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docIncDb.settings')

import django
django.setup()

from docIncApp.models import Person

def create_people():
    new_person = Person.objects.create(
        personname = "Gary Smith",
        birthday = 12122008,
        lastfoursocial = 1111
    )
    new_person2 = Person.objects.create(
        personname = "John Smith",
        birthday = 12122008,
        lastfoursocial = 1112
    )

    print(f"Created ID: {new_person.id}")
    print(f"Created ID: {new_person2.id}")

def read_people():
    try:
        Person.objects.get(personname = "Gary Smith")
    except Person.DoesNotExist:
        print("Person with name Gary Smith was not found")
    
    people = Person.objects.all()
    for person in people:
        print(person)

def update_people():
    people_named_Gary = Person.objects.filter(personname__icontains="Gary")
    people_named_Gary.update(birthday = 12121998)

def delete_person():
    person = Person.objects.get(personname = "John Smith")
    person.delete()

    try:
        Person.objects.get(personname = "John Smith")
    except Person.DoesNotExist:
        print("Person with name John Smith was deleted")

def clear_table():
    Person.objects.all().delete()

if __name__ == '__main__':
    print("Clearing table.")
    clear_table()
    input("Press enter to continue.\n>")

    print("Creating 2 entries.")
    create_people()
    input("Press enter to continue.\n>")

    print("Reading entries.")
    read_people()
    input("Press enter to continue.\n>")

    print("Updating 1 entry.")
    update_people()
    input("Press enter to continue.\n>")

    print("Deleting 1 entry.")
    delete_person()
