"""! File containing the class where the vcalendar data are stored.
This file does not manage or build vcalendar.

@author Benjamin PAUMARD
@version 1.0.0
@since 04 December 2022
"""

# importing elements used in the VCalendar
from ics.data.vevent import VEvent
from ics.data.vtodo import VTodo


class VCalendar:
    """! Class that contains the elements of a calendar.
    All the events, alarms etc are stored in this class in the form of objects.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @version 25 November 2022
    """
    
    def __init__(self, vevents: list[VEvent] = [], vtodos: list[VTodo] = []) -> None:
        """! Constructor of a VCalendar.
        All the events are stored inside this class.

        @param vevents list of events (optional).
        @param vtodos list of todos (optional).
        """
        self.__vevents: list[VEvent] = vevents
        self.__vtodos: list[VTodo] = vtodos

    def __str__(self) -> str:
        """! Method that returns the object as a string.
        All of the data is stored in a string and returned.

        @return a string containing the object.
        """
        string: str = "VCalendarObject={events=["
        for vevent in self.__vevents:
            string += str(vevent)
        string += "]}"
        return string

    def get_vevents(self) -> list[VEvent]:
        return self.__vevents

    def set_vevents(self, vevents: list[VEvent]) -> None:
        self.__vevents = vevents

    def add_vevent(self, vevent: VEvent) -> None:
        """! Add a VEvent to the VCalendar.
        All the events of an ics file are listed in the calendar.
        
        @param vevent the event to add.
        """
        self.__vevents.append(vevent)

    def save(self, f) -> None:
        """! Method to save a calendar into a file.
        All events will be automatically saved.
        
        @param f the file wrapper, it must be opened as 'w' or at least 'a'.
        """
        # write the beginning of the file
        f.write("BEGIN:VCALENDAR\n")
        f.write(f"VERSION:2.0\n")

        # for each vevent, write it
        for vevent in self.__vevents:
            vevent.save(f)

        # for each vevent, write it
        for vtodos in self.__vtodos:
            vtodos.save(f)

        f.write("END:VCALENDAR\n")

    def export_csv(self, f) -> None:
        """! Method to save a calendar into a CSV format.
        All events will be automatically saved.
        
        @param f the file wrapper, it must be opened as 'w' or at least 'a'.
        """
        # write the beginning of the file
        f.write("type,timestamp,uid,summary,dtstart,status\n")

        # for each vevent, write it
        for vevent in self.__vevents:
            vevent.export_csv(f)

        # for each vtodos, write it
        for vtodo in self.__vtodos:
            vtodo.export_csv(f)
    
    def export_html(self, f) -> None:
        """! Method to save a calendar into a HTML format.
        All events will be automatically saved.
        
        @param f the file wrapper, it must be opened as 'w' or at least 'a'.
        """
        # for each vevent, write it
        for vevent in self.__vevents:
            vevent.export_html(f)

        # for each vtodos, write it
        for vtodo in self.__vtodos:
            vtodo.export_html(f)


    