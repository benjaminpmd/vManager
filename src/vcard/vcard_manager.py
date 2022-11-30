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

    def export_html(self) -> None:
        pass

    def export_csv(self) -> None:
        pass
