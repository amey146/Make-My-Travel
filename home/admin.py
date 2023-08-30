from django.contrib import admin
from .models import Flight, Home, Itinerary, ItineraryDay
# Register your models here.
admin.site.register(Flight)
admin.site.register(Home)
admin.site.register(Itinerary)
admin.site.register(ItineraryDay)