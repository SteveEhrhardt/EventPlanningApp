from django import forms
from . models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'client_name',
            'client_street_address',
            'client_city',
            'client_state',
            'client_zip_code',
            'client_phone_number',
            'client_email_address',
            'event_manager_name',
            'date_first_contacted',
            'date_last_contacted',
            'preferred_event_date',
            'actual_event_date',
            'venue_name',
            'band',
            'florist',
            'caterer',
            'notes',
        ]

        