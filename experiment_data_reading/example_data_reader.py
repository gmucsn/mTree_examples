import pandas as pd

df = pd.read_json("experiment_data.logex", lines=True)

print("Show simulation 1: ")
print(df.loc[df['simulation_id'] == 1])

print("Show simulation 2: ")
print(df.loc[df['simulation_id'] == 2])