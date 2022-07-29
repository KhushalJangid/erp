from django.test import TestCase
from models import ClassesCollection
# Create your tests here.

obj = ClassesCollection("12_a")
print(obj.get())
