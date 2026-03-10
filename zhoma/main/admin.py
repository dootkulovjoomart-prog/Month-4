from django.contrib import admin

# Register your models here.

from .models import Celebrities ,  Club , Trophy 

admin.site.register(Celebrities)
admin.site.register(Club)
admin.site.register(Trophy)

