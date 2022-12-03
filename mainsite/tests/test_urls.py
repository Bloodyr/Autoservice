from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mainsite.views import *


class TestUrls(SimpleTestCase):

    def test_home_is_resolver(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func, home_page)

    def test_registration_is_resolver(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func, register_page)

    def test_login_is_resolver(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_page)
    
    def test_logout_is_resolver(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_cars_is_resolver(self):
        url = reverse('cars_page')
        self.assertEquals(resolve(url).func, cars_page)
    
    def test_cars_details_is_resolver(self):
        url = reverse('cars_details_page')
        self.assertEquals(resolve(url).func, cars_details_page)
    
    def test_settings_is_resolver(self):
        url = reverse('settings_page')
        self.assertEquals(resolve(url).func, settings_page)

    def test_order_info_is_resolver(self):
        url = reverse('order_info_page')
        self.assertEquals(resolve(url).func, order_info_page)
    
    def test_order_detail_is_resolver(self):
        url = reverse('order_detail_page', args=[1])
        self.assertEquals(resolve(url).func, order_detail_page)

    def test_parts_list_is_resolver(self):
        url = reverse('part_list_page')
        self.assertEquals(resolve(url).func, part_list_page)
    
    def test_part_detail_is_resolver(self):
        url = reverse('part_detail_page', args=[1])
        self.assertEquals(resolve(url).func, part_detail_page)

    def test_part_check_is_resolver(self):
        url = reverse('part_check_page', args=[1])
        self.assertEquals(resolve(url).func, part_check_page)

    def test_job_list_is_resolver(self):
        url = reverse('job_list_page')
        self.assertEquals(resolve(url).func, job_list_page)

    def test_job_detail_is_resolver(self):
        url = reverse('job_details', args=[1])
        self.assertEquals(resolve(url).func, job_details)

    def test_creation_order_is_resolver(self):
        url = reverse('creation_order_page')
        self.assertEquals(resolve(url).func, creation_order_page)

    def test_order_pay_is_resolver(self):
        url = reverse('order_pay', args=[1000,1])
        self.assertEquals(resolve(url).func, order_pay)

    def test_bill_is_resolver(self):
        url = reverse('bill_page')
        self.assertEquals(resolve(url).func, bill_page)

    def test_recipe_is_resolver(self):
        url = reverse('recipe', args=[1])
        self.assertEquals(resolve(url).func, recipe)