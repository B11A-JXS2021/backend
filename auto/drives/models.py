from django.db import models
from django.conf import settings


class Drive(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+", on_delete=models.CASCADE, null=True)
    accel_x = models.DecimalField(max_digits=19, decimal_places=2)
    accel_y = models.DecimalField(max_digits=19, decimal_places=2)
    accel_z = models.DecimalField(max_digits=19, decimal_places=2)
    timestamp = models.DateTimeField(null=True)
