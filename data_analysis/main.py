from src.data_cleaning import load_data, clean_data, save_clean_data
from src.database import create_connection, save_to_db
from src.visualization import plot_dept_sales, plot_monthly_trends, plot_heatmap
from src.analysis import dept_performance, top_employee, monthly_trends, correlation
def main():
    # Load and clean data
    df = load_data("data/raw/sales_data.csv")
    df = clean_data(df)
    save_clean_data(df, "data/processed/clean_sales_data.csv")

    # Save to database
    conn = create_connection()
    save_to_db(df, conn)

    # Visualizations
    plot_dept_sales(df)
    plot_monthly_trends(df)
    plot_heatmap(df)

    # Analysis
    print("\nDepartment Performance:\n", dept_performance(df))
    print("\nTop Employee:\n", top_employee(df))
    print("\nMonthly Trends:\n", monthly_trends(df))
    print("\nCorrelation:\n", correlation(df))


if __name__ == "__main__":    main()

# main()