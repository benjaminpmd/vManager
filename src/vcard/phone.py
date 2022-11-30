class Phone:
    def __init__(self, type: str = '', phone: str = '', preferential: bool = False) -> None:
        self.__type: str = type
        self.__phone: str = phone
        self.__preferential: bool = preferential

    def get_type(self) -> str:
        return self.__type

    def get_phone(self) -> str:
        return self.__phone

    def is_preferential(self) -> bool:
        return self.__preferential

    def set_type(self, type: str) -> None:
        self.__type = type

    def set_phone(self, phone: str) -> None:
        self.__phone = phone

    def set_preferential(self, preferential: bool) -> None:
        self.__preferential = preferential