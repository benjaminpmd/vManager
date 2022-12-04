"""! File containing the class that manage a VCalendar.
Everything contained in an ics file can be managed from this class.

@author Benjamin PAUMARD
@version 1.0.0
@version 03 December 2022
"""
from ics.data.vevent import VEvent
from ics.data.vtodo import VTodo
from ics.vcalendar import VCalendar
from ics.vcalendar_builder import VCalendarBuilder

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
        # if the path is not empty read the file
        if path != '':
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

    def export_csv(self, output_path: str) -> None:
        """! Method that export a calendar into a CSV."""
        with open(output_path, 'w') as f:
            self.__vcalendar.export_csv(f)


    def export_html(self, output_path: str) -> None:
        """! Method that export a calendar into a HTML file."""
        with open(output_path, 'w') as f:
            self.__vcalendar.export_html(f)

            
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
            

            