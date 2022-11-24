from ics import Calendar
import requests
import arrow

ms_calendar_url = "https://outlook.office365.com/owa/calendar/082ea3b36412419cae8917d72a0e9ef1@microsoft.com/a21381e028f840a38c5741372420ae9c12844932849465516124/S-1-8-626361487-1738957682-918359862-3134698642/reachcalendar.ics"
ms_calendar = Calendar(requests.get(ms_calendar_url).text)

now = arrow.utcnow()

next_events = ms_calendar.timeline.start_after(now)
next_busy_events = filter(lambda event: event.name == 'Busy', next_events)

next_event = next(next_busy_events)