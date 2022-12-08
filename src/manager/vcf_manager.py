"""! File containing the manager to manipulate a VCF file.
All methods to read and get the content of a VCF file are in this file, 
Features to export contacts to a vcf file are also available here.

@author Benjamin PAUMARD
@version 1.0.0
@since 03 December 2022
"""
from data.vcf.vcard import VCard
from builder.vcard_builder import VCardBuilder


class VCFManager:
    """! Class that contains all methods to manage a vcf file.
    This class allow to read, get the content and save a vcf file.

    @author Benjamin PAUMARD
    @version 1.0.0
    @since 03 December 2022
    """
    def __init__(self, path: str = '') -> None:
        """! Constructor of the VcfManager file.
        This class is used to read Vcf file.
        
        @param path an optional path to read
        """
        # set the attributes
        self.__vcards: list[VCard] = []
        self.__builder: VCardBuilder = VCardBuilder()
        self.__path: str = '' 
        self.__current_card_index: int = -1

        # if path is not empty, read the content of the file
        if path != '':
            self.__path = path
            self.read(path)

    def get_vcards(self) -> list[VCard]:
        """! Get the cards that have been read.
        It is necessary to use the read method first.
        
        @return the list of VCard objects.
        """
        return self.__vcards

    def get_vcard_from_name(self, full_name: str) -> VCard | None:
        """! Get the card from a given vcard.
        the vcard is returned for display.
        
        @param full_name the name to search.
        @return a VCard and its id.
        """
        for i in range(len(self.__vcards)):
            if (self.__vcards[i].get_full_name() ==full_name):
                self.__current_card_index = i
                return self.__vcards[i]
        return None

    def update_current_card(self, full_name: str = '', names: list[str] = [], org: str = '', title: str = '') -> None:
        """! Updating the card that was selected using the get_card_from_name method.
        Only this method can update the current selected card.
        
        @param full_name the full name to set.
        @param names the name list to use.
        @param org the org to mark.
        @param title the title to apply.
        """
        # update the card
        self.__vcards[self.__current_card_index].set_full_name(full_name)
        self.__vcards[self.__current_card_index].set_names(names)
        self.__vcards[self.__current_card_index].set_org(org)
        self.__vcards[self.__current_card_index].set_title(title)
        # save to the file
        self.save()

    def set_vcards(self, vcards: list[VCard]) -> None:
        """! Set the cards of the manager.
        The current cards will be replaced.
        
        @param the list of VCard objects.
        """
        self.__vcards = vcards

    def get_path(self) -> str:
        """! Method to get the path of the opened file.
        The path can be used by default if no path is provided to save method.
        
        @return the path of the opened file.
        """
        return self.__path

    def set_path(self, path: str) -> None:
        """! Method to set the path of the opened file.
        The path can be used by default if no path is provided to save method.
        
        @param path the path of the opened file.
        """
        self.__path = path

    def read(self, path: str) -> None:
        """! Open a vcf file and extract all VCards contained inside.
        The vcf file can contain multiple VCards from different versions.
        To get the cards that have been read, please use get_cards method.

        @param path the path of the file to read.
        """
        # reset the vcards
        self.__vcards = []

        # open the file
        with open(path, 'r') as f:
            
            # init the lines of the vcard
            card_lines: list[str] = []

            # read each line of the file
            for line in f:
        
                # replace return to line with empty string
                line = line.replace("\n", '')

                # if the line is the beginning of a VCard, reset the list
                if line.upper() == "BEGIN:VCARD":
                    card_lines = []
                
                # if the line indicate the end of a VCard, then create the VCard and store it
                if line.upper() == "END:VCARD":
                    card = None
                    card = self.__builder.build(card_lines)
                    self.__vcards.append(card)
                
                # else it's the content of a VCard, save it in the list of the lines
                else:
                    card_lines.append(line)
        self.__path = path
    
    def save(self, path: str = '') -> None:
        """! Save all the contained contact into a vcf file.
        All the VCards this manager contains will be saved inside.

        @param path the path of the file to store.
        """
        # if no path is provided, then save it in the original file
        if path == '':
            path = self.__path

        with open(path, 'w') as f:
            for vcard in self.__vcards:
                vcard.save(f)

    def export_csv(self, path: str) -> None:
        """! Save all the contained contact into a vcf file.
        All the VCards this manager contains will be saved inside.

        @param path the path of the file to store.
        """
        with open(path, 'w') as f:
            f.write("full name,emails,phones,addresses,organization\n")
            for vcard in self.__vcards:
                vcard.export_csv(f)


    def export_html(self, path: str, complete: bool = False) -> None:
        """! Save all the contained contact into a vcf file.
        All the VCards this manager contains will be saved inside.

        @param path the path of the file to store.
        @param complete a boolean indicating if the page must be completed rendered.
        """
        
        with open(path, 'w') as f:

            if (complete):
                f.write("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n\t<title>Exported Contacts</title>\n</head>\n<body>\n")

            for vcard in self.__vcards:
                vcard.export_html(f)

            if (complete):
                f.write("</body>\n</html>\n")

            
