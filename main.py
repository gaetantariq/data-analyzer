# main.py
import argparse
from src.data_loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizer import DataVisualizer

def main():
    parser = argparse.ArgumentParser(description="Data Analysis Tool")
    parser.add_argument("csv_path", help="Path to the CSV file")
    parser.add_argument("--analysis", choices=["summary", "time", "top"], default="summary")
    parser.add_argument("--plot", choices=["bar", "line", "pie", "heatmap"], default="bar")
    parser.add_argument("--output", help="Path to save the plot", default=None)
    args = parser.parse_args()

    loader = DataLoader(args.csv_path)
    df = loader.load_data()
    analyzer = DataAnalyzer(df)
    visualizer = DataVisualizer()

    if args.analysis == "summary":
        result = analyzer.summary_statistics()
    elif args.analysis == "time":
        result = analyzer.time_series()
    elif args.analysis == "top":
        result = analyzer.top_categories()
    else:
        result = df

    print(result)

    if args.plot == "bar":
        visualizer.bar_chart(result, save_path=args.output)
    elif args.plot == "line":
        visualizer.line_chart(result, save_path=args.output)
    elif args.plot == "pie":
        visualizer.pie_chart(result, save_path=args.output)
    elif args.plot == "heatmap":
        visualizer.heatmap(df, save_path=args.output)

if __name__ == "__main__":
    main()
