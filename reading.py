# /reading.py
import datetime
from dataclasses import dataclass

@dataclass
class Reading:
    date: datetime.date
    book: str
    start_chapter: int
    start_verse: int
    end_chapter: int
    end_verse: int
    
    def __str__(self):
        return f"{self.date}, {self.book}, {self.start_chapter}, {self.start_verse}, {self.end_chapter}, {self.end_verse}"