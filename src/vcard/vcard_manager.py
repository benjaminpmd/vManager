from vcard.vcard_builder import VCardBuilder
from vcard.vcard import VCard


class VCardManager:
    def __init__(self) -> None:
        self.__builder = VCardBuilder()
        self.__vcard: VCard = VCard()

    def __init__(self, path: str) -> None:
        self.__builder = VCardBuilder()
        self.__vcard = self.__builder.build(path)

    def get_vcard(self) -> VCard:
        return self.__vcard

    def set_vcard(self, path: str):
        self.__vcard = self.__builder.build(path)

    def export(self, output_path: str) -> None:
        
        with open(output_path, 'w') as f:
            f.write(f"N:{';'.join(self.__vcard.get_names())}")
            f.write(f"FN:{self.__vcard.get_full_name()}")
            f.write(f"TITLE:{self.__vcard.get_title}")
            f.write(f"ORG:{(','.join(self.__vcard.get_org()))}")
    
            for address in self.__vcard.get_addresses():
                temp: str = "ADR:"

                for type in address.get_address_types():
                    temp += f"type={type};"

                temp += ';'.join(address.get_address_elements())

                f.write(temp)

            for email in self.__vcard.get_emails():
                temp: str = "EMAIL:"

                for type in email.get_email_types():
                    temp += f"type={type};"

                temp += email.get_email_address()

                f.write(temp)

            for phone in self.__vcard.get_phones():
                temp: str = "TEL:"

                for type in phone.get_phone_types():
                    temp += f"type={type};"

                temp += phone.get_phone_number()

                f.write(temp)

            f.write(f"NOTE:{self.__vcard.get_note()}")

    def export_csv(self, output_path: str) -> None:
        
        with open(output_path, 'w') as f:
            f.write(f"name,{','.join(self.__vcard.get_names())}")
            f.write(f"\nfull name,{self.__vcard.get_full_name()}")
            f.write(f"\ntitle,{self.__vcard.get_title()}")
            f.write(f"\norganization,{(','.join(self.__vcard.get_org()))}")
    
            for address in self.__vcard.get_addresses():
                temp: str = "\naddress,"

                temp += ','.join(address.get_address_elements())

                f.write(temp)

            for email in self.__vcard.get_emails():
                temp: str = "\nemail,"

                temp += email.get_email_address()

                f.write(temp)

            for phone in self.__vcard.get_phones():
                temp: str = "\nphone,"

                temp += phone.get_phone_number()

                f.write(temp)

            f.write(f"\nnote,{self.__vcard.get_note()}")


    def export_html(self, output_path: str) -> None:
        
        with open(output_path, 'w') as f:
            f.write('<div class="vcard">\n')
            f.write(f"\t<div class=\"name\">{' '.join(self.__vcard.get_names())}</div>\n")
            f.write(f"\t<div class=\"full-name\">{self.__vcard.get_full_name()}</div>\n")
            f.write(f"\t<div class=\"title\">{self.__vcard.get_title()}</div>\n")
            f.write(f"\t<div class=\"organization\">{(','.join(self.__vcard.get_org()))}</div>\n")
    
            for address in self.__vcard.get_addresses():
                temp: str = "\t<div class=\"adr\">\n\t\t"

                for type in address.get_address_types():
                    temp += f"<span class=\"type\">{type}</span>"

                temp += ' '.join(address.get_address_elements())

                temp += "\n\t</div>"

                f.write(temp)

            for email in self.__vcard.get_emails():
                temp: str = "\n\t<div class=\"email\">\n\t\t"

                for type in email.get_email_types():
                    temp += f"<span class=\"type\">{type}</span>"

                temp += email.get_email_address()

                temp += "\n\t</div>"

                f.write(temp)

            for phone in self.__vcard.get_phones():
                temp: str = "\n\t<div class=\"tel\">\n\t\t"

                for type in phone.get_phone_types():
                    temp += f"<span class=\"type\">{type}</span>"

                temp += phone.get_phone_number()

                temp += "\n\t</div>"

                f.write(temp)

            f.write(f"\n\t<div class=\"note\">{self.__vcard.get_note()}</div>\n")
            f.write(f"</div>")
