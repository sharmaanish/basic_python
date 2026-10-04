import pandas as pd

df = pd.DataFrame(
    {
        "salary" : [10,20,23],
        "dept" : ["IT", "HR", "IT"]
    })

print(df['salary'].sum())