"""! File containing the class to store a rule used in a event.
Rules are stored in events. Fore more information, please see vevent.py documentation.

@author Benjamin PAUMARD
@version 1.0.0
@version 03 December 2022
"""

class RRule:
    """! Class that contains the elements of a rule.
    Rules are part of an event.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @version 03 December 2022
    """
    
    def __init__(self, frequency: str = '', until: str = '') -> None:
        """! Constructor of the class containing a recurrence rule for an event.
        An event can contain multiple rules.
        
        @param frequency the frequency of the event.
        @param until the date of end.
        """
        # setting attributes
        self.__frequency: str = frequency
        self.__until: str = until

    def get_frequency(self) -> str:
        """! Method to get the frequency.
        It must is like DAILY for example.
        
        @return the frequency of the recurrence rule.
        """
        return self.__frequency

    def set_frequency(self, frequency: str) -> None:
        """! Method to set the frequency.
        It must be like DAILY for example.
        
        @param frequency of the rule to use.
        """
        self.__frequency = frequency

    def get_until(self) -> str:
        """! Method to get the until time.
        This time represent when the rule will end.
        
        @return the end date of the rule.
        """
        return self.__until

    def set_until(self, until: str) -> None:
        """! Method to set the until time.
        This time represent when the rule will end.
        
        @param until time of the rule to use.
        """
        self.__until = until
