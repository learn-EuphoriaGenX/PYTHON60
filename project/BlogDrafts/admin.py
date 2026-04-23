from django.contrib import admin
from .models import Category, Blog, Payment

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Payment)

