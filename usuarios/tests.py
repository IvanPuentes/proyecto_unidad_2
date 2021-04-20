from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.

class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_mangas_page_status_code(self):
        response = self.client.get('mangas')
        self.assertEqual(response.status_code,200)
    def test_Autores_page_status_code(self):
        response = self.client.get('Autor')
        self.assertEqual(response.status_code,200)
    def test_descrip_page_status_code(self):
        response = self.client.get('descrip')
        self.assertEqual(response.status_code,200)
    