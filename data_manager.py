# /startup.py
import pandas as pd
import datetime

def load_data(current_year: int):
    bible_dataframe = pd.read_csv('./data/BIBLE_DATA_P.csv')
    
    reading_plan_dataframe = pd.read_csv(f'./data/{current_year}_reading_plan.csv')
    reading_plan = reading_plan_dataframe.set_index('date').to_dict(orient='index')
    
    reading_history_dataframe = pd.read_csv(f'./data/{current_year}_reading_history.csv')
    reading_history = reading_history_dataframe.set_index('date').to_dict(orient='index')
    
    return {
        "bible_data": bible_dataframe,
        "reading_plan": reading_plan,
        "reading_history": reading_history
    }
    

    
