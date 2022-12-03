from django.test import TestCase, Client
from django.urls import reverse
from mainsite.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home_page')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 302)