class Email:
    def __init__(self, type: str = '', email: str = '', preferential: bool = False) -> None:
        self.__type: str = type
        self.__email: str = email
        self.__preferential: bool = preferential

    def get_type(self) -> str:
        return self.__type

    def get_email(self) -> str:
        return self.__email

    def is_preferential(self) -> bool:
        return self.__preferential

    def set_type(self, type: str) -> None:
        self.__type = type

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_preferential(self, preferential: bool) -> None:
        self.__preferential = preferential