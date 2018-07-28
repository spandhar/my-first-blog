from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(NewClientOrder)
admin.site.register(CreateMergeOrder)
admin.site.register(NewStreetOrder)
admin.site.register(StreetExecutionReport)
admin.site.register(RplStreetOrder)

