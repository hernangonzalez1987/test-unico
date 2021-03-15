from django.test import TestCase

class TestCalls(TestCase):
    def test_list_all(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code,200)
