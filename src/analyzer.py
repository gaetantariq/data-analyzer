# src/analyzer.py
class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def summary_statistics(self):
        return self.df.groupby('category')['amount'].agg(['mean', 'median', 'std'])

    def time_series(self):
        return self.df.groupby('date')['amount'].sum()

    def spending_distribution(self):
        return self.df['amount'].describe()

    def top_categories(self, top_n=5):
        return self.df.groupby('category')['amount'].sum().sort_values(ascending=False).head(top_n)

    def customer_segmentation(self):
        return self.df.groupby('customer_id')['amount'].sum()
