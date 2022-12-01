class Address:
    def __init__(self, address_types: list[str], address: lis) -> None:
        self.__address_type: str = address_type
        self.__street: str = street
        self.__city: str = city
        self.__region: str = region
        self.__postal_code: str = postal_code
        self.__country: str = country

    def get_address_type(self) -> str:
        return self.__address_type

    def set_address_type(self, address_type) -> None:
        self.__address_type = address_type
    
    def get_street(self) -> str:
        return self.__street

    def set_street(self, street) -> None:
        self.__street = street
    
    def get_city(self) -> str:
        return self.__city

    def set_city(self, city) -> None:
        self.__city = city
    
    def get_region(self) -> str:
        return self.__region

    def set_region(self, region) -> None:
        self.__region = region
    
    def get_postal_code(self) -> str:
        return self.__postal_code

    def set_postal_code(self, postal_code) -> None:
        self.__postal_code = postal_code
    
    def get_country(self) -> str:
        return self.__country

    def set_country(self, country) -> None:
        self.__country = country

