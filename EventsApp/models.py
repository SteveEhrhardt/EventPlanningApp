from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_name = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=2)
    contact_name= models.CharField(max_length=50)
    phone_number= models.CharField(max_length=20)
    website_url= models.URLField(blank=True)
    notes= models.TextField(blank=True)

    def __str__(self):
        return self.venue_name

class Band(models.Model):
    band_name = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=2)
    contact_name= models.CharField(max_length=50)
    phone_number= models.CharField(max_length=20)
    website_url= models.URLField(blank=True)
    notes= models.TextField(blank=True)

    def __str__(self):
        return self.band_name

class Florist(models.Model):
    florist_name = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=2)
    contact_name= models.CharField(max_length=50)
    phone_number= models.CharField(max_length=20)
    website_url= models.URLField(blank=True)
    notes= models.TextField(blank=True)

    def __str__(self):
        return self.florist_name

class Caterer(models.Model):
    caterer_name = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=2)
    contact_name= models.CharField(max_length=50)
    phone_number= models.CharField(max_length=20, blank=True)
    website_url= models.URLField(blank=True)
    notes= models.TextField(blank=True)

    def __str__(self):
        return self.caterer_name
    
class Event(models.Model):    
    client_name = models.CharField(max_length=75)
    client_street_address = models.CharField(max_length=75)
    client_city = models.CharField(max_length=50)
    client_state = models.CharField(max_length=2)
    client_zip_code = models.CharField(max_length=10)
    client_phone_number = models.CharField(max_length=20, blank=True)
    client_email_address = models.EmailField(blank=True)
    event_manager_name = models.CharField(max_length=75)
    date_first_contacted = models.DateField()
    date_last_contacted = models.DateField(null=True, blank=True)
    preferred_event_date = models.DateField(null=True, blank=True)
    actual_event_date = models.DateField(null=True, blank=True)
    venue_name = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True)   
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)
    florist = models.ForeignKey(Florist, on_delete=models.SET_NULL, null=True, blank=True)
    caterer =models.ForeignKey(Caterer, on_delete=models.SET_NULL, null=True, blank=True)
    notes= models.TextField(blank=True)

    def __str__(self):
        return self.client_name

