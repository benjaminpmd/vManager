class Phone:
    def __init__(self, phone_types: list[str] = [], phone_number: str = '') -> None:
        """! Class used to store data of a phone.
        This class can store a phone number and its type.

        @param phone_type the type of the phone.
        @param phone_number the phone number to store.
        @param preferential whether the phone is the preferred one.
        """
        self.__phone_types: list[str] = phone_types
        self.__phone_number: str = phone_number

    def get_phone_types(self) -> list[str]:
        """! Return the type of the phone.
        This type indicate if the phone is WORK, HOME etc...

        @return the type of the phone.
        """
        return self.__phone_types

    def get_phone_number(self) -> str:
        """! Return the number of the phone.
        This includes any phone format.

        @return the phone number.
        """
        return self.__phone_number

    def add_phone_type(self, phone_type: str) -> None:
        self.__phone_types.append(phone_type)

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number
