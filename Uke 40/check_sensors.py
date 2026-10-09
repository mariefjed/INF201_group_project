# Read files

import yaml
import json
import pandas as pd


# Les YAML
with open("/Users/mariefjellbakk-edfeldt/Library/CloudStorage/OneDrive-NorwegianUniversityofLifeSciences/INF201/Uke 40/config.yml", "r", encoding = "utf-8") as file:
    data = yaml.safe_load(file)

max_days_since_calibration = data["max_days_since_calibration"]
output_file = data["output_file"]

# Read and join data

data_cal=("/Users/mariefjellbakk-edfeldt/Library/CloudStorage/OneDrive-NorwegianUniversityofLifeSciences/INF201/Uke 40/calibrations.csv")

calibrations = pd.read_csv(data_cal, sep=',', header = 0)
print(calibrations)

data_excel = ("/Users/mariefjellbakk-edfeldt/Library/CloudStorage/OneDrive-NorwegianUniversityofLifeSciences/INF201/Uke 40/sensors.xlsx")

sensor = pd.read_excel(data_excel)
print(sensor)

join = sensor.merge(
    calibrations,
    on = "sensor_id",
    how = "inner"

)
print(join)

# Filtrerer data
sensor_filtrert = join[join["days_since_calibration"] > max_days_since_calibration]
print(sensor_filtrert)

# Finner tilovers etter filtrering og legger det i output fil
sensor_overdue= sensor_filtrert.to_dict(orient = "records")


with open(output_file, "w", encoding="utf-8") as file:
    json.dump(sensor_overdue, file, indent=2)

print(f"Exported {len(sensor_overdue)} overdue sensors to {output_file}")
