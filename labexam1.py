import pandas as pd
import numpy as np


file_path = "C:\Users\HP\Downloads\AQI_Data.csv"
data = pd.read_csv(file_path)


print("First 8 rows:")
print(data.head(8))


print("\nLast 5 rows:")
print(data.tail(5))

print("\nData Info:")
data.info()


grouped = data.groupby('City').agg({
    'AQI': 'mean',  
    'PM2.5': 'max',  
    'PM10': 'min'   
}).rename(columns={
    'AQI': 'Mean_AQI',
    'PM2.5': 'Max_PM2.5',
    'PM10': 'Min_PM10'
})

sorted_grouped = grouped.sort_values(by='Mean_AQI', ascending=False)
print("\nSorted Grouped Data:")
print(sorted_grouped)


city_metrics = grouped.agg({
    'Mean_AQI': np.mean,
    'Max_PM2.5': np.max,
    'Min_PM10': np.min
})
print("\nCity Metrics using NumPy:")
print(city_metrics)
