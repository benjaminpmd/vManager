import icalendar as ics

class CalendarManager:
    def __init__(self, path: str = '') -> None:
        self.path = path
        if (path == ''):
            self.calendar = ics.Calendar()
        else:
            with open(path, 'r') as f:
                self.calendar: ics.Calendar = ics.Calendar.from_ical(f.read())       

            
    
    def get_formatted_events(self):
        events: list[dict] = []
        
        for component in self.calendar.walk("VEVENT"):
            
            event: dict[str, any] = {}
            
            event["start_date"] = component["DTSTART"].dt
            event["end_date"] = component["DTEND"].dt
            event["timestamp"] = component["DTSTAMP"].dt
            event["creation_date"] = component["CREATED"].dt
            if (component.get("T-MODIFIED") != None):
                event["modified_date"] = component["T-MODIFIED"].dt
            else:
                event["modified_date"] = False
            event["rule"] = {}
            event["rule"]["repeat"] =  [component["RRULE"]["FREQ"][i].lower() for i in range(len(component["RRULE"]["FREQ"]))]
            event["rule"]["until"] =  component["RRULE"]["UNTIL"][0]
            event["summary"] = component["SUMMARY"]
            
            events.append(event)

        return events
