"""! File containing the class of a VEvent.
This class inherits from VBase.

@author Benjamin PAUMARD
@version 1.0.0
@since 25 November 2022
"""

# importing libs
from datetime import datetime
from io import TextIOWrapper

# importing modules
from data.ics.vbase import VBase
from data.ics.rrule import RRule
from data.ics.valarm import VAlarm


class VEvent(VBase):
    """! Class that contains the elements of an events.
    This class inherits from VBase.

    @author Benjamin PAUMARD
    @version 1.0.0
    @since 25 November 2022
    """

    def __init__(self, timestamp: datetime, uid: str, dtstart: datetime, dtend: datetime, tzstart: str = '',  tzend: str = '', summary: str = '', location: str = '', description: str = '', status: str = '', valarms: list[VAlarm] = [], rules: list[RRule] = []) -> None:
        """! Class used to store an event.
        This class inherit from the VBase one.

        @param timestamp the creation date of the element.
        @param uid the unique id of the element.
        @param dtstart the starting time of the database.
        @param dtend the ending time of the database.
        @param tzstart the timezone of the beginning datetime (optional).
        @param tzend the timezone of the ending datetime (optional).
        @param summary the description of the element (optional).
        @param description the description of the event (optional).
        @param status the status of the event (optional).
        @param valarms the alarms of the events (optional).
        @param rules the recursion rules of the event (optional).
        """

        # init the inherit class
        super().__init__(timestamp, uid, dtstart, tzstart, summary, valarms)

        # set the attributes
        self.__dtend: datetime = dtend
        self.__tzend: str = tzend
        self.__location: str = location
        self.__description: str = description
        self.__status: str = status
        self.__rules: list[RRule] = rules

    def get_dtend(self) -> datetime:
        """! Method to get the ending time.
        The end time is a datetime object.

        @return the ending time.
        """
        return self.__dtend

    def set_dtend(self, dtend: datetime) -> None:
        """! Method to set the ending time.
        The end time is a datetime object.

        @param dtend the ending time.
        """
        self.__dtend = dtend

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

    def get_location(self) -> str:
        """! Method to get the location of the event.
        The location is a string.

        @return the location of the event.
        """
        return self.__location

    def set_location(self, location: str) -> None:
        """! Method to set the location of the event.
        The location is a string.

        @param location the location of the event.
        """
        self.__location = location

    def get_description(self) -> str:
        """! Method to get the description of the event.
        The description is a string.

        @return the description of the event.
        """
        return self.__description

    def set_description(self, description: str) -> None:
        """! Method to set the description of the event.
        The description is a string.

        @param description the description of the event.
        """
        self.__description = description

    def get_status(self) -> str:
        """! Method to get the status of the event.
        The status is a string.

        @return the status of the event.
        """
        return self.__status

    def set_status(self, status: str) -> None:
        """! Method to set the status of the event.
        The status is a string.

        @param status the status of the event.
        """
        self.__status = status

    def get_rrules(self) -> list[RRule]:
        """! Method to get the recursion rules of the event.
        The rules are objects of type RRules.

        @return the list of the rules of the event.
        """
        return self.__rules

    def set_rrules(self, rrules: list[RRule]) -> None:
        """! Method to set the recursion rules of the event.
        The rules are objects of type RRules.

        @param vrules the list of the rules of the event.
        """
        self.__rules = rrules

    def add_rrule(self, rule: RRule) -> None:
        """! Method to add a recursion rule of the event.
        The rules are objects of type RRules.

        @param rules the list of the rules of the event.
        """
        self.__rules.append(rule)


    def save(self, f: TextIOWrapper) -> None:
        """! Method that save the vevent into a file.
        All alarms and rules will be saved as well.

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        # write all basic data
        f.write("BEGIN:VEVENT\n")
        f.write(f"UID:{self.get_uid()}\n")
        f.write(f"DTSTAMP:{self.get_timestamp().strftime('%Y%m%dT%H%M%S')}\n")
        
        # if summary is not empty write it
        if (self.get_summary() != ''):
            f.write(f"SUMMARY:{self.get_summary()}\n")
        
        # write the start time
        f.write(f"DTSTART:{self.get_tzstart()}:{self.get_dtstart().strftime('%Y%m%dT%H%M%S')}\n")
        
        # write the ending time
        f.write(f"DTEND:{self.get_tzend()}:{self.get_dtend().strftime('%Y%m%dT%H%M%S')}\n")
        
        # if location is not empty write it
        if (self.get_location() != ''):
            f.write(f"LOCATION:{self.get_location()}\n")
        
        # if description is not empty write it
        if (self.get_description() != ''):
            f.write(f"DESCRIPTION:{self.get_location()}\n")

        # if status is not empty write it
        if (self.get_status() != ''):
            f.write(f"STATUS:{self.get_status()}\n")

        # print each rule
        for rule in self.__rules:
            if (rule.get_until() != ''):
                f.write(
                f"RRULE:FREQ={rule.get_frequency()};UNTIL={rule.get_until()}\n")
            else:
               f.write(
                f"RRULE:FREQ={rule.get_frequency()}\n") 

        # print each alarm
        for alarm in self.get_valarms():
            alarm.save(f)

        # write the end of the vevent
        f.write(f"END:VEVENT\n")

    def export_csv(self, f: TextIOWrapper) -> None:
        """! Method that export an event into a CSV.
        The file used may be opened in the calendar class.

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        # write the line with the data
        f.write(
            f"vevent,{self.get_timestamp().strftime('%Y%m%dT%H%M%S')},{self.get_uid()},{self.get_summary()},{self.get_dtstart().strftime('%Y%m%dT%H%M%S')},{self.get_status()}\n")

    def export_html(self, f: TextIOWrapper) -> None:
        """! Method that export an event into a HTML file.
        The file used may be opened in the calendar class.

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        f.write("<div class=\"vevent\">\n")
        f.write(f"\
        <div class=\"summary\">{self.get_summary()}</div>\n\
        <abbr class=\"dtstart\" title=\"{self.get_dtstart().strftime('%Y%m%dT%H%M%S')}\">{self.get_dtstart()}</abbr>\n\
        <abbr class=\"dtend\" title=\"{self.get_dtend().strftime('%Y%m%dT%H%M%S')}\">{self.get_dtend()}</abbr>\n\
        <div class=\"location\">{self.get_location()}</div>\n\
        <div class=\"status\">{self.get_status()}</div>\n"
        )
        f.write("</div>\n")
