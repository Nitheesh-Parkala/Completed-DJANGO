import os 
import django

# Run administrative tasks
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakerProject.settings')
django.setup()

from faker import Faker
from myApp.models import Student

f = Faker()

def generate_data(n):
    for i in range(n):  # n specifies the number of records
        fname = f.name()
        froll = f.random_int(min=1, max=100)
        fmarks = f.random_int(min=1, max=100)
        fdob = f.date_of_birth()
        femail = f.email()  # Call the method to get the email
        # Create or get the Student object
        Student.objects.get_or_create(name=fname, roll=froll, marks=fmarks, dob=fdob, email=femail)

generate_data(10)

