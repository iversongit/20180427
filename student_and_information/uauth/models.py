from django.db import models

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=10)
    u_password = models.CharField(max_length=255)
    u_ticket = models.CharField(max_length=30,null=True)

    class Meta:
        db_table = "user"