def dept_performance(df):
    return df.groupby("Dept")["Sales"].sum()

def top_employee(df):
    return df.groupby("Name")["Sales"].sum().sort_values(ascending=False).head(1)

def monthly_trends(df):
    return df.groupby("Month")["Sales"].sum()

def correlation(df):
    return df.corr(numeric_only=True)

