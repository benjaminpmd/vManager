class Email:
    def __init__(self, email_type: str = '', email_address: str = '') -> None:
        """! Class used to store data of a phone.
        This class can store a phone number and its type.

        @param email_type the type of the phone.
        @param email_address the phone number to store.
        @param preferential whether the phone is the preferred one.
        """
        self.__email_type: str = email_type
        self.__email_address: str = email_address

    def get_email_type(self) -> str:
        """! Return the type of the phone.
        This type indicate if the phone is WORK, HOME etc...

        @return the type of the phone.
        """
        return self.__email_type

    def get_email_address(self) -> str:
        """! Return the number of the phone.
        This includes any phone format.

        @return the phone number.
        """
        return self.__email_address

    def set_email_type(self, email_type: str) -> None:
        self.__email_type = email_type

    def set_email_address(self, email_address: str) -> None:
        self.__email_address = email_address