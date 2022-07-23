from django.test import TestCase
from models import Collection
# Create your tests here.

table = Collection("478")
print(table.get({"date":""}))