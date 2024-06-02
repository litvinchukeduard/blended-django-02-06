from django.contrib import admin

from trip_app.models import Trip, Review, Destination, Friend

# Register your models here.
admin.site.register(Trip)
admin.site.register(Review)
admin.site.register(Destination)
admin.site.register(Friend)
