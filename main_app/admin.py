from django.contrib import admin
from .models import Cow, Feeding, Toy

# Register your models here.

admin.site.register(Cow)
admin.site.register(Feeding)
admin.site.register(Toy)