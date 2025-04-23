# google_calendar.py

import os
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def schedule_google_calendar_event(date_time: str, description: str) -> str:
    """Creates a service appointment event in Google Calendar."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': 'Car Service Appointment',
        'description': description,
        'start': {
            'dateTime': date_time,
            'timeZone': 'Australia/Sydney',
        },
        'end': {
            'dateTime': (datetime.datetime.fromisoformat(date_time) + datetime.timedelta(hours=1)).isoformat(),
            'timeZone': 'Australia/Sydney',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return f"✅ Service scheduled! View in Calendar: {event.get('htmlLink')}"
