from django.contrib import admin

# Register your models here.

from .models import ContactForm



admin.site.register(ContactForm)

from .models import Reach

admin.site.register(Reach)