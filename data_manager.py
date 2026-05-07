# /startup.py
import os
import re
import json
import pandas as pd
from datetime import datetime
from dataclasses import asdict

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
    
    
def load_reading_history() -> dict[str, DailyReading]:
    file_path = f"./data/{current_year}_reading_history.json"

    if not os.path.exists(file_path):
        return {}

    if os.path.getsize(file_path) == 0:
        return {}

    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        # Accept either [] or {} as empty history
        if data == [] or data == {}:
            return {}

        result = {}

        for dr in data:
            readings = [Reading(**r) for r in dr["readings"]]

            result[dr["date"]] = DailyReading(
                date=dr["date"],
                readings=readings
            )

        return result

    except json.JSONDecodeError as e:
        print(f"[ERROR] Corrupted JSON in {file_path}: {e}")
        raise

    except (OSError, TypeError, KeyError) as e:
        print(f"[ERROR] Failed to load reading history: {e}")
        raise

def load_data(current_year: int):
    bible_dataframe = pd.read_csv('./data/BIBLE_DATA_P.csv')
    bible_data = bible_df_to_dict(bible_dataframe)

    reading_plan_dataframe = pd.read_csv(f'./data/{current_year}_reading_plan.csv')
    reading_plan = reading_plan_dataframe.set_index('date').to_dict(orient='index')
    
    reading_history = load_reading_history()
    
    return {
        "bible_data": bible_data,
        "reading_plan": reading_plan,
        "reading_history": reading_history
    }
    
    
current_year = datetime.now().year    
loaded_data = load_data(current_year)
today_datetime = datetime.now().date()
today = today_datetime.strftime("%Y-%m-%d")
    
plan = loaded_data.get("reading_plan")
reading_history = loaded_data.get("reading_history")
bible_data = loaded_data.get("bible_data")
book_list = set(book for book, _ in bible_data.keys())


def get_today_passage():
    if plan and today in plan:
        today_passage_json = plan.get(today)
        today_passage = f"{today_passage_json['book']} {today_passage_json['start chapter']}:{today_passage_json['start verse']} - {today_passage_json['end chapter']}:{today_passage_json['end verse']}"
    else:
        today_passage = "Passage Not Available."
    
    return today_passage


def validate_passage(passage: Reading):
    book = passage.book
    start_chapter = passage.start_chapter
    start_verse = passage.start_verse
    end_chapter = passage.end_chapter
    end_verse = passage.end_verse
    
    rtn_string = ""
    is_valid = True
    # Check if book exists
    if book not in book_list:
        rtn_string = f"Invalid passage: {book} - Book does not exist."
        is_valid = False
    
    # Validate STARTING chapter and verse
    if (book, start_chapter) not in bible_data:
        rtn_string = f"Invalid passage: {book} {start_chapter}:{start_verse} - Chapter does not exist."
        is_valid = False

    start_max_verse = bible_data[(book, start_chapter)]
    if start_verse > start_max_verse or start_verse < 1:
        rtn_string = f"Invalid passage: {book} {start_chapter}:{start_verse} - Verse does not exist."
        is_valid = False

    # Validate ENDING chapter and verse
    if (book, end_chapter) not in bible_data:
        rtn_string = f"Invalid passage: {book} {end_chapter}:{end_verse} - Chapter does not exist."
        is_valid = False

    end_max_verse = bible_data[(book, end_chapter)]
    if end_verse > end_max_verse or end_verse < 1:
        rtn_string = f"Invalid passage: {book} {end_chapter}:{end_verse} - Verse does not exist."
        is_valid = False

    return is_valid, rtn_string


def passage_parser(args):
    passage = " ".join(args[:]).strip()
    passage = re.sub(r"\s*-\s*", "-", passage)

    parts = passage.split("-", 1)
    start_part = parts[0]
    end_part = parts[1] if len(parts) > 1 else None

    re_groups = re.match(r"(.+?)\s+(\d+):(\d+)", start_part)

    book = re_groups.group(1)
    start_chapter = re_groups.group(2)
    start_verse = re_groups.group(3)

    if end_part is None:
        end_chapter = start_chapter
        end_verse = start_verse
    elif ":" in end_part:
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
    
    is_valid, validation_message = validate_passage(this_reading)
    if not is_valid:
        print(validation_message)
        return None
    
    return this_reading


def save_reading_history(daily_readings: dict[str, DailyReading]):
    dir_path = "./data"
    file_path = f"{dir_path}/{current_year}_reading_history.json"
    temp_path = f"{file_path}.tmp"

    os.makedirs(dir_path, exist_ok=True)

    try:
        data = [
            {
                "date": dr.date,
                "readings": [asdict(r) for r in dr.readings]
            }
            for dr in daily_readings.values()
        ]

        with open(temp_path, "w") as f:
            json.dump(data, f, indent=2)

        os.replace(temp_path, file_path)

        return True

    except (OSError, TypeError) as e:
        print(f"[ERROR] Failed to save reading history: {e}")

        if os.path.exists(temp_path):
            os.remove(temp_path)

        return False