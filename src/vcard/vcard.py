from email import Email
from phone import Phone

class VCard:
    def __init__(self) -> None:
        self.name: list[str] = []
        self.full_name: str = ''
        self.org: str = ''
        self.title: str = ''
        self.emails: list[Email] = []
        self.tels: list[Phone] = []
        self.note: str = ''
        self.categories: str[str] = []
