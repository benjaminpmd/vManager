"""! File containing the class to build VCards.
VCards are managed through the VcfManager.

@author Benjamin PAUMARD
@version 1.0.0
@version 25 November 2022
"""

# importing modules
# main vcards
from data.vcf.vcard import VCard

# object that compose vcards
from data.vcf.email import Email
from data.vcf.phone import Phone
from data.vcf.address import Address


class VCardBuilder:
    """! Class that contains the builder of a vcard given an array of lines.
    The class is used to create VCard objects.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @version 25 November 2022
    """

    def __init__(self) -> None:
        """! Constructor of the VCardBuilder class."""
        self.__card_lines: list[str] = []
        self.__vcard: VCard = VCard()

    def __extract21(self) -> None:
        """! Method that is used to extract data of a vcard version 2.1."""
        pass

    def __extract30(self) -> None:
        """! Method that is used to extract data of a vcard version 3.0."""

        # check each line of the vcard
        for line in self.__card_lines:
            # elements list will the the line splited with : or ;
            elements: list[str] = ['']

            for char in line:
                # if the char is ; or : append a new element
                if (char == ';') or (char == ':'):
                    elements.append('')
                else:
                    # else append the element to the last string in the element list
                    elements[len(elements)-1] += char

            # remove each empty element that may be in the file
            for i in range(len(elements)-1):
                if elements[i] == '':
                    elements.pop(i)
            
            # get the title of the line
            title: str = elements[0].upper()

            # remove the first element as we wont manipulate it
            elements.remove(elements[0])

            # search among the values how to process it
            match title:

                case 'N':
                    # case N is name
                    # for each element not empty append it to the names list
                    for element in elements:
                        if element != '':
                            self.__vcard.add_name(element)

                case 'FN':
                    # case FN is full name
                    # set the full name
                    self.__vcard.set_full_name(elements[0])

                case 'ORG':
                    # case ORG is organization
                    # set the organization 
                    for element in elements:
                        if element != '':
                            self.__vcard.set_org(element)

                case 'TITLE':
                    # case TITLE is brief summary
                    # set the title
                    self.__vcard.set_title(elements[0])

                case 'EMAIL':
                    # case EMAIL is email information
                    # create an empty Email object
                    email = Email([], '', False)

                    # for each element, check what it is
                    for element in elements:
                        # if it start with TYPE, then append it to the types
                        # except if the type is PREF, in that case, set the email as preferred one
                        if element.upper().startswith("TYPE"):
                            if element.upper().endswith("PREF"):
                                email.set_preferred(True)
                            else:    
                                email.add_email_type(element.split('=')[1].upper())
                        
                        # else then it is the email, set the email address
                        else:
                            email.set_email_address(element)
                    
                    # append the email to the list
                    self.__vcard.add_email(email)
                    
                case 'TEL':
                    # case TEL is phone information
                    # create an empty Phone object
                    phone: Phone = Phone([], '', False)

                    # for each element, check what it is
                    for element in elements:
                        # if it start with TYPE, then append it to the types
                        # except if the type is PREF, in that case, set the phone as preferred one
                        if element.upper().startswith("PREF"):
                            if element.upper().endswith("PREF"):
                                phone.set_preferred(True)
                            else:
                                phone.add_phone_type(element.split('=')[1].upper())
                        
                        # else then it is the number, set the phone
                        else:
                            phone.set_phone_number(element)
                    
                    # append the email to the list
                    self.__vcard.add_phone(phone)

                case 'ADR':
                    # case ADR is an address information
                    # create an empty Address object
                    address: Address = Address([], [], False)

                    # for each element, check what it is
                    for element in elements:
                        # if it start with TYPE, then append it to the types
                        # except if the type is PREF, in that case, set the address as preferred one
                        if element.upper().startswith("TYPE"):
                            if element.upper().endswith("PREF"):
                                address.set_preferred(True)
                            else:
                                address.add_address_type(element.split('=')[1].upper())
                        
                        # else then it is an element of the address
                        else:
                            address.add_address_element(element)

                    # append the address to the list
                    self.__vcard.add_address(address)

                case 'NOTE':
                    # case NOTE is a summary
                    # set the note
                    self.__vcard.set_note(elements[0])

                case 'CATEGORIES':
                    # case CATEGORIES is categories of the contact
                    # set the data
                    categories: list[str] = elements[0].split(',')
                    for category in categories:
                        if category != '':
                            self.__vcard.add_category(category)


    def __extract40(self) -> None:
        """! Method that extract data from a vcard version 4.0."""
        pass

    def build(self, lines: list[str]) -> VCard:
        """! Method that build a VCard given a list of lines.
        The method will generate a VCard object based on the version of the VCard.
        
        @param lines a list of lines of the vcard.
        """

        # reset the card to a empty one
        self.__vcard: VCard = VCard()
        
        # set the lines
        self.__card_lines = lines
        
        # go through the lines until we find the version
        for line in self.__card_lines:
            
            if line.upper().startswith("VERSION:"):
                # call the extraction method based on the version
                if line.endswith("2.1"):
                    self.__extract21()
                
                elif line.endswith("3.0"):
                    self.__extract30()
                    
                elif line.endswith("4.0"):
                    self.__extract40()
        
        # return the vcard
        return self.__vcard
