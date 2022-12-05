"""! File containing the class of a VTodo.
This class inherits from VBase.

@author Benjamin PAUMARD
@version 1.0.0
@version 04 December 2022
"""

# importing libs
from datetime import datetime
from io import TextIOWrapper

# importing modules
from data.ics.valarm import VAlarm
from data.ics.vbase import VBase


class VTodo(VBase):
    """! Class that contains the elements of an events.
    This class inherits from VBase.

    @author Benjamin PAUMARD
    @version 1.0.0
    @version 04 December 2022
    """

    def __init__(self, timestamp: datetime, uid: str, dtstart: datetime, tzstart: str = '', summary: str = '', duration: str = '', status: str = '', valarms: list[VAlarm] = []) -> None:
        """! Class used to store an event.
        This class inherit from the VBase one.

        @param timestamp the creation date of the element.
        @param uid the unique id of the element.
        @param dtstart the starting time of the database.
        @param dtend the ending time of the database.
        @param tzstart the timezone of the beginning datetime (optional).
        @param tzend the timezone of the ending datetime (optional).
        @param summary the description of the element (optional).
        @param duration the duration of the task (optional).
        @param status the status of the event (optional).
        @param valarms the alarms of the event (optional).
        """

        # init the inherit class
        super().__init__(timestamp, uid, dtstart, tzstart, summary, valarms)

        # set the attributes
        self.__duration: str = duration
        self.__status: str = status


    def get_duration(self) -> str:
        """! Method to get the timezone of the ending time.
        The time zone is a string indicating the zone where the ending date is.

        @return the ending date time zone.
        """
        return self.__duration

    def set_duration(self, duration: str) -> None:
        """! Method to set the timezone of the ending time.
        The time zone is a string indicating the zone where the ending date is.

        @param tzend the ending date time zone.
        """
        self.__duration = duration

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

    def save(self, f: TextIOWrapper) -> None:
        """! Method that save the vevent into a file.
        All alarms and rules will be saved as well.

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        # write all basic data
        f.write("BEGIN:TODO\n")
        f.write(f"UID:{self.__uid}\n")
        f.write(f"DTSTAMP:{self.__timestamp.strftime('%Y%m%dT%H%M%S')}\n")
        f.write(f"SUMMARY:{self.__summary}\n")
        f.write(f"DTSTART;{self.__tzstart}:{self.__dtstart.strftime('%Y%m%dT%H%M%S')}\n")
        f.write(f"DURATION:{self.__duration}\n")
        f.write(f"STATUS:{self.__status}\n")

        # print each alarm
        for alarm in self.__valarms:
            alarm.save(f)

        # write the end of the vevent
        f.write(f"END:TODO\n")

    def export_csv(self, f: TextIOWrapper) -> None:
        """! Method that export an event into a CSV.
        The file used may be opened in the calendar class.

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        f.write(
            f"vtodo,{self.get_timestamp().strftime('%Y%m%dT%H%M%S')},{self.get_uid()},{self.get_summary()},{self.get_dtstart().strftime('%Y%m%dT%H%M%S')},{self.get_status()}\n")

    def export_html(self, f: TextIOWrapper) -> None:
        """! Method that export an event into a HTML file.
        The file used may be opened in the calendar class.

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        f.write("<div class=\"vtodo\">\n")
        f.write(f"\
            \t<div class=\"summary\">{self.get_summary()}</div>\n\
            \t<abbr class=\"dtstart\" title=\"{self.get_dtstart().strftime('%Y%m%dT%H%M%S')}\">{self.get_dtstart()}</abbr>\n\
            \t<div class=\"duration\">{self.get_duration()}</div>\n\
            \t<div class=\"status\">{self.get_duration()}</div>\n"
        )
        f.write("</div>\n")
