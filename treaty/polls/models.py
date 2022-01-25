from django.db import models

# Create your models here.


class Employees(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    second_name = models.CharField('Фамилия', max_length=100)
    third_name = models.CharField('Отчество', max_length=100)
    characteristic = models.CharField('Характеристика', max_length=250)
    addres = models.CharField('Адрес', max_length=100)
    positions = models.ForeignKey('Positions', on_delete=models.CASCADE)



class Positions(models.Model):
    title = models.CharField(max_length=250)



class Projects(models.Model):
    name = models.CharField('Название', max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class EmployeeProject(models.Model):
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
    days = models.CharField('Количество отработанных дней',max_length=50)

class Salaries(models.Model):
    amount = models.FloatField('Оклад', max_length=100)
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)


