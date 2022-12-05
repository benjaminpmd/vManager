"""! File containing the class to store an Address.
Address are stored as a list in a VCard. Fore more information, please see VCard.py documentation.

@author Benjamin PAUMARD
@version 1.0.0
@version 25 November 2022
"""

class Address:
    """! Class that contains the elements of an address.
    Address are part of a VCard.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @version 25 November 2022
    """
    
    def __init__(self, address_types: list[str] = [], address: list[str] = [], preferred: bool = False) -> None:
        """! Constructor of the address class.
        In this class, all elements related to an address are stored.

        @param address_types the types of the address (optional).
        @param address the elements making the address (optional).
        @param wether the address is the preferred one or not (optional).
        """
        self.__address_types: list[str] = address_types
        self.__address_elements: list[str] = address
        self.__preferred: bool = preferred
    
    def __str__(self) -> str:
        """! Override the default __str__ method.
        Allow to see the object as a string.
        
        @return the object as a string.
        """
        return "AddressObject: {address_types=["+(', '.join(self.__address_types))+"], address_address=["+(', '.join(self.__address_elements))+"], preferred="+str(self.__preferred)+'}'

    
    def get_address_types(self) -> list[str]:
        """! Getter of the address types.
        Address types are stored as a list.

        @return a list of address types.
        """
        return self.__address_types

    def add_address_type(self, address_type: str) -> None:
        """! Method that append an address type to the list of types.
        All the types are represented as strings.
        
        @param address_type the type of the address to add.
        """
        self.__address_types.append(address_type)
    
    def get_address_elements(self) -> list[str]:
        """! Getter of the address elements.
        Address elements as street, city, state, country etc are stored separately as a list.

        @return a list of address elements.
        """
        return self.__address_elements

    def add_address_element(self, element) -> None:
        """! Method that append an address element to the list of elements.
        Address elements as street, city, state, country etc are stored separately as a list.
        
        @param address_element the element of the address to add.
        """
        self.__address_elements.append(element)

    def is_preferred(self) -> bool:
        """! Get a boolean, True whether the address is the preferred one, False otherwise.
        By default, the preferred parameter is at False.
        
        @return boolean if the address is the preferred one.
        """
        return self.__preferred

    def set_preferred(self, preferred) -> None:
        """! Set whether the address is the preferred one.
        By default, the preferred parameter is at False.
        
        @param preferred if the address is the preferred one.
        """
        self.__preferred = preferred
    

