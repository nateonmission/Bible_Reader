# /startup.py
import re
import pandas as pd
from datetime import datetime

from reading import Reading, DailyReading

def bible_df_to_dict(bible_dataframe):
    return {
        (book, int(ch)): int(vc)
        for book, ch, vc in zip(
            bible_dataframe["book_name"],
            bible_dataframe["chapter"],
            bible_dataframe["chapter_verse_count"]
        )
    }

def load_data(current_year: int):
    bible_dataframe = pd.read_csv('./data/BIBLE_DATA_P.csv')
    bible_data = bible_df_to_dict(bible_dataframe)

    reading_plan_dataframe = pd.read_csv(f'./data/{current_year}_reading_plan.csv')
    reading_plan = reading_plan_dataframe.set_index('date').to_dict(orient='index')
    
    reading_history_dataframe = pd.read_csv(f'./data/{current_year}_reading_history.csv')
    reading_history = reading_history_dataframe.set_index('date').to_dict(orient='index')
    
    return {
        "bible_data": bible_data,
        "reading_plan": reading_plan,
        "reading_history": reading_history
    }
    
    
    
loaded_data = load_data(datetime.now().year)
today_datetime = datetime.now().date()
today = today_datetime.strftime("%Y-%m-%d")
    
plan = loaded_data.get("reading_plan")
reading_history = loaded_data.get("reading_history")
bible_data = loaded_data.get("bible_data")


def get_today_passage():
    if plan and today in plan:
        today_passage_json = plan.get(today)
        today_passage = f"{today_passage_json['book']} {today_passage_json['start chapter']}:{today_passage_json['start verse']} - {today_passage_json['end chapter']}:{today_passage_json['end verse']}"
    else:
        today_passage = "Passage Not Available."
    
    return today_passage


def passage_parser(args):
    passage = " ".join(args[:]).strip()
    passage = re.sub(r"\s*-\s*", "-", passage)
    re_groups = re.match(r"(.+?)\s+(\d+):(\d+)", passage)
    book = re_groups.group(1)
    start_chapter = re_groups.group(2)
    start_verse = re_groups.group(3)
    end_part = passage.split("-")[1]
    if ":" in end_part:
        end_chapter, end_verse = end_part.split(":")
    else:
        end_chapter = start_chapter
        end_verse = end_part.strip()
        
    this_reading = Reading(
        date= datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        book=book,
        start_chapter=int(start_chapter),
        start_verse=int(start_verse),
        end_chapter=int(end_chapter),
        end_verse=int(end_verse)
    )
    return this_reading
