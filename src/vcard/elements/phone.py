class Phone:
    def __init__(self, phone_type: str = '', phone_number: str = '', preferential: bool = False) -> None:
        """! Class used to store data of a phone.
        This class can store a phone number and its type, plus whether the phone number is preferential or not.

        @param phone_type the type of the phone.
        @param phone_number the phone number to store.
        @param preferential whether the phone is the preferred one.
        """
        self.__phone_type: str = phone_type
        self.__phone_number: str = phone_number
        self.__preferential: bool = preferential

    def get_phone_type(self) -> str:
        """! Return the type of the phone.
        This type indicate if the phone is WORK, HOME etc...

        @return the type of the phone.
        """
        return self.__phone_type

    def get_phone_number(self) -> str:
        """! Return the number of the phone.
        This includes any phone format.

        @return the phone number.
        """
        return self.__phone_number

    def is_preferential(self) -> bool:
        """! Returns whether the phone is preferential or not.
        It means that it's the default phone number.

        @return whether the phone is preferential or not.
        """
        return self.__preferential

    def set_phone_type(self, phone_type: str) -> None:
        self.__phone_type = phone_type

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    def set_preferential(self, preferential: bool) -> None:
        self.__preferential = preferential
