# 📖 Bible Reader (CLI)

A terminal-based Bible reading tracker built with Python.
Track daily readings, validate passages, and visualize progress with a Rich-powered heatmap.

---

## 🚀 Features

* ✅ REPL-style command interface
* ✅ Record Bible readings by passage
* ✅ Automatic validation of books, chapters, and verses
* ✅ Daily reading history tracking
* ✅ Verse counting across multi-chapter passages
* ✅ Rich terminal UI
* ✅ GitHub-style heatmap (Sunday → Saturday layout)

---

## 📦 Tech Stack

* Python 3.12+
* Pandas (data loading)
* Rich (terminal UI)

See dependencies: 

---

## 📁 Project Structure

```
.
├── main.py                # Entry point (REPL loop)
├── commands.py            # Command definitions and handlers
├── data_manager.py        # Data loading, parsing, validation, persistence
├── reading.py             # Dataclasses (Reading, DailyReading)
├── pages.py               # UI rendering (home, history, heatmap)
├── data/
│   ├── BIBLE_DATA_P.csv
│   ├── {year}_reading_plan.csv
│   └── {year}_reading_history.json
```

---

## 🧠 Core Concepts

### Reading

Represents a single passage:

```python
Reading(
    date="2026-05-06 08:30:00",
    book="1 Samuel",
    start_chapter=17,
    start_verse=1,
    end_chapter=17,
    end_verse=58
)
```

### DailyReading

Groups readings by date:

```python
DailyReading(
    date="2026-05-06",
    readings=[Reading(...), Reading(...)]
)
```

### In-Memory Structure

```python
reading_history = {
    "2026-05-06": DailyReading(...)
}
```

---

## 🖥️ Usage

Run the app:

```bash
python main.py
```

---

## ⌨️ Commands

| Command        | Description                    |
| -------------- | ------------------------------ |
| `home`         | Show home screen + heatmap     |
| `record ...`   | Record a reading               |
| `record today` | Record today’s planned reading |
| `history`      | Show reading history           |
| `vcount`       | Show total verses read today   |
| `help`         | Show commands                  |
| `clear`        | Clear screen                   |
| `exit`         | Save and exit                  |

See command definitions: 

---

## ✍️ Recording a Reading

Example:

```bash
record 1 Samuel 17:1-17:58
```

Or:

```bash
record 1 Samuel 17:1 58
```

Or:

```bash
record today
```

---

## 🔥 Heatmap

Displayed on the home screen:

* Columns = weeks
* Rows = days (Sunday → Saturday)
* Intensity based on verses read:

```
█ 25+ verses
▓ 24 verses
▒ 12+ verses
░ 1+ verse
```

Rendered using Rich tables. See implementation: 

---

## 💾 Data Persistence

Reading history is saved to:

```
./data/{year}_reading_history.json
```

* Uses atomic writes (safe save)
* Loaded at app startup
* Structure:

```json
[
  {
    "date": "2026-05-06",
    "readings": [
      {
        "date": "2026-05-06 08:30:00",
        "book": "1 Samuel",
        "start_chapter": 17,
        "start_verse": 1,
        "end_chapter": 17,
        "end_verse": 58
      }
    ]
  }
]
```

---

## 📊 Verse Counting

Handles:

* Single chapter
* Multi-chapter
* Full chapter spans

Implemented in `count_verses()`.

---

## ⚠️ Notes

* JSON file should initialize as `[]`, not `{}`.
* Book names must match CSV exactly (e.g., `"1 Samuel"`).
* Validation ensures:

  * Book exists
  * Chapter exists
  * Verse range is valid

---

## 🧭 Future Improvements

* [ ] Streak tracking
* [ ] Monthly summaries
* [ ] Planned vs actual comparison
* [ ] Backup file rotation
* [ ] Web/API version

---

## 👨‍💻 Author

Nathan Allen

---

## 📜 License

MIT 
