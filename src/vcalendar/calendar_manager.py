import icalendar as ics

class CalendarManager:
    def __init__(self, path: str = '') -> None:
        self.path = path
        if (path == ''):
            self.calendar = ics.Calendar()
        else:
            with open(path, 'r') as f:
                self.calendar: ics.Calendar = ics.Calendar.from_ical(f.read())       

            
    
    def get_formatted_events(self) -> None:
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


    def export_csv(self, output_path: str) -> None:

        events = self.get_formatted_events()

        with open(output_path, 'w') as f:
            f.write("summary,start date,end date,creation date\n")

            for event in events:
                summary: str = event["summary"]
                start_time = event["start_date"]
                end_time = event["end_date"]
                creation_date = event["creation_date"]
                f.write(f"{summary},{start_time},{end_time},{creation_date}\n")

    def export_html(self, output_path: str) -> None:
        events = self.get_formatted_events()

        with open(output_path, 'w') as f:
            for event in events:
                f.write("<div class=\"vevent\">\n")
                summary: str = event["summary"]
                start_time = event["start_date"]
                end_time = event["end_date"]
                creation_date = event["creation_date"]
                f.write(f"\t<span class=\"summary\">{summary}</span>\n\t<span class=\"dtstart\">{start_time}</span>\n\t<span class=\"dtend\">{end_time}</span>\n\t<span class=\"created\">{creation_date}</span>\n")
                f.write("</div>\n")
            
