from django.contrib import admin

from .models import Recipient, Gift, Occasion


admin.site.register(Recipient)
admin.site.register(Gift)
admin.site.register(Occasion)
