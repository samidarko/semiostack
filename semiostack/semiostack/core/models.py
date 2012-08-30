from django.db import models

class Semiocoder(models.Model):
    name = models.CharField(max_length=10, unique=False,)
    adresse = models.IPAddressField(unique=False,)

    def __unicode__(self):
        return self.name   