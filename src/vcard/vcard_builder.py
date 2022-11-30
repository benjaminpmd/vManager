from vcard.vcard import VCard


class VCardBuilder:
    def __init__(self) -> None:
        self.__vcard: VCard = VCard()

    def build(self, path: str) -> VCard:
        self.__vcard = VCard()

        with open(path, 'r') as f:
            for line in f:
                line = line.replace("\n", '')
                if line.startswith("N:"):
                    
                    split: list[str] = line.split(':')[1].split(";")
                    for name in split:
                        if name != '':
                            self.__vcard.add_name(name)

                elif line.startswith("FN:"):
                    self.__vcard.set_full_name(line.split(':')[1])

                elif line.startswith("ORG:"):
                    split: list[str] = line.split(':')[1].split(";")
                    for org in split:
                        if org != '':
                            self.__vcard.add_org(org)

        print
        return self.__vcard
