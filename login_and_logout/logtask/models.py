from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=10)
    s_age = models.IntegerField
    s_school = models.CharField(max_length=10)
    s_create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "student"