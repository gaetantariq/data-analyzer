# src/visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def bar_chart(self, data, title="Bar Chart", save_path=None):
        fig, ax = plt.subplots()
        data.plot(kind='bar', ax=ax)
        ax.set_title(title)
        if save_path:
            plt.savefig(save_path)
        return fig

    def line_chart(self, data, title="Line Chart", save_path=None):
        fig, ax = plt.subplots()
        data.plot(kind='line', ax=ax)
        ax.set_title(title)
        if save_path:
            plt.savefig(save_path)
        return fig

    def pie_chart(self, data, title="Pie Chart", save_path=None):
        fig, ax = plt.subplots()
        data.plot(kind='pie', ax=ax, autopct='%1.1f%%')
        ax.set_ylabel('')
        ax.set_title(title)
        if save_path:
            plt.savefig(save_path)
        return fig

    def heatmap(self, df, title="Heatmap", save_path=None):
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        ax.set_title(title)
        if save_path:
            plt.savefig(save_path)
        return fig
