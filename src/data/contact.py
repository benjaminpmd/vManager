"""! File containing the class used to store a contact.

@author Benjamin PAUMARD
@version 1.0.0
@since 10/11/2022
"""

class Contact:
    def __init__(self, name: str, firstname: str, title: str) -> None:
        """! Constructor of the class used to store a contact data."""
        self.name: str = name
        self.firstname: str = firstname
        self.title: str = title
