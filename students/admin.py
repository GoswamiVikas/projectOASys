from django.contrib import admin
from students import models

# Register your models here.
admin.site.register(models.Subjects)
admin.site.register(models.Teaches)
admin.site.register(models.Assignment)