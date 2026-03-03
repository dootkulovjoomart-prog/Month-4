from django.db import models

# Create your models here.

class Celebrities(models.Model):
    name = models.CharField('И.Ф.О', max_length=50)
    image = models.ImageField(null=True , upload_to= 'main')
    profession = models.CharField('Профессия' , max_length=50)
    discription = models.TextField('Биграфия')
    content = models.TextField('Контент' , null=True , blank= True )
    date = models.DateField('Дата публикации')  


    def __str__(self):
        return self.name

