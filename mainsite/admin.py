from django.contrib import admin
from .models import Auto, ClientAuto, Part, Mesurable, PartsPrice, Jobtype, JobPrice, Order


# admin.site.register(Client)
admin.site.register(Auto)
admin.site.register(ClientAuto)
admin.site.register(Part)
admin.site.register(Mesurable)
admin.site.register(PartsPrice)
admin.site.register(Jobtype)
admin.site.register(JobPrice)
admin.site.register(Order)