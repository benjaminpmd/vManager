"""! File containing the class to store an alarm.
Alarm are stored as a list in a VEvent. Fore more information, please see vevent.py documentation.

@author Benjamin PAUMARD
@version 1.0.0
@version 25 November 2022
"""

class VAlarm:
    """! Class that contains the elements of an alarm.
    Alarms are part of a VEvent.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @version 25 November 2022
    """
    
    def __init__(self, trigger: str, description: str, action: str) -> None:
        """! Class used to store data of an alarm.
        This class contains data from an alarm.

        @param trigger the time when the alarm if fired.
        @param description a short summary to describe the alarm.
        @param action the action that is made when firing the alarm.
        """
        self.__trigger: str = trigger
        self.__description: str = description
        self.__action: str = action

    def get_trigger(self) -> str:
        """! Method to get the trigger.
        It must is like -PT10PM for example.
        
        @return the trigger of the alarm.
        """
        return self.__trigger

    def set_trigger(self, trigger: str) -> None:
        """! Method to set the trigger.
        It must be like -PT10PM for example.
        
        @param trigger the trigger to use.
        """
        self.__trigger = trigger

    def get_description(self) -> str:
        """! Method to get the description.
        It is a short summary of the alarm.
        
        @return the description of the alarm.
        """
        return self.__description

    def set_description(self, description: str) -> None:
        """! Method to set the description.
        It is a short summary of the alarm.
        
        @param description the description to use.
        """
        self.__description = description

    def get_action(self) -> str:
        """! Method to get the action.
        It must is like DISPLAY for example.
        
        @return the action of the alarm.
        """
        return self.__action

    def set_action(self, action: str) -> None:
        """! Method to set the action.
        It must be like DISPLAY for example.
        
        @param action the action to use.
        """
        self.__action = action
