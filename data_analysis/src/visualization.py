import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("output/plot", exist_ok=True)

def plot_dept_sales(df):
    sns.barplot(x="Dept", y="Sales", data=df)
    plt.title("Sales by Department")
    plt.savefig("output/plot/dept_sales.png")
    plt.clf()

def plot_monthly_trends(df):
    sns.lineplot(x="Month", y="Sales", data=df)
    plt.title("Monthly Sales Trends")
    plt.savefig("output/plot/monthly_trends.png")
    plt.clf()

def plot_heatmap(df):
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("output/plot/correlation_heatmap.png")
    plt.clf()
