"""! File containing the class that is the base of both events and todo.
VEvents and VTodo herits from this class.

@author Benjamin PAUMARD
@version 1.0.0
@version 25 November 2022
"""

# importing libs
from datetime import datetime

from data.ics.valarm import VAlarm


class VBase:
    """! Class that contains the elements of an alarm.
    Alarms are part of a VEvent.

    @author Benjamin PAUMARD
    @version 1.0.0
    @version 25 November 2022
    """

    def __init__(self, timestamp: datetime, uid: str,  dtstart: datetime, tzstart: str = '', summary: str = '', valarms: list[VAlarm] = []) -> None:
        """! Class that is the base of both events and todo.
        VEvents and VTodo herits from this class.

        @param timestamp the creation date of the element.
        @param uid the unique id of the element.
        @param dtstart the starting time of the database.
        @param tzstart the timezone of the beginning datetime (optional).
        @param summary the description of the element (optional).
        @param valarms the alarms of the element (optional).
        """
        self.__timestamp: datetime = timestamp
        self.__uid: str = uid
        self.__summary: str = summary
        self.__dtstart: datetime = dtstart
        self.__tzstart: str = tzstart
        self.__valarms: list[VAlarm] = valarms

    def get_timestamp(self) -> datetime:
        """! Method to get the creation date of the element.
        The creation date is a datetime object.

        @return the creation date.
        """
        return self.__timestamp

    def set_timestamp(self, timestamp: datetime) -> None:
        """! Method to set the creation date of the element.
        The creation date is a datetime object.

        @param timestamp the creation date.
        """
        self.__timestamp = timestamp

    def get_uid(self) -> str:
        """! Method to get the unique ID of the element.
        The unique ID is a string.

        @return the unique ID.
        """
        return self.__uid

    def set_uid(self, uid: str) -> None:
        """! Method to get the unique ID of the element.
        The unique ID is a string.

        @param uid the unique ID.
        """
        self.__uid = uid

    def get_dtstart(self) -> datetime:
        """! Method to get the starting time of the element.
        The starting time is a datetime object.

        @return the starting time.
        """
        return self.__dtstart

    def set_dtstart(self, dtstart: datetime) -> None:
        """! Method to set the starting time of the element.
        The starting time is a datetime object.

        @param dtstart the starting time.
        """
        self.__dtstart = dtstart

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

    def get_summary(self) -> str:
        """! Method to get the summary of the element.
        The summary is a string.

        @return the summary.
        """
        return self.__summary

    def set_summary(self, summary: str) -> None:
        """! Method to set the summary of the element.
        The summary is a string.

        @param summary the summary.
        """
        self.__summary = summary

    def get_valarms(self) -> list[VAlarm]:
        """! Method to get the alarms of the event.
        The alarms are objects of type VAlarm.

        @return the list of the alarms of the event.
        """
        return self.__valarms

    def set_valarms(self, valarms: list[VAlarm]) -> None:
        """! Method to set the alarms of the event.
        The alarms are objects of type VAlarm.

        @param valarms the list of the alarms of the event.
        """
        self.__valarms = valarms

    def add_valarm(self, valarm: VAlarm) -> None:
        """! Method to add a valarm to the event.
        The alarms are objects of type VAlarm.

        @param valarm the alarm to add.
        """
        self.__valarms.append(valarm)
