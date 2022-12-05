"""! File that includes the class for an email.
Emails are stored as a list in a VCard. Fore more information, please see VCard.py documentation.

@author Benjamin PAUMARD
@version 1.0.0
@version 25 November 2022
"""

class Email:
    """! Class that contains the elements of an email.
    Emails are part of a VCard.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @version 25 November 2022
    """

    def __init__(self, email_types: list[str] = [], email_address: str = '', preferred: bool = False) -> None:
        """! Class used to store data of an email.
        This class can store an email and its types.

        @param email_type the types of the email.
        @param email_address the email to store.
        @param preferred whether the email is the preferred one.
        """
        self.__email_types: list[str] = email_types
        self.__email_address: str = email_address
        self.__preferred: bool = preferred

    def __str__(self) -> str:
        """! Override the default __str__ method.
        Allow to see the object as a string.
        
        @return the object as a string."""
        return "EmailObject: {email_types=["+(', '.join(self.__email_types))+"], email_address="+self.__email_address+", preferred="+str(self.__preferred)+'}'

    def get_email_types(self) -> list[str]:
        """! Return the types of the email.
        This types indicates if the email is WORK, HOME etc...

        @return the types of the email.
        """
        return self.__email_types

    def add_email_type(self, email_type: str) -> None:
        """! Method to add an email type.
        The type can be WORK, HOME etc...
        
        @param email_type the type of the email.
        """
        self.__email_types.append(email_type)

    def get_email_address(self) -> str:
        """! Return the email address.
        The email address is in a unique string.

        @return the email address.
        """
        return self.__email_address

    def set_email_address(self, email_address: str) -> None:
        """! Method to set the email address.
        The email is a unique string.
        
        @param email_address  the email address.
        """
        self.__email_address = email_address

    def is_preferred(self) -> bool:
        """! Get a boolean, True whether the email is the preferred one, False otherwise.
        By default, the preferred parameter is at False.
        
        @return boolean if the email is the preferred one.
        """
        return self.__preferred

    def set_preferred(self, preferred) -> None:
        """! Set whether the email is the preferred one.
        By default, the preferred parameter is at False.
        
        @param preferred if the email is the preferred one.
        """
        self.__preferred = preferred