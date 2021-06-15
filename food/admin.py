

# Register your models here.

from django.contrib import admin
from recommend.models import Food, Myfoodrating, MyfoodList

# Register your models here.
admin.site.register(Food)
admin.site.register(Myfoodrating)
admin.site.register(MyfoodList)