"""! File containing the class that manage a VCalendar.
Everything contained in an ics file can be managed from this class.

@author Benjamin PAUMARD
@version 1.0.0
@version 03 December 2022
"""
from datetime import datetime
from data.ics.vevent import VEvent
from data.ics.vtodo import VTodo
from data.ics.vcalendar import VCalendar
from builder.vcalendar_builder import VCalendarBuilder

class ICSManager:
    """! Class that the main manager of an ICS file.
    Everything contained in an ics file can be managed from this class.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @version 03 December 2022
    """

    def __init__(self, path: str = '') -> None:
        """! Constructor of the ICSManager.
        All data from an ICS file are managed by this class.
        
        @param path the path of the file to read.
        """

        # init the values
        self.__builder: VCalendarBuilder = VCalendarBuilder()
        self.__vcalendar: VCalendar = VCalendar()
        self.__path: str = ''
        self.__current_event_index: int = -1
        self.__current_todo_index: int = -1
        # if the path is not empty read the file
        if path != '':
            self.__path = path
            self.read(path)
            
    def get_vevents(self) -> list[VEvent]:
        """! Method to get the list of events of the calendar.
        The events have their own type: VEvent.

        @return a list of VEvent.
        """
        return self.__vcalendar.get_vevents()

    def get_event_from_summary(self, summary: str) -> VEvent | None:
        """! Returns a VEvent from a given summary.
        In the case the event does not exist, return None.
        
        @param summary the event summary.
        @return the VEvent corresponding"""
        for i in range(len(self.get_vevents())):
            # check for each event if the summary is the same
            if (self.get_vevents()[i].get_summary() == summary):
                self.__current_event_index = i
                return self.get_vevents()[i]
        return None

    def update_current_event(self, summary: str, dtstart: datetime, dtend: datetime, location: str):
        """! Updating the event that was selected using the get_event_from_summary method.
        Only this method can update the current selected event.
        
        @param summary the summary to set.
        @param dtsart the ew date to use for start.
        @param dtend the ending date of the event.
        @param location the location of the event.
        """
        # update the element
        self.get_vevents()[self.__current_event_index].set_summary(summary)
        self.get_vevents()[self.__current_event_index].set_dtstart(dtstart)
        self.get_vevents()[self.__current_event_index].set_dtend(dtend)
        self.get_vevents()[self.__current_event_index].set_location(location)
        # save the file
        self.save()


    def get_vtodos(self) -> list[VTodo]:
        """! Method to get the list of events of the calendar.
        The events have their own type: VTodo.

        @return a list of VTodo.
        """
        return self.__vcalendar.get_vtodos()

    def get_todo_from_summary(self, summary: str) -> VTodo | None:
        """! Returns a VEvent from a given summary.
        In the case the event does not exist, return None.
        
        @param summary the event summary.
        @return the VEvent corresponding.
        """
        for i in range(len(self.get_vtodos())):
            # check for each event if the summary is the same
            if (self.get_vtodos()[i].get_summary() == summary):
                self.__current_todo_index = i
                return self.get_vtodos()[i]
        return None

    def update_current_todo(self, summary: str, dtstart: datetime, duration: str, status: str):
        """! Updating the todo that was selected using the get_todo_from_summary method.
        Only this method can update the current selected todo.
        
        @param summary the summary to set.
        @param dtsart the ew date to use for start.
        @param duration the ending date of the tdo.
        @param status the status of the todo.
        """
        # update the element
        self.get_vtodos()[self.__current_todo_index].set_summary(summary)
        self.get_vtodos()[self.__current_todo_index].set_dtstart(dtstart)
        self.get_vtodos()[self.__current_todo_index].set_duration(duration)
        self.get_vtodos()[self.__current_todo_index].set_status(status)
        # save the file
        self.save()

    def get_path(self) -> str:
        """! Method to get the path of the opened file.
        The path can be used by default if no path is provided to save method.
        
        @return the path of the opened file.
        """
        return self.__path

    def set_path(self, path: str) -> None:
        """! Method to set the path of the opened file.
        The path can be used by default if no path is provided to save method.
        
        @param path the path of the opened file.
        """
        self.__path = path
        
    def read(self, path: str) -> None:
        """! Open a vcf file and extract all VCards contained inside.
        The vcf file can contain multiple VCards from different versions.
        To get the cards that have been read, please use get_cards method.

        @param path the path of the file to read.
        """
        # reset the content of the calendar
        self.__vcalendar.get_vevents().clear()
        self.__vcalendar.get_vtodos().clear()
        # open the file
        with open(path, 'r') as f:
            
            # init the lines of the vcard
            lines: list[str] = []

            # read each line of the file
            for line in f:
                # replace return to line with empty string
                line = line.replace("\n", '')
                lines.append(line)

        self.__vcalendar = self.__builder.build(lines)
        self.__path = path

    def import_from_file(self, path: str) -> None:
        """! Method that set the calendar out of a HTML or CSV file.
        Only some elements will be retrieved from the file.
        
        @param path the path of the file to import.
        """
        # reset the calendar
        self.__vcalendar.get_vevents().clear()
        self.__vcalendar.get_vtodos().clear()

        with open(path, 'r') as f:

            # if the opened file is an HTML file
            if path.endswith(".html"):

                # init the lines of the vcard
                lines: list[str] = []
                # read each line of the file
                for line in f:
                    # replace return to line with empty string
                    line = line.replace("\n", '')
                    line = line.replace("	", '')
                    line = line.replace("        ", '')
                    line = line.replace("    ", '')
                    lines.append(line)

                # build calendar
                self.__vcalendar = self.__builder.build_from_html(lines)
            
            # if the opened file is an HTML file
            elif path.endswith(".csv"):

                # init the lines of the vcard
                lines: list[str] = []
                
                # read each line of the file
                for line in f:
                    
                    # replace return to line with empty string
                    line = line.replace("\n", '')
                    
                    # append if not the header line
                    if not line.startswith("type"):
                        lines.append(line)
                
                # build the calendar
                self.__vcalendar = self.__builder.build_from_csv(lines)

    def save(self, path: str = '') -> None:
        """! Save all the contained contact into an ics file.
        All the VEvent and VTodo the calendar contains will be saved inside.

        @param path the path of the file to store.
        """
        # if no path is provided, then save it in the original file
        if path == '':
            path = self.__path

        # save the file
        with open(path, 'w') as f:
            self.__vcalendar.save(f)

    def export_csv(self, output_path: str) -> None:
        """! Method that export a calendar into a CSV file.
        This method will export only some elements.
        
        @param path the path of the file to store.
        """
        with open(output_path, 'w') as f:
            self.__vcalendar.export_csv(f)

    def export_html(self, path: str, complete: bool = False) -> None:
        """! Method that export a calendar into a HTML file.
        This method will export only some elements.
        
        @param path the path of the file to store.
        @param complete a boolean indicating if the page must be completed rendered.
        """
        
        # open the file
        with open(path, 'w') as f:
            f.write("<!--vcalendar_export-->\n")
            if (complete):
                # if complete page write the beginning
                f.write("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n\t<title>Exported Calendar</title>\n</head>\n<body>\n")

            self.__vcalendar.export_html(f)

            if (complete):
                f.write("</body>\n</html>\n")
            

            