from django.db import models


class TimeStampUtil(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimeStampUtil):
    username = models.CharField(max_length=16, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=12, blank=True, null=True, unique=True)
    active = models.BooleanField(default=False)
    balance = models.FloatField(default=0, blank=True, null=True)
    first_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.email
