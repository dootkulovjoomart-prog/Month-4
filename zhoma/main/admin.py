from django.contrib import admin

# Register your models here.

from .models import Celebrities ,  Club , Trophy , Wife

admin.site.register(Celebrities)
admin.site.register(Club)
admin.site.register(Trophy)
admin.site.register(Wife)

