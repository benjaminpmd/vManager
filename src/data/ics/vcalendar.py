"""! File containing the class where the vcalendar data are stored.
This file does not manage or build vcalendar.

@author Benjamin PAUMARD
@version 1.0.0
@since 04 December 2022
"""

# importing elements used in the VCalendar
from data.ics.vevent import VEvent
from data.ics.vtodo import VTodo


class VCalendar:
    """! Class that contains the elements of a calendar.
    All the events, alarms etc are stored in this class in the form of objects.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @since 04 December 2022
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
        """! Method that returns the events of the calendar.
        Only events will be returned, in VEvent objects.
        
        @return a list of VEvent objects.
        """
        return self.__vevents

    def set_vevents(self, vevents: list[VEvent]) -> None:
        """! Method that set the events of the calendar.
        Only events will be set as VEvent objects.
        
        @param vevents a list of VEvent objects.
        """
        self.__vevents = vevents

    def add_vevent(self, vevent: VEvent) -> None:
        """! Add a vevent to the VCalendar.
        All the events of an ics file are listed in the calendar.
        
        @param vevent the event to add.
        """
        self.__vevents.append(vevent)

    def get_vtodos(self) -> list[VTodo]:
        """! Method that returns the events of the calendar.
        Only events will be returned, in vtodo objects.
        
        @return a list of vtodo objects.
        """
        return self.__vtodos

    def set_vtodos(self, vtodos: list[VTodo]) -> None:
        """! Method that set the events of the calendar.
        Only events will be set as vtodo objects.
        
        @param vtodos a list of vtodo objects.
        """
        self.__vtodos = vtodos

    def add_vtodo(self, vtodo: VTodo) -> None:
        """! Add a vtodo to the VCalendar.
        All the events of an ics file are listed in the calendar.
        
        @param vtodo the todo to add.
        """
        self.__vtodos.append(vtodo)

    def save(self, f) -> None:
        """! Method to save a calendar into a file.
        All events will be automatically saved.
        
        @param f the file wrapper, it must be opened as 'w' or at least 'a'.
        """
        # write the beginning of the file
        f.write("BEGIN:VCALENDAR\n")
        f.write(f"VERSION:2.0\n")
        f.write(f"PRODID:-//XYZproduct//EN\n")

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


    