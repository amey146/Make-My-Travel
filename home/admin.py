from django.contrib import admin
from .models import Flight, Home, Itinerary, ItineraryDay, Places
# Register your models here.
admin.site.register(Flight)
admin.site.register(Home)
admin.site.register(Itinerary)
admin.site.register(ItineraryDay)
admin.site.register(Places)