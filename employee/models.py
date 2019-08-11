from django.db import models

# Create your models here.


class Employee(models.Model):
	eid = models.CharField(max_length=20)
	ename = models.CharField(max_length=100)
	email = models.EmailField()
	contact = models.CharField(max_length=10)

	class Meta:
		db_table = "employee"
