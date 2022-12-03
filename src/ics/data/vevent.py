from datetime import datetime
from io import TextIOWrapper
from ics.data.vrule import VRule
from ics.data.valarm import VAlarm


class VEvent:
    def __init__(self, summary: str = '', tzstart: str = '',  dtstart: datetime = datetime.now(), tzend: str = '', dtend: datetime = datetime.now(), location: str = '', description: str = '', status: str = '', valarms: list[VAlarm] = [], vrules: list[VRule] = []) -> None:
        """! Class used to store data of a phone.
        This class can store a phone number and its type.

        @param tzstart the timezone of the beginning datetime.
        @param tzsend the timezone of the ending datetime.
        @param preferential whether the phone is the preferred one.
        """
        self.__summary: str = summary
        self.__tzstart: str = tzstart
        self.__dtstart: datetime = dtstart
        self.__tzend: str = tzend
        self.__dtend: datetime = dtend
        self.__location: str = location
        self.__description: str = description
        self.__status: str = status
        self.__valarms: list[VAlarm] = valarms
        self.__rules: list[VRule] = vrules


    def get_summary(self) -> str:
        return self.__summary

    def set_summary(self, summary: str) -> None:
        self.__summary = summary

    def get_tzstart(self) -> str:
        """! Method to get the timezone of the beginning time.
        The time zone is a string indicating the zone where the beginning date is.
        
        @return the beginning date time zone.
        """
        return self.__tzstart

    def set_tzstart(self, tzstart: str) -> None:
        """! Method to set the timezone of the beginning time.
        The time zone is a string indicating the zone where the beginning date is.
        
        @param tzstart the beginning date time zone.
        """
        self.__tzstart = tzstart

    def get_dtstart(self) -> datetime:
        return self.__dtstart

    def set_dtstart(self, dtstart: datetime) -> None:
        self.__dtstart = dtstart

    def get_tzend(self) -> str:
        """! Method to get the timezone of the ending time.
        The time zone is a string indicating the zone where the ending date is.
        
        @return the ending date time zone.
        """
        return self.__tzend

    def set_tzend(self, tzend: str) -> None:
        """! Method to set the timezone of the ending time.
        The time zone is a string indicating the zone where the ending date is.
        
        @param tzend the ending date time zone.
        """
        self.__tzend = tzend

    def get_dtend(self) -> datetime:
        return self.__dtend

    def set_dtend(self, dtend: datetime) -> None:
        self.__dtend = dtend

    def get_location(self) -> str:
        return self.__location

    def set_location(self, location: str) -> None:
        self.__location = location

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str) -> None:
        self.__description = description

    def get_status(self) -> str:
        return self.__status

    def set_status(self, status: str) -> None:
        self.__status = status

    def get_valarms(self) -> list[VAlarm]:
        return self.__valarms

    def set_valarms(self, valarms: list[VAlarm]) -> None:
        self.__valarms = valarms

    def get_vrules(self) -> list[VRule]:
        return self.__rules

    def set_vrules(self, vrules: list[VRule]) -> None:
        self.__rules = vrules

    def save(self, f: TextIOWrapper) -> None:
        """! Method that save the vevent into a file.
        All alarms and rules will be saved as well.
        
        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        # write all basic data
        f.write("BEGIN:VEVENT\n")
        f.write(f"SUMMARY:{self.__summary}\n")
        f.write(f"DTSTART;{self.__tzstart}:{self.__dtstart}\n")
        f.write(f"DTEND;{self.__tzend}:{self.__dtend}\n")
        f.write(f"LOCATION:{self.__location}\n")
        f.write(f"DESCRIPTION:{self.__description}\n")
        f.write(f"STATUS:{self.__status}\n")
        
        # print each rule
        for rule in self.__rules:
            f.write(f"RRULE:FREQ={rule.get_frequency()};UNTIL={rule.get_until()}\n")

        # print each alarm
        for alarm in self.__valarms:
            f.write("BEGIN:VALRM\n")
            f.write(f"TRIGGER:{alarm.get_trigger()}\n")
            f.write(f"DESCRIPTION:{alarm.get_description()}\n")
            f.write(f"ACTION:{alarm.get_action()}\n")
            f.write("BEGIN:VALRM")

        # write the end of the vevent
        f.write(f"END:VEVENT\n")

    def export_csv(self, f: TextIOWrapper) -> None:
        """! Method that export an event into a CSV.
        All rules and alarms will be exported too.
        
        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        f.write(f"{self.__summary},{self.__dtstart},{self.__dtend},{self.__location},{self.__status}\n")

    def export_html(self, f: TextIOWrapper) -> None:
        """! Method that export an event into a HTML file.
        All rules and alarms will be exported too.
        
        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        f.write("<div class=\"vevent\">\n")
        f.write(f"\t<span class=\"summary\">{self.__summary}</span>\n\t<span class=\"dtstart\">{self.__dtstart}</span>\n\t<span class=\"dtend\">{self.__dtend}</span>\n\t<span class=\"location\">{self.__location}</span>\n\t<span class=\"status\">{self.__status}</span>\n")
        f.write("</div>\n")
