from django.contrib import admin
from subscriber.models import Subscriber
from subscriber.models import Issue
from subscriber.models import Order

admin.site.register(Subscriber)
admin.site.register(Issue)
admin.site.register(Order)

# Register your models here.
