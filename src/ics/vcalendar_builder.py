from ics.vcalendar import VCalendar
from vcf.vcard import VCard
from vcf.data.email import Email
from vcf.data.phone import Phone
from vcf.data.address import Address


class VCalendarBuilder:
    def __init__(self) -> None:
        self.__vcalendar: VCalendar = VCalendar()


    def build(self, lines: list[str]) -> VCalendar:
        return self.__vcalendar
        
