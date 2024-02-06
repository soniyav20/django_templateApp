from django.db import models

# Create your models here.
class Employee(models.Model):
    EmpId=models.IntegerField(unique=True,null=False)
    EmpName=models.CharField(max_length=20)
    Salary=models.FloatField()
    TempEmp=models.BooleanField()
    JoinDate=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return super().__str__()