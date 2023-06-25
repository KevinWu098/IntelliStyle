import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pytz import timezone

def getCalendarEvents():
    # Define the scopes required for calendar access
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Set up OAuth 2.0 credentials
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
    credentials = flow.run_local_server()

    # Create a service client
    service = build('calendar', 'v3', credentials=credentials)

    # Define the date for which you want to retrieve events
    date = datetime.datetime.today()  # Replace with your desired date

    # Convert the date to PDT timezone
    timezone_pdt = timezone('America/Los_Angeles')
    date_pdt = timezone_pdt.localize(date)

    # Adjust the start and end time of the day for PDT
    start_time = date_pdt.strftime('%Y-%m-%dT00:00:00-07:00')
    end_time = date_pdt.strftime('%Y-%m-%dT23:59:59-07:00')

    # Retrieve the events for the specified day
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_time,
        timeMax=end_time,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    event_summaries = []

    if not events:
        return "No Events Today"
    else:
        for event in events:
            event_summaries.append(event['summary'])
        return event_summaries