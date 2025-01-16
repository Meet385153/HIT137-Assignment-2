import os
import re
import pandas as pd

# Define the temperature data
data_directory = 'temperature_data' 

file_pattern = r"stations_group_\d{4}\.csv"

# List all files in the data directory
all_files = os.listdir(data_directory)

csv_files = [file for file in all_files if re.match(file_pattern, file)]

# List to store individual DataFrames for each CSV file
dfs = []

# Loop through the filtered CSV files and read them into DataFrames
for file in csv_files:
    file_path = os.path.join(data_directory, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)

# Print the first few rows of the concatenated DataFrame for verification
print(df_all.head())

# Define the months that correspond to each season
seasons = {
    'Spring': ['September', 'October', 'November'],
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August']
}

def calculate_seasonal_avg(df, seasons):
    seasonal_avg = {}
    for season, months in seasons.items():
        seasonal_avg[season] = df[months].mean(axis=1)  
    return seasonal_avg

# Calculate the average temperature for each season across all years
seasonal_avg_all = calculate_seasonal_avg(df_all, seasons)

for season, avg_temps in seasonal_avg_all.items():
    df_all[season] = avg_temps

seasonal_avg_across_years = {season: df_all[season].mean() for season in seasonal_avg_all.keys()}

# Write the average seasonal temperatures to a text file
with open('average_temp.txt', 'w') as f:
    for season, avg_temp in seasonal_avg_across_years.items():
        f.write(f"{season} Average Temperature: {avg_temp:.2f}°C\n")

df_all['Temp_Range'] = df_all.iloc[:, 4:16].max(axis=1) - df_all.iloc[:, 4:16].min(axis=1)

# Identify the station(s) with the largest temperature range
largest_temp_range_station = df_all.loc[df_all['Temp_Range'] == df_all['Temp_Range'].max()]

with open('largest_temp_range_station.txt', 'w') as f:
    f.write("Station(s) with largest temperature range:\n")
    for _, row in largest_temp_range_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Temperature Range: {row['Temp_Range']:.2f}°C)\n")

# Calculate the maximum temperature for each station
df_all['Max_Temperature'] = df_all.iloc[:, 4:16].max(axis=1)

# Calculate the minimum temperature for each station
df_all['Min_Temperature'] = df_all.iloc[:, 4:16].min(axis=1)

warmest_station = df_all.loc[df_all['Max_Temperature'] == df_all['Max_Temperature'].max()]
coolest_station = df_all.loc[df_all['Min_Temperature'] == df_all['Min_Temperature'].min()]

# Write the warmest and coolest stations to a text file
with open('warmest_and_coolest_station.txt', 'w') as f:
    f.write("Warmest Station(s):\n")
    for _, row in warmest_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Max Temperature: {row['Max_Temperature']:.2f}°C)\n")
    
    f.write("\nCoolest Station(s):\n")
    for _, row in coolest_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Min Temperature: {row['Min_Temperature']:.2f}°C)\n")