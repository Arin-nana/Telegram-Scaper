from dataclasses import dataclass
from datetime import datetime


@dataclass
class TelegramMessage:
    text: str
    datetime: datetime
    link: str
