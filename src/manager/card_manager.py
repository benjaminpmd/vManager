import vobject as vcf

class CardManager:
    def __init__(self, path: str = '') -> None:
        self.path = path
        if (path == ''):
            self.vcard: vcf.vCard = vcf.vCard()
        else:
            with open(path, 'r') as f:
                self.vcard: vcf.vCard = vcf.readOne(f.read())  
        for el in self.vcard.contents:
            for e in self.vcard.contents[el]:
                print(e.value)