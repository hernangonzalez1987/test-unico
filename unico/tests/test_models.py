
from django.test import TestCase
import json
from markets.models import Market
from django.db import IntegrityError

class MarketModelTest(TestCase):

    def test_unique_registration_code(self):
        Market.objects.create(id=1, registration_code='A')
        with self.assertRaisesMessage(IntegrityError,"already exists"):
            Market.objects.create(id=1, registration_code='B')

    def test_unique_registration_code_by_registration_code(self):
        Market.objects.create(id=1, registration_code='A')
        with self.assertRaisesMessage(IntegrityError,"already exists"):
            Market.objects.create(id=2, registration_code='A')