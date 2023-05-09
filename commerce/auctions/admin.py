from django.contrib import admin
from .models import User, listing, category

# Register your models here.
admin.site.register(User)
admin.site.register(listing)
admin.site.register(category)