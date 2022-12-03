"""! File containing the class where the vcard element is stored.

@author Benjamin PAUMARD
@version 1.0.0
@since 25 November 2022
"""
# importing elements used in the VCard
from vcf.data.email import Email
from vcf.data.phone import Phone
from vcf.data.address import Address


class VCard:
    """! Class containing all the elements of a VCard."""

    def __init__(self) -> None:
        """! Constructor of a VCard, the same class is used no matter the version. Only data extraction and saving will change/"""
        # version of the vcard
        self.version: float = 0
        # names of the contact
        self.names: list[str] = []
        # full name of the contact
        self.full_name: str = ''
        # organization of the contact
        self.org: str = ''
        # title of the contact
        self.title: str = ''
        # addresses of the contact
        self.addresses: list[Address] = []
        # emails of the contact
        self.emails: list[Email] = []
        # phones of th contact
        self.phones: list[Phone] = []
        # note of the contact
        self.note: str = ''
        # categories of the contact
        self.categories: list[str] = []

    def __str__(self) -> str:
        """! Method that returns the object as a string.
        All of the data is stored in a string and returned.

        @return a string containing the object.
        """
        return f"VCardObject=[version = {self.version}, names = {self.names}, \nfull_name = {self.full_name}, \norg = {self.org}, \ntitle = {self.title}, \naddresses = {self.addresses}, \nemails = {self.emails} \nphones = {self.phones} \nnote = {self.note} \ncategories = {self.categories}]"

    def get_version(self) -> float:
        return self.version

    def set_version(self, version: float) -> None:
        self.version = version

    def get_names(self) -> list[str]:
        return self.names

    def add_name(self, name) -> None:
        self.names.append(name)

    def get_full_name(self) -> str:
        return self.full_name

    def set_full_name(self, full_name: str) -> None:
        self.full_name = full_name

    def get_org(self) -> str:
        return self.org

    def set_org(self, org: str) -> None:
        self.org = org

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title

    def get_addresses(self) -> list[Address]:
        return self.addresses

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def get_emails(self) -> list[Email]:
        return self.emails

    def add_email(self, email: Email) -> None:
        self.emails.append(email)

    def get_phones(self) -> list[Phone]:
        return self.phones

    def add_phone(self, phone: Phone) -> None:
        self.phones.append(phone)

    def get_note(self) -> str:
        return self.note

    def set_note(self, note: str) -> None:
        self.note = note

    def get_categories(self) -> list[str]:
        return self.categories

    def add_category(self, category: str) -> None:
        self.categories.append(category)

    def save(self, f) -> None:

        f.write("BEGIN:VCARD\n")
        f.write(f"VERSION:{self.version}\n")
        f.write(f"N:{';'.join(self.names)}\n")
        f.write(f"FN:{self.full_name}\n")
        f.write(f"TITLE:{self.title}\n")
        f.write(f"ORG:{self.org}\n")

        for address in self.addresses:
            temp: str = "ADR:"

            for type in address.get_address_types():
                temp += f"type={type};"

            temp += f"{';'.join(address.get_address_elements())}\n"

            f.write(temp)

        for email in self.emails:
            temp: str = "EMAIL:"

            for type in email.get_email_types():
                temp += f"type={type};"

            temp += f"{email.get_email_address()}\n"

            f.write(temp)

        for phone in self.phones:
            temp: str = "TEL:"

            for type in phone.get_phone_types():
                temp += f"type={type};"

            temp += f"{phone.get_phone_number()}\n"

            f.write(temp)

        f.write(f"NOTE:{self.note}\n")
        f.write("END:VCARD\n")

    def export_csv(self, f) -> None:

        f.write(f"name,{','.join(self.names)}")
        f.write(f"\nfull name,{self.full_name}")
        f.write(f"\ntitle,{self.title}")
        f.write(f"\norganization,{self.org}")

        for address in self.addresses:
            temp: str = "\naddress,"

            temp += ','.join(address.get_address_elements())

            f.write(temp)

        for email in self.emails:
            temp: str = "\nemail,"

            temp += email.get_email_address()

            f.write(temp)

        for phone in self.phones:
            temp: str = "\nphone,"

            temp += phone.get_phone_number()

            f.write(temp)

        f.write(f"\nnote,{self.note}")

    def export_html(self, f) -> None:
        f.write('<div class="vcard">\n')
        f.write(f"\t<div class=\"name\">{' '.join(self.names)}</div>\n")
        f.write(f"\t<div class=\"full-name\">{self.full_name}</div>\n")
        f.write(f"\t<div class=\"title\">{self.title}</div>\n")
        f.write(f"\t<div class=\"organization\">{self.org}</div>\n")

        for address in self.addresses:
            temp: str = "\t<div class=\"adr\">\n\t\t"

            for type in address.get_address_types():
                temp += f"<span class=\"type\">{type}</span>"

            temp += ' '.join(address.get_address_elements())

            temp += "\n\t</div>"

            f.write(temp)

        for email in self.emails:
            temp: str = "\n\t<div class=\"email\">\n\t\t"

            for type in email.get_email_types():
                temp += f"<span class=\"type\">{type}</span>"

            temp += email.get_email_address()

            temp += "\n\t</div>"

            f.write(temp)

        for phone in self.phones:
            temp: str = "\n\t<div class=\"tel\">\n\t\t"

            for type in phone.get_phone_types():
                temp += f"<span class=\"type\">{type}</span>"

            temp += phone.get_phone_number()

            temp += "\n\t</div>"

            f.write(temp)

        f.write(f"\n\t<div class=\"note\">{self.note}</div>\n")
        f.write(f"</div>\n")
