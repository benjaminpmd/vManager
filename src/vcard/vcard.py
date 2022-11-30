from vcard.elements.email import Email
from vcard.elements.phone import Phone
from vcard.elements.address import Address


class VCard:
    def __init__(self) -> None:
        self.__names: list[str] = []
        self.__full_name: str = ''
        self.__org: list[str] = []
        self.__title: str = ''
        self.__addresses: list[Address] = []
        self.__emails: list[Email] = []
        self.__phones: list[Phone] = []
        self.__note: str = ''
        self.__categories: list[str] = []
    
    def __str__(self) -> str:
        return f"[names = {self.__names}, \nfull_name = {self.__full_name}, \norg = {self.__org}, \ntitle = {self.__title}, \naddresses = {self.__addresses}, \nemails = {self.__emails} \nphones = {self.__phones} \nnote = {self.__note} \ncategories = {self.__categories}]"

    def get_names(self) -> list[str]:
        return self.__names

    def add_name(self, name) -> None:
        self.__names.append(name)

    def get_full_name(self) -> str:
        return self.__full_name

    def set_full_name(self, full_name: str) -> None:
        self.__full_name = full_name 

    def get_org(self) -> list[str]:
        return self.__org

    def add_org(self, org: str) -> None:
        self.__org.append(org) 

    def get_title(self) -> str:
        return self.__title
    
    def set_title(self, title: str) -> None:
        self.__title = title 

    def get_addresses(self) -> list[Address]:
        return self.__addresses

    def add_address(self, address: Address) -> None:
        self.__addresses.append(address)

    def get_emails(self) -> list[Email]:
        return self.__emails

    def add_email(self, email: Email) -> None:
        self.__emails.append(email)

    def get_phones(self) -> list[Phone]:
        return self.__phones
    
    def set_phones(self, phone: Phone) -> None:
        self.__phones.append(phone)

    def get_note(self) -> str:
        return self.__note

    def set_note(self, note: str) -> None:
        self.__note = note 

    def get_categories(self) -> list[str]:
        return self.__categories

    def add_category(self, category: str) -> None:
        self.__categories.append(category)
