"""! File containing the class that manage a VCalendar.
Everything contained in an ics file can be managed from this class.

@author Benjamin PAUMARD
@version 1.0.0
@version 03 December 2022
"""
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

    def get_vtodos(self) -> list[VTodo]:
        """! Method to get the list of events of the calendar.
        The events have their own type: VTodo.

        @return a list of VTodo.
        """
        return self.__vcalendar.get_vtodos()

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

    def save(self, path: str = '') -> None:
        """! Save all the contained contact into an ics file.
        All the VEvent and VTodo the calendar contains will be saved inside.

        @param path the path of the file to store.
        """
        # if no path is provided, then save it in the original file
        if path == '':
            path = self.__path

        with open(path, 'w') as f:
            self.__vcalendar.save(f)

    def export_csv(self, output_path: str) -> None:
        """! Method that export a calendar into a CSV file.
        
        @param path the path of the file to store.
        """
        with open(output_path, 'w') as f:
            self.__vcalendar.export_csv(f)

    def export_html(self, path: str, complete: bool = False) -> None:
        """! Method that export a calendar into a HTML file.
        
        @param path the path of the file to store.
        @param complete a boolean indicating if the page must be completed rendered.
        """
        
        with open(path, 'w') as f:
            if (complete):
                f.write("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n\t<title>Exported Calendar</title>\n</head>\n<body>\n")

            self.__vcalendar.export_html(f)

            if (complete):
                f.write("</body>\n</html>\n")
            

            