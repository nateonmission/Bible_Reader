# /reading.py
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Reading:
    date: str
    book: str
    start_chapter: int
    start_verse: int
    end_chapter: int
    end_verse: int
    
    def __str__(self):
        return f"{self.date}, {self.book}, {self.start_chapter}, {self.start_verse}, {self.end_chapter}, {self.end_verse}"
    
    def recompose(self):
        return f"{self.book} {self.start_chapter}:{self.start_verse} - {self.end_chapter}:{self.end_verse}"
    
    
@dataclass
class DailyReading:
    date: str
    readings: list[Reading]
    
    def __str__(self):
        readings_str = "\n".join(str(reading) for reading in self.readings)
        return f"Date: {self.date}\nReadings:\n{readings_str}"