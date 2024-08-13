from django.db import models
# from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Usr(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    class Meta:
        db_table="Usr_details"

class Proffesional(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=100)
    phone = models.IntegerField()
    qualification=models.CharField(max_length=100)
    work_experiece=models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table="proffesional_detail"


class Servicesreq(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=100)
    phone = models.IntegerField()
    services = models.CharField(max_length=100)
    technician = models.CharField(max_length=100)
    # technician_mobile=models.IntegerField()
    class Meta:
        db_table="service_detail"