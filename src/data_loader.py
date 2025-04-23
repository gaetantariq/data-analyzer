# src/data_loader.py
import pandas as pd

class DataLoader:
    REQUIRED_COLUMNS = ['date', 'category', 'amount', 'customer_id']

    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.filepath)
        self.validate_data()
        self.clean_data()
        return self.df

    def validate_data(self):
        missing = [col for col in self.REQUIRED_COLUMNS if col not in self.df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    def clean_data(self):
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df['amount'] = pd.to_numeric(self.df['amount'], errors='coerce')
        self.df.dropna(subset=['date', 'amount'], inplace=True)

    def filter_by_date(self, start_date, end_date):
        return self.df[(self.df['date'] >= start_date) & (self.df['date'] <= end_date)]

    def filter_by_category(self, categories):
        return self.df[self.df['category'].isin(categories)]
