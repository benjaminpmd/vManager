"""! File that contains the builder of a Calendar.
The builder extract all the informations in an ics file.
Methods to extract calendar from html and csv files are also available.

@author Benjamin PAUMARD
@version 1.0.0
@since 25 November 2022
"""

# importing the modules
from datetime import datetime
from data.ics.vcalendar import VCalendar
from data.ics.vevent import VEvent
from data.ics.valarm import VAlarm
from data.ics.rrule import RRule
from data.ics.vtodo import VTodo

class VCalendarBuilder:
    """! Class that build a VCalendar object out of an ics file.
    The VCalendar contains all the VEVENT and VTODO elements.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @since 25 November 2022
    """
    def __init__(self) -> None:
        """! Constructor of the VCalendar builder.
        This class can build a VCalendar object out of lines from an ics file.
        Methods to extract calendar from html and csv files are also available.
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
        
        # return the elements of the line
        return elements

    def build(self, lines: list[str]) -> VCalendar:
        """! Method that build a VCalendar object out of lines read from an ICS file.
        The line must not contain \\n at the end of the file.
        
        @param lines the lines of the ICS file.
        @return a VCalendar object.
        """

        # init the calendar to return
        vcalendar: VCalendar = VCalendar()

        # set the number of lines
        count: int = len(lines)

        # create the iteration index
        i: int = 0
        
        # while index is lower than the number of lines
        while i < count:

            # split the line into elements
            data: list[str] = self.split(lines[i])

            # if first element is the beginning of something
            if data[0].upper() == "BEGIN":

                # match the starting element
                match data[1].upper():
                    
                    # case where the calendar is starting, increment the index
                    case "VCALENDAR":
                        i += 1

                    # case where an event starts
                    case "VEVENT":
                        
                        # create an empty event
                        vevent = VEvent(datetime.now(), '', datetime.now(), datetime.now())
                        
                        # while the line does not indicate the end of an event and the index is not over the number of line
                        while (i < count and lines[i] != "END:VEVENT"):
                            
                            # split the line into elements
                            data = self.split(lines[i])
                            
                            # increment for next iteration
                            i += 1

                            # match the data key of the line
                            match data[0].upper():
                                
                                # case where this is the UID of the event
                                case "UID":
                                    vevent.set_uid(data[1])
                                
                                # case where this is the start date of the event
                                case "DTSTART":
                                    # if the len of data is 2, it means no time zone is present
                                    if (len(data) == 2):
                                        vevent.set_dtstart(datetime.fromisoformat(data[1]))
                                    
                                    # else, there is a timezone to save
                                    else:
                                        # if the timezone is correctly formatted, save it
                                        if( "=" in data[1]):
                                            tz: str = data[1].split('=')[1]
                                            vevent.set_tzstart(tz)
                                        
                                        # save the last item of the data as the date
                                        vevent.set_dtstart(datetime.fromisoformat(data[len(data)-1]))
                                
                                # case where this is the end date of the event
                                case "DTEND":

                                    # if the len of data is 2, it means no time zone is present
                                    if (len(data) == 2):
                                        vevent.set_dtend(datetime.fromisoformat(data[1]))
                                    
                                    # else, there is a timezone to save
                                    else:
                                        # if the timezone is correctly formatted, save it
                                        if("=" in data[1]):
                                            tz: str = data[1].split('=')[1]
                                            vevent.set_tzend(tz)

                                        # save the last item of the data as the date
                                        vevent.set_dtend(datetime.fromisoformat(data[len(data)-1]))

                                # case where this is the creation date of the event
                                case "DTSTAMP":
                                    vevent.set_timestamp(datetime.fromisoformat(data[1]))
                                
                                # case where this is the summary of the event
                                case "SUMMARY":
                                    vevent.set_summary(data[1])

                                # case where this is the status of the event
                                case "STATUS":
                                    vevent.set_status(data[1])
                                
                                # case where this is the location of the event
                                case "LOCATION":
                                    vevent.set_location(data[1])

                                # case where this is a recursion rule of the event
                                case "RRULE":
                                    # split to get the frequency
                                    freq: str = data[1].split('=')[1]
                                    
                                    # get the until time of the event
                                    until: str = ''
                                    if len(data) > 2:
                                        until = data[2].split('=')[1]
                                    
                                    # add the rule to the event
                                    vevent.add_rrule(RRule(freq, until))                                    
                                         
                                # case where this is an alarm for the event
                                case "BEGIN:ALARM":

                                    # create an empty alarm
                                    valarm: VAlarm = VAlarm('', '', '')
                                    
                                    # while it is not the end of the alarm
                                    while (i < count and lines[i] != "END:VALARM"):
                                        
                                        # split the line
                                        data = self.split(lines[i])
                                        
                                        #increment
                                        i += 1
                                        
                                        # match the data key of the line
                                        match data[0].upper():

                                            # case where the line is the trigger of the alarm
                                            case "TRIGGER":
                                                valarm.set_trigger(data[1])

                                            # case where the line is the description of the alarm
                                            case "DESCRIPTION":
                                                valarm.set_description(data[1])

                                            # case where the line is the action of the alarm
                                            case "ACTION":
                                                valarm.set_action(data[1])
                                    
                                    # add the alarm to the event
                                    vevent.add_valarm(valarm)

                                    # increment
                                    i += 1
                        # once read, append the event to the calendar
                        vcalendar.add_vevent(vevent)
                        
                        # increment
                        i += 1

                    # case where a TODO starts
                    case "VTODO":
                        
                        # create a VTodo object
                        vtodo = VTodo(datetime.now(), '', datetime.now())

                        # while the vtodo is not complete
                        while (i < count and lines[i] != "END:VTODO"):

                            # split the line into elements
                            data: list[str] = self.split(lines[i])
                            
                            # increment
                            i += 1

                            # match the first element of the line
                            match data[0].upper():
                                
                                # case where this is the UID of the todo
                                case "UID":
                                    vtodo.set_uid(data[1])
                                
                                # case where this is the start date of the event
                                case "DTSTART":

                                    # if the len of data is 2, it means no time zone is present
                                    if (len(data) == 2):
                                        vtodo.set_dtstart(datetime.fromisoformat(data[1]))
                                    
                                    # else, there is a timezone to save
                                    else:
                                        # if the timezone is correctly formatted, save it
                                        if('=' in data[1]):
                                            tz: str = data[1].split('=')[1]
                                            vtodo.set_tzstart(tz)
                                        
                                        # save the last item of the data as the date
                                        vtodo.set_dtstart(datetime.fromisoformat(data[len(data)-1]))

                                # case where this is the creation date of the event
                                case "DTSTAMP":
                                    vtodo.set_timestamp(datetime.fromisoformat(data[1]))
                                
                                # case where this is the summary of the todo
                                case "SUMMARY":
                                    vtodo.set_summary(data[1])

                                # case where this is the status of the todo
                                case "STATUS":
                                    vtodo.set_status(data[1])
                                
                                # case where this is the duration of the todo
                                case "DURATION":
                                    vtodo.set_duration(data[1])

                                # case where this is the status of the todo
                                case "BEGIN:ALARM":
                                    valarm: VAlarm = VAlarm('', '', '')

                                    while (i < count and lines[i] != "END:VALARM"):
                                        
                                        # split the line
                                        data = self.split(lines[i])
                                        
                                        # increment
                                        i += 1
                                        
                                        # match the data key of the line
                                        match data[0].upper():

                                            # case where the line is the trigger of the alarm
                                            case "TRIGGER":
                                                valarm.set_trigger(data[1])

                                            # case where the line is the description of the alarm
                                            case "DESCRIPTION":
                                                valarm.set_description(data[1])

                                            # case where the line is the action of the alarm
                                            case "ACTION":
                                                valarm.set_action(data[1])
                                    
                                    # add the alarm to the todo
                                    vtodo.add_valarm(valarm)

                                    # increment
                                    i += 1
                        # add the todo to the calendar
                        vcalendar.add_vtodo(vtodo)

                        # increment
                        i += 1
                    
                    # in case something else is starting
                    # futur support for more data maybe added here
                    case other:
                        i+=1
            # increment
            else:
                i += 1

        # return the calendar
        return vcalendar


    def build_from_csv(self, lines: list[str]) -> VCalendar:
        """! Method that build a VCalendar object out of lines read from a CSV file.
        The line must not contain \\n at the end of the file.
        
        @param lines the lines of the CSV file.
        @return a VCalendar object.
        """

        # create the calendar to return
        vcalendar: VCalendar = VCalendar()
        
        # for each line
        for line in lines:

            # split the line
            data: list[str] = line.split(',')

            # it is a vevent, create it and add it to the events
            if data[0] == 'vevent':
                event: VEvent = VEvent(datetime.fromisoformat(data[1]), data[2], datetime.fromisoformat(data[4]), datetime.fromisoformat(data[4]), summary=data[3], status=data[5])
                vcalendar.add_vevent(event)

            # it is a vtodo, create it and add it to the todos
            elif data[0] == 'vtodo':
                todo: VTodo = VTodo(datetime.fromisoformat(data[1]), data[2], datetime.fromisoformat(data[4]), summary=data[3], status=data[5])
                vcalendar.add_vtodo(todo)

        # return the calendar
        return vcalendar

    def build_from_html(self, lines: list[str]) -> VCalendar:
        """! Method that build a VCalendar object out of lines read from a CSV file.
        The line must not contain \\n at the end of the file.
        
        @param lines the lines of the CSV file.
        @return a VCalendar object.
        """
        # init the calendar to return
        vcalendar: VCalendar = VCalendar()

        # set the number of lines
        count: int = len(lines)

        # create the iteration index
        i: int = 0
        
        # while index is lower than the number of lines
        while i < count:

            # get the line
            line: str = lines[i]

            # check if line start with the vevent beginning
            if line.startswith("<div class=\"vevent\">"):

                # create the VEvent object
                vevent = VEvent(datetime.now(), '', datetime.now(), datetime.now())
                
                # while the line is not the end of the div
                while not line.startswith("</div>"):

                    # get the line
                    line: str = lines[i]

                    # line is the starting date of the event
                    if line.startswith("<abbr class=\"dtstart\""):
                        line = line[46:]
                        line = line.replace("</abbr>", '')
                        vevent.set_dtstart(datetime.fromisoformat(line))

                    # line is the ending date of the event
                    elif line.startswith("<abbr class=\"dtend\""):
                        line = line[44:]
                        line = line.replace("</abbr>", '')
                        vevent.set_dtend(datetime.fromisoformat(line))
                    
                    # line is the summary of the event
                    elif line.startswith("<div class=\"summary\">"):
                        line = line.replace("<div class=\"summary\">", '')
                        line = line.replace("</div>", '')
                        vevent.set_summary(line)

                    # line is the location of the event
                    elif line.startswith("<div class=\"location\">"):
                        line = line.replace("<div class=\"location\">", '')
                        line = line.replace("</div>", '')
                        vevent.set_location(line)

                    # line is the status of the event
                    elif line.startswith("<div class=\"status\">"):
                        line = line.replace("<div class=\"status\">", '')
                        line = line.replace("</div>", '')
                        vevent.set_status(line)
                    
                    # increment
                    i += 1

                # add the event
                vcalendar.add_vevent(vevent)

            # while index is lower than the number of lines
            elif line.startswith("<div class=\"vtodo\">"):

                # create the VObject object
                vtodo = VTodo(datetime.now(), '', datetime.now())

                # while the line is not the end of the div
                while not line.startswith("</div>"):

                    # get the line
                    line: str = lines[i]

                    # line is the starting date of the todo
                    if line.startswith("<abbr class=\"dtstart\">"):
                        line = line[46:]
                        line = line.replace("</abbr>", '')
                        vtodo.set_dtstart(datetime.fromisoformat(line))
                    
                    # line is the summary of the todo
                    elif line.startswith("<div class=\"summary\">"):
                        line = line.replace("<div class=\"summary\">", '')
                        line = line.replace("</div>", '')
                        vtodo.set_summary(line)

                    # line is the duration of the todo
                    elif line.startswith("<div class=\"duration\">"):
                        line = line.replace("<div class=\"duration\">", '')
                        line = line.replace("</div>", '')
                        vtodo.set_duration(line)

                    # line is the status of the todo
                    elif line.startswith("<div class=\"status\">"):
                        line = line.replace("<div class=\"status\">", '')
                        line = line.replace("</div>", '')
                        vtodo.set_status(line)

                    # increment
                    i += 1
                # add the todo
                vcalendar.add_vtodo(vtodo)
            
            else:
                # increment
                i += 1
        
        # return the calendar
        return vcalendar
