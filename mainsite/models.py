from django.db import models
from django.contrib.auth.models import User


# class Client(models.Model):
#     "Модель описывает профиль клиента, имя, фамилию, и никнейм"
#     user =  models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')

#     username = models.CharField(max_length=99)
#     def __str__(self) -> str:
#         return self.username
#     class Meta:
#         verbose_name = "Клиент"
#         verbose_name_plural = "Клиенты"
        


class Auto(models.Model):
    "Модель описывает автомобиль, брэнд, модель, и номер."
    brand = models.CharField(max_length=100, verbose_name="Брэнд")
    model = models.CharField(max_length=100, verbose_name="Модель")
    gov_number = models.CharField(max_length=100, verbose_name="Номер")

    def __str__(self) -> str:
        return "Brand {}|Model {}".format(self.brand, self.model)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class ClientAuto(models.Model):
    "Модель связывает машины которые есть у пользователя"
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент")
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, verbose_name="Автомобиль")

    def __str__(self) -> str:
        return "Клиент {}|Авто {}".format(self.client,self.auto)

    class Meta:
        verbose_name = "Автомобиль клиента"
        verbose_name_plural = "Автомобили клиентов"


class Part(models.Model):
    "Название детали"
    part_name = models.CharField(max_length=100, verbose_name="Деталь")

    def __str__(self) -> str:
        return self.part_name

    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"


class Mesurable(models.Model):
    "Измерение"
    mesurable_name = models.CharField(max_length=100, verbose_name="Название измерения")

    def __str__(self) -> str:
        return self.mesurable_name

    class Meta:
        verbose_name = "Измерение"
        verbose_name_plural = "Измерения"


class PartsPrice(models.Model):
    "Цены детали которые задаются её названием колличеством и измерением"
    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name="Деталь")
    mesurable = models.ForeignKey(Mesurable, on_delete=models.CASCADE, verbose_name="Измерение")
    amount = models.IntegerField(default=0,verbose_name="Колличество")

    def __str__(self) -> str:
        return "Деталь |{}|-Измерение |{}|-Колличество {}|".format(
            self.part.part_name,
            self.mesurable.mesurable_name,
            self.amount)
    
    class Meta:
        verbose_name = "Цена детали"
        verbose_name_plural = "Цены деталей"



class Jobtype(models.Model):
    job_name = models.CharField(max_length=100,verbose_name="Название работы")

    def __str__(self) -> str:
        return self.job_name

    class Meta:
        verbose_name = "Тип работы"
        verbose_name_plural = "Типы работ"



class JobPrice(models.Model):
    job = models.ForeignKey(Jobtype, on_delete=models.CASCADE, verbose_name="Работа")
    mesurable = models.ForeignKey(Mesurable, on_delete=models.CASCADE, verbose_name="Измерение")
    amount = models.IntegerField(default=0, verbose_name="Колличество")

    def __str__(self) -> str:
        return "Работа {}|Измерение {}|Колличество {}".format(
                                                        self.job.job_name, 
                                                        self.mesurable.mesurable_name,
                                                        self.amount)

    class Meta:
        verbose_name = "Цена за работу"
        verbose_name_plural = "Цена за работы"


class Order(models.Model):
    status_choice = (
        ("В работе","В работе"),
        ("Ожидает оплаты","Ожидает оплаты"),
        ("Размещён","Размещён"),
    )
    order_date = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент")
    job = models.ForeignKey(JobPrice, on_delete=models.CASCADE, verbose_name="Работа")
    parts_price = models.ForeignKey(PartsPrice, on_delete=models.CASCADE, verbose_name="Цена детали")
    status = models.CharField(
        max_length=15,
        choices=status_choice,
        verbose_name="Статус",
    )
    car = models.ForeignKey(ClientAuto, on_delete=models.CASCADE, verbose_name='Машина клиента')

    def __str__(self) -> str:
        return "Заказ клиента {}|Статус {}| Работа {}|Деталь {}".format(
            self.client.username, 
            self.status,
            self.job.job.job_name,
            self.parts_price.part)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"