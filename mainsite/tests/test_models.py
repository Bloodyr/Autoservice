from django.test import TestCase
from django.contrib.auth.models import User
from mainsite.models import Auto, ClientAuto


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='Eldar',
        )

        car1 = Auto.objects.create(
            brand = 'Toyota',
            model = '2005',
            gov_number = '1234567'
        )

        car2 = Auto.objects.create(
            brand = 'Lada',
            model = '1815',
            gov_number = '1234567'
        )

    def test_cars_creation(self):
        cars = Auto.objects.all()
        count=0
        for car in cars:
            count+=1
        test = Auto.objects.get(brand='Lada')
        self.assertEquals(test.model, '1815')
        self.assertEquals(count,2)

    def test_user_car_relation(self):
        auto1 = Auto.objects.get(brand='Toyota')
        auto2 = Auto.objects.get(brand='Lada')

        ClientAuto.objects.create(
            client = self.user,
            auto = auto1
        )

        ClientAuto.objects.create(
            client = self.user,
            auto = auto2
        )
        counter=0
        cars = ClientAuto.objects.all()
        for car in cars:
            counter+=1

        self.assertEqual(counter, 2)

        