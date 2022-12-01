from vcard.vcard import VCard
from vcard.elements.email import Email
from vcard.elements.phone import Phone
from vcard.elements.address import Address

class VCardBuilder:
    def __init__(self) -> None:
        self.__vcard: VCard = VCard()

    def build(self, path: str) -> VCard:
        self.__vcard = VCard()

        with open(path, 'r') as f:
            for line in f:
                
                line = line.replace("\n", '')
                
                elements: list[str] = ['']
                
                for char in line:
                    if (char == ';') or (char == ':'):
                        elements.append('')
                    else:
                        elements[len(elements)-1] += char 
                
                for i in range(len(elements)-1):
                    if elements[i] == '':
                        elements.pop(i)
                
                title: str = elements[0]

                elements.remove(elements[0])
            
                
                match title:
                    case 'N':
                        for element in elements:
                            if element != '':
                                self.__vcard.add_name(element)

                    case 'FN':
                        self.__vcard.set_full_name(elements[0])

                    case 'ORG':
                        for element in elements:
                            if element != '':
                                self.__vcard.add_org(element)
                
                    case 'TITLE':
                        self.__vcard.set_title(elements[0])
                
                    case 'EMAIL':
                        email: Email = Email()
                        for element in elements:
                            if element.lower().startswith('type'):
                                email.add_email_type(element.split('=')[1].upper())
                            else:
                                email.set_email_address(element)
                        self.__vcard.add_email(email)
                    
                    case 'TEL':
                        phone: Phone = Phone()
                        for element in elements:
                            if element.lower().startswith('type'):
                                phone.add_phone_type(element.split('=')[1].upper())
                            else:
                                phone.set_phone_number(element)
                        self.__vcard.add_phone(phone)

                    case 'ADR':
                        address: Address = Address()
                        for element in elements:
                            if element.lower().startswith('type'):
                                address.add_address_type(element.split('=')[1].upper())
                            else:
                                address.add_address_element(element)
                        self.__vcard.add_address(address)

                    case 'NOTE':
                        self.__vcard.set_note(elements[0])

                    case 'CATEGORIES':
                        categories: list[str] = elements[0].split(',')
                        for category in categories:
                            if category != '':
                                self.__vcard.add_category(category)

        return self.__vcard
