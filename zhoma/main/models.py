from django.db import models

# Create your models here.

class Celebrities(models.Model):
    name = models.CharField('И.Ф.О', max_length=50)
    profession = models.CharField('Профессия' , max_length=50)
    discription = models.TextField('Биграфия')
    date = models.DateField('Дата публикации')  


    def __str__(self):
        return self.name

