from django.db import models

# Create your models here.
class Hall(models.Model):
  short_name = models.CharField(max_length=20, verbose_name='Короткое название')
  full_name = models.CharField(max_length=50, verbose_name='Полное название')

class Shelf(models.Model):
  number = models.IntegerField(verbose_name='Номер стеллажа')
  hall = models.ForeignKey(Hall, on_delete=models.CASCADE,verbose_name='Зал')

class Book(models.Model):
  name = models.TextField(null=False,blank=True,verbose_name='Название')
  authors = models.TextField(null=False,blank=True,verbose_name='Авторы')
  chapter = models.IntegerField(verbose_name='Том')
  isbn = models.CharField(max_length=13,verbose_name='Код ISBN')
  publishing_year = models.IntegerField(verbose_name='Год издания')
  shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE,verbose_name='Стеллаж')
  shelf_number = models.IntegerField(verbose_name='Номер полки')
  amount = models.IntegerField(verbose_name='Кол-во экземпляров')
