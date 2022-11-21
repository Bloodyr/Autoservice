from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    "Модель описывает профиль клиента, имя, фамилию, и никнейм"
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=99)
    second_name = models.CharField(max_length=99)
    username = models.CharField(max_length=99)

    def __str__(self) -> str:
        return self.username


class Auto(models.Model):
    "Модель описывает автомобиль, брэнд, модель, и номер."
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    gov_number = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "Brand {}|Model {}".format(self.brand, self.model)


class ClientAuto(models.Model):
    "Модель связывает машины которые есть у пользователя"
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Клиент {}|Авто {}".format(self.client,self.auto)


class Part(models.Model):
    "Название детали"
    part_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.part_name


class Mesurable(models.Model):
    "Измерение"
    mesurable_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.mesurable_name


class PartsPrice(models.Model):
    "Цены детали которые задаются её названием колличеством и измерением"
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    mesurable = models.ForeignKey(Mesurable, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return "Деталь |{}|-Измерение |{}|-Колличество |{}|".format(
            self.part.part_name,
            self.mesurable.mesurable_name,
            self.amount)


class Jobtype(models.Model):
    job_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.job_name


class JobPrice(models.Model):
    job = models.ForeignKey(Jobtype, on_delete=models.CASCADE)
    mesurable = models.ForeignKey(Mesurable, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return "Работа {}|Измерение {}|Колличество {}".format(
                                                        self.job.job_name, 
                                                        self.mesurable.mesurable_name,
                                                        self.amount)


class Order(models.Model):
    status_choice = (
        ("В работе","В работе"),
        ("Ожидает оплаты","Ожидает оплаты"),
        ("Размещён","Размещён"),
    )
    order_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPrice, on_delete=models.CASCADE)
    parts_price = models.ForeignKey(PartsPrice, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15,
        choices=status_choice,
    )

    def __str__(self) -> str:
        return "Заказ клиента {}|Статус {}| Работа {}|Деталь {}".format(
            self.client.username, 
            self.status, 
            self.job.job.job_name)