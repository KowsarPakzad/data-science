import pandas as pd
from ydata_profiling import ProfileReport
import os
print("========================")
print(os.getcwd())
df = pd.read_csv('E:\industry.csv')
profile = ProfileReport(df, title="exam")
profile.to_file("E:\q1.html")
