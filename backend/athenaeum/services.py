from dataclasses import dataclass
from typing import Optional
from drf_service_layer.services import Service


@dataclass
class ScrapperDTO:
    book_name: str


class ScrapperService(Service):
    dto: ScrapperDTO

    def scrapper(self):
        book = self.dto.book_name
        pass
        # logic

