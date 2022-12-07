"""! File that contains the builder of a Calendar.
The builder extract all the informations in an ics file.

@author Benjamin PAUMARD
@version 1.0.0
@since 04 December 2022
"""

# importing the modules
from datetime import datetime
from data.ics.vcalendar import VCalendar
from data.ics.vevent import VEvent
from data.ics.valarm import VAlarm
from data.ics.vrule import VRule
from data.ics.vtodo import VTodo

class VCalendarBuilder:
    """! Class that build a VCalendar object out of an ics file.
    The VCalendar contains all the VEVENT and VTODO elements.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @since 04 December 2022
    """
    def __init__(self) -> None:
        """! Constructor of the VCalendar builder.
        This class can build a VCalendar object out of lines from an ics file.
        """
        pass

    @staticmethod
    def split(line: str) -> list[str]:
        """! Method that split a line into a list.
        The first element will contain the key of the line.
        
        @param line the line to split.
        @return an array of string.
        """
        # elements list will the the line splited with : or ;
        elements: list[str] = ['']
        for char in line:
            # if the char is ; or : append a new element
            if (char == ';') or (char == ':'):
                elements.append('')
            else:
                # else append the element to the last string in the element list
                elements[len(elements)-1] += char
        return elements

    def build(self, lines: list[str]) -> VCalendar:
        """! Method that build a VCalendar object out of lines read from an ICS file.
        The line must not contain \\n at the end of the file.
        
        @param lines the lines of the ICS file.
        @return a VCalendar object.
        """
        vcalendar: VCalendar = VCalendar()
        count: int = len(lines)
        i: int = 0
        
        while i < count:
            data: list[str] = self.split(lines[i])

            if data[0].upper() == "BEGIN":
                match data[1].upper():
                    case "VCALENDAR":
                        i += 1

                    case "VEVENT":

                        vevent = VEvent(datetime.now(), '', datetime.now(), datetime.now())
                        while (i < count and lines[i] != "END:VEVENT"):
                            data = self.split(lines[i])
                            i += 1
                            match data[0].upper():
                                
                                case "UID":
                                    vevent.set_uid(data[1])
                                
                                case "DTSTART":
                                    if (len(data) == 2):
                                        vevent.set_dtstart(datetime.fromisoformat(data[1]))
                                    else:
                                        if( "=" in data[1]):
                                            tz: str = data[1].split('=')[1]
                                            vevent.set_tzstart(tz)
                                        vevent.set_dtstart(datetime.fromisoformat(data[len(data)-1]))
                                
                                case "DTEND":
                                    if (len(data) == 2):
                                        vevent.set_dtend(datetime.fromisoformat(data[1]))
                                    else:
                                        if("=" in data[1]):
                                            tz: str = data[1].split('=')[1]
                                            vevent.set_tzend(tz)
                                        vevent.set_dtend(datetime.fromisoformat(data[len(data)-1]))

                                case "DTSTAMP":
                                    vevent.set_timestamp(datetime.fromisoformat(data[1]))
                                
                                case "SUMMARY":
                                    vevent.set_summary(data[1])

                                case "STATUS":
                                    vevent.set_status(data[1])
                                
                                case "LOCATION":
                                    vevent.set_location(data[1])

                                case "BEGIN:ALARM":
                                    valarm: VAlarm = VAlarm('', '', '')

                                    while (i < count and lines[i] != "END:VALARM"):
                                        
                                        data = self.split(lines[i])
                                        i += 1
                                        
                                        match data[0].upper():
                                            case "TRIGGER":
                                                valarm.set_trigger(data[1])

                                            case "DESCRIPTION":
                                                valarm.set_description(data[1])

                                            case "ACTION":
                                                valarm.set_action(data[1])
                                    
                                    vevent.add_valarm(valarm)
                                    i += 1
                        vcalendar.add_vevent(vevent)
                        i += 1
                    case "VTODO":

                        vtodo = VTodo(datetime.now(), '', datetime.now())
                        while (i < count and lines[i] != "END:VEVENT"):
                            data = self.split(lines[i])
                            i += 1
                            match data[0].upper():
                                
                                case "UID":
                                    vtodo.set_uid(data[1])
                                
                                case "DTSTART":
                                    if (len(data) == 2):
                                        vtodo.set_dtstart(datetime.fromisoformat(data[1]))
                                    else:
                                        if('=' in data[1]):
                                            tz: str = data[1].split('=')[1]
                                            vtodo.set_tzstart(tz)
                                        vtodo.set_dtstart(datetime.fromisoformat(data[len(data)-1]))

                                case "DTSTAMP":
                                    vtodo.set_timestamp(datetime.fromisoformat(data[1]))
                                
                                case "SUMMARY":
                                    vtodo.set_summary(data[1])

                                case "STATUS":
                                    vtodo.set_status(data[1])
                                
                                case "DURATION":
                                    vtodo.set_duration(data[1])

                                case "BEGIN:ALARM":
                                    valarm: VAlarm = VAlarm('', '', '')

                                    while (i < count and lines[i] != "END:VALARM"):
                                        
                                        data = self.split(lines[i])
                                        i += 1
                                        
                                        match data[0].upper():
                                            case "TRIGGER":
                                                valarm.set_trigger(data[1])

                                            case "DESCRIPTION":
                                                valarm.set_description(data[1])

                                            case "ACTION":
                                                valarm.set_action(data[1])
                                    
                                    vtodo.add_valarm(valarm)
                                    i += 1
                        vcalendar.add_vtodo(vtodo)
                        i += 1
                    case other:
                        i+=1
            else:
                i += 1
            

        return vcalendar
        
