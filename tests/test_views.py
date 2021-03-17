
from django.test import TestCase
import json
from markets.models import Market

class ErrorHandlerTests(TestCase):

    def test_404(self):
        response = self.client.get('/not_exists/')
        self.assertEqual(response.status_code,404)
        self.assertEqual(json.loads(response.content),{"message" : "Not Found"})

class ListViewTests(TestCase):

    def test_view_empty_market_lists(self):
        response = self.client.get('/markets/?district=A')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)),0)

    def test_view_market_lists_without_filters(self):
        response = self.client.get('/markets/')
        self.assertEqual(response.status_code, 400)

    def test_view_market_lists_district_filter(self):
        Market.objects.create(id=1, registration_code='A',district="A",region_5="Leste",name="A",address_city="CITY_2")
        Market.objects.create(id=2, registration_code='B',district="A",region_5="Oeste",name="B",address_city="CITY_1")
        Market.objects.create(id=3, registration_code='C',district="B",region_5="Leste",name="C",address_city="CITY_1")
        response = self.client.get('/markets?district=A',follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)),2)

    def test_view_market_lists_name_filter(self):
        Market.objects.create(id=1, registration_code='A',district="A",region_5="Leste",name="A",address_city="CITY_2")
        Market.objects.create(id=2, registration_code='B',district="A",region_5="Oeste",name="B",address_city="CITY_1")
        Market.objects.create(id=3, registration_code='C',district="B",region_5="Leste",name="C",address_city="CITY_1")
        response = self.client.get('/markets?name=A',follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)),1)

    def test_view_market_lists_name_not_found_filter(self):
        Market.objects.create(id=1, registration_code='A',district="A",region_5="Leste",name="A",address_city="CITY_2")
        Market.objects.create(id=2, registration_code='B',district="A",region_5="Oeste",name="B",address_city="CITY_1")
        Market.objects.create(id=3, registration_code='C',district="B",region_5="Leste",name="C",address_city="CITY_1")
        response = self.client.get('/markets?name=D',follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)),0)

    def test_view_market_lists_complex_filter(self):
        Market.objects.create(id=1, registration_code='A',district="A",region_5="Leste",name="A",address_city="CITY_2")
        Market.objects.create(id=2, registration_code='B',district="A",region_5="Oeste",name="B",address_city="CITY_1")
        Market.objects.create(id=3, registration_code='C',district="B",region_5="Leste",name="C",address_city="CITY_1")
        response = self.client.get('/markets?region_5=Leste&name=A',follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)),1)

class CreateViewTests(TestCase):

    def test_create_market(self):
        response = self.client.post('/markets/',{'id' : '1','registration_code' : 'A'})
        self.assertEqual(response.status_code, 201)

    def test_create_duplicate_market(self):
        Market.objects.create(id=1, registration_code='A',district="A",region_5="Leste",name="A",address_city="CITY_2")
        response = self.client.post('/markets/',{'id' : '1','registration_code' : 'A'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content)['registration_code'], ['market with this registration code already exists.'])

class UpdateViewTests(TestCase):

    def test_update_market(self):
        Market.objects.create(id=1, registration_code='A')
        response = self.client.put('/markets/A',{'id' : '1','district' : "A"},content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_non_existing_market(self):
        response = self.client.put('/markets/B',{'id' : '1','district' : "B"})
        self.assertEqual(response.status_code, 404)


class PatchViewTests(TestCase):

    def test_patch_market(self):
        Market.objects.create(id=1, registration_code='A')
        response = self.client.patch('/markets/A',{'district' : "A"},content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_patch_non_existing_market(self):
        response = self.client.patch('/markets/B',{'id' : '1','district' : "B"})
        self.assertEqual(response.status_code, 404)

class DeleteViewTests(TestCase):

    def test_delete_market(self):
        Market.objects.create(id=1, registration_code='A')
        response = self.client.delete('/markets/A')
        self.assertEqual(response.status_code, 204)

    def test_delete_non_existing_market(self):
        response = self.client.delete('/markets/B')
        self.assertEqual(response.status_code, 404)

class GetViewTests(TestCase):

    def test_get_market(self):
        Market.objects.create(id=1, registration_code='A')
        response = self.client.get('/markets/A')
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_market(self):
        response = self.client.get('/markets/B')
        self.assertEqual(response.status_code, 404)


