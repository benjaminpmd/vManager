"""! File containing the class where the vcard element is stored.
All elements of a vcard is saved in this class.

@author Benjamin PAUMARD
@version 1.0.0
@since 25 November 2022
"""
# importing elements used in the VCard
from data.vcf.email import Email
from data.vcf.phone import Phone
from data.vcf.address import Address


class VCard:
    """! Class containing all the elements of a VCard.
    All elements of a vcard is saved in this class.

    @author Benjamin PAUMARD
    @version 1.0.0
    @since 25 November 2022
    """

    def __init__(self) -> None:
        """! Constructor of a VCard, the same class is used no matter the version. Only data extraction and saving will change/"""
        # version of the vcard
        self.__version: float = 0
        # names of the contact
        self.__names: list[str] = []
        # full name of the contact
        self.__full_name: str = ''
        # organization of the contact
        self.__org: str = ''
        # title of the contact
        self.__title: str = ''
        # addresses of the contact
        self.__addresses: list[Address] = []
        # emails of the contact
        self.__emails: list[Email] = []
        # phones of th contact
        self.__phones: list[Phone] = []
        # note of the contact
        self.__note: str = ''
        # categories of the contact
        self.__categories: list[str] = []

    def __str__(self) -> str:
        """! Method that returns the object as a string.
        All of the data is stored in a string and returned.

        @return a string containing the object.
        """
        return f"VCardObject=[version = {self.__version}, names = {self.__names}, \nfull_name = {self.__full_name}, \norg = {self.__org}, \ntitle = {self.__title}, \naddresses = {self.__addresses}, \nemails = {self.__emails} \nphones = {self.__phones} \nnote = {self.__note} \ncategories = {self.__categories}]"

    def get_version(self) -> float:
        return self.__version

    def set_version(self, version: float) -> None:
        self.__version = version

    def get_names(self) -> list[str]:
        return self.__names

    def set_names(self, names: list[str]) -> None:
        """! Set the list of the names.
        All names are stored here, full name also exist as single string.
        
        @param names the names of the person.
        """
        self.__names = names

    def add_name(self, name) -> None:
        self.__names.append(name)

    def get_full_name(self) -> str:
        return self.__full_name

    def set_full_name(self, full_name: str) -> None:
        self.__full_name = full_name

    def get_org(self) -> str:
        return self.__org

    def set_org(self, org: str) -> None:
        self.__org = org

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

    def add_phone(self, phone: Phone) -> None:
        self.__phones.append(phone)

    def get_note(self) -> str:
        return self.__note

    def set_note(self, note: str) -> None:
        self.__note = note

    def get_categories(self) -> list[str]:
        return self.__categories

    def add_category(self, category: str) -> None:
        self.__categories.append(category)

    def save(self, f) -> None:
        """! Method that save the vcard into a file.
        All the data  will be saved

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """
        # save basic infos
        f.write("BEGIN:VCARD\n")
        f.write(f"VERSION:{self.__version}\n")
        f.write(f"N:{';'.join(self.__names)}\n")
        f.write(f"FN:{self.__full_name}\n")
        f.write(f"TITLE:{self.__title}\n")
        f.write(f"ORG:{self.__org}\n")

        # save each address
        for address in self.__addresses:
            temp: str = "ADR:"
            # save address types
            for type in address.get_address_types():
                temp += f"type={type};"

            temp += f"{';'.join(address.get_address_elements())}\n"

            f.write(temp)

        # save emails
        for email in self.__emails:
            temp: str = "EMAIL:"
            # save email types
            for type in email.get_email_types():
                temp += f"type={type};"

            temp += f"{email.get_email_address()}\n"

            f.write(temp)

        # save phones
        for phone in self.__phones:
            temp: str = "TEL:"
            # save phone types
            for type in phone.get_phone_types():
                temp += f"TYPE={type};"

            temp += f"{phone.get_phone_number()}\n"

            f.write(temp)

        f.write(f"NOTE:{self.__note}\n")
        f.write("END:VCARD\n")

    def export_csv(self, f) -> None:
        """! Method that export a vcard into a CSV.
        The file used may be opened in the vcf manager.

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """

        # create the string to save
        string: str = f"{self.__full_name},"

        # temp list
        temp: list[str] = []

        # add emails to the string
        for email in self.__emails:
            temp.append(email.get_email_address())
        
        string += '/'.join(temp) + ','

        temp.clear()
        # add phones to the string
        for phone in self.__phones:
            temp.append(phone.get_phone_number())

        string += '/'.join(temp) + ','

        temp.clear()
        # add addresses to the string
        for address in self.__addresses:
            temp.append(' '.join(address.get_address_elements()))

        string += '/'.join(temp) + ','

        # add organization
        string += self.__org + '\n'
        # write into the folder
        f.write(string)

    def export_html(self, f) -> None:
        """! Method that export a vcard into an HTML file.
        The file used may be opened in the vcf manager.

        @param f the file wrapper to use. It must be opened as 'w' or at least 'a'.
        """

        # write base of the content
        f.write('<div class="vcard">\n')
        f.write(f"\t<div class=\"fn\">{self.__full_name}</div>\n")
        f.write(f"\t<div class=\"title\">{self.__title}</div>\n")
        f.write(f"\t<div class=\"org\">{self.__org}</div>\n")

        # write emails
        for email in self.__emails:
            f.write(f"\t<div class=\"email\">{email.get_email_address()}</div>\n")

        # write phones
        for phone in self.__phones:
            f.write(f"\t<div class=\"tel\">{phone.get_phone_number()}</div>\n")

        # write end of the file
        f.write(f"\t<div class=\"note\">{self.__note}</div>\n")
        f.write(f"</div>\n")
