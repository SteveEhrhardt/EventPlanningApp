# Register your models here.
from django.contrib import admin
from .models import Venue, Event, Band, Florist, Caterer
 
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Band)
admin.site.register(Florist)
admin.site.register(Caterer)
