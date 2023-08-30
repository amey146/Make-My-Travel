from django.db import models
from datetime import date

# Create your models here.
class Home(models.Model):
    cn = models.CharField(max_length=30)
    cd = models.CharField(max_length=125)
    cl = models.CharField(max_length=30)

class Flight(models.Model):
    Source = models.CharField(max_length=30)
    Destination = models.CharField(max_length=30)
    Date = models.DateField(max_length=30)
    Time = models.TimeField(max_length=30)
    dDate = models.DateField(max_length=30)
    dTime = models.TimeField(max_length=30)
    eFare = models.CharField(max_length=30)
    bFare = models.CharField(max_length=30)
    eSeats = models.CharField(max_length=30)
    bSeats = models.CharField(max_length=30)
    Layover = models.CharField(max_length=30)
    ProviderName = models.CharField(max_length=30)
    ProviderLogo = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Source} - {self.Destination}"
    
class Itinerary(models.Model):
    Destination = models.CharField(max_length=30)
    OfferPrice = models.IntegerField()
    def __str__(self):
        return str(self.Destination)
    
    class Meta:
        verbose_name_plural = "Itineraries"
    
class ItineraryDay(models.Model):
    DestinationName = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    Title= models.CharField(max_length=30)
    Description = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.DestinationName} - {self.Title}"

    
