from django.contrib import admin
from .models import rooms , comment, contactus, printpage


# Register your models here.
admin.site.register(rooms)
admin.site.register(comment)
admin.site.register(contactus)
admin.site.register(printpage)