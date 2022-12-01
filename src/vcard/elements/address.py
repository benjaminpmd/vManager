class Address:
    def __init__(self, address_types: list[str] = [], address: list[str] = []) -> None:
        self.__address_types: list[str] = address_types
        self.__address_elements: list[str] = address
    
    def get_address_types(self) -> list[str]:
        return self.__address_types

    def add_address_type(self, address_type) -> None:
        self.__address_types.append(address_type)
    
    def get_address_elements(self) -> list[str]:
        return self.__address_elements

    def add_address_element(self, element) -> None:
        self.__address_elements.append(element)
    

