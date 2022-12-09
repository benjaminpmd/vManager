"""! File that includes the class for an phone.
Phones are stored as a list in a VCard. Fore more information, please see VCard.py documentation.

@author Benjamin PAUMARD
@version 1.0.0
@version 25 November 2022
"""

class Phone:
    """! Class that contains the elements of a phone number.
    Phones number are part of a VCard.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @version 25 November 2022
    """

    def __init__(self, phone_types: list[str] = [], phone_number: str = '', preferred: bool = False) -> None:
        """! Class used to store data of a phone.
        This class can store a phone number and its type.

        @param phone_type the type of the phone.
        @param phone_number the phone number to store.
        @param preferential whether the phone is the preferred one.
        """
        self.__phone_types: list[str] = phone_types
        self.__phone_number: str = phone_number
        self.__preferred: bool = preferred

    def __str__(self) -> str:
        """! Override the default __str__ method.
        Allow to see the object as a string.
        
        @return the object as a string."""
        return "PhoneObject: {phone_types=["+(', '.join(self.__phone_types))+"], phone_number="+self.__phone_number+", preferred="+str(self.__preferred)+'}'


    def get_phone_types(self) -> list[str]:
        """! Return the type of the phone.
        This type indicate if the phone is WORK, HOME etc...

        @return the type of the phone.
        """
        return self.__phone_types
    
    def add_phone_type(self, phone_type: str) -> None:
        """! Method to add a phone type.
        The type can be WORK, HOME etc...
        
        @param phone_type the type of the phone.
        """
        self.__phone_types.append(phone_type)

    def get_phone_number(self) -> str:
        """! Return the number of the phone.
        This includes any phone format.

        @return the phone number.
        """
        return self.__phone_number

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    def is_preferred(self) -> bool:
        """! Get a boolean, True whether the number is the preferred one, False otherwise.
        By default, the preferred parameter is at False.
        
        @return boolean if the number is the preferred one.
        """
        return self.__preferred

    def set_preferred(self, preferred) -> None:
        """! Set whether the number is the preferred one.
        By default, the preferred parameter is at False.
        
        @param preferred if the number is the preferred one.
        """
        self.__preferred = preferred