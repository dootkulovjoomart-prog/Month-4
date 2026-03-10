from django.db import models

# Create your models here.


class Trophy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    liga = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name } , {self.liga}"

class Celebrities(models.Model):
    name = models.CharField('И.Ф.О', max_length=50)
    image = models.ImageField(null=True , blank = True , upload_to= 'main')
    profession = models.CharField('Профессия' , max_length=50)
    discription = models.TextField('Биграфия')
    content = models.TextField('Контент' , null=True , blank= True )
    date = models.DateField('Дата публикации') 
    club = models.ForeignKey(Club , on_delete= models.CASCADE , null=True) 
    trophy = models.ManyToManyField(Trophy)
  




    def __str__(self):
        return self.name

