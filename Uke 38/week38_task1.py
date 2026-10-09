
def sensor_reading(readings: list[None | float], threshold: float): 
    '''Reads a list and returns the valid readings above threshold in a new list'''
    valid_reading = [] # defines list
    for a in readings:
        if a is not None and a >= threshold: # checks that the value is above threshold and is a number
            valid_reading.append(a) # adds the value to the new list
    return valid_reading

def report(name: str, readings: list[None | float], threshold: float):
    ''' Makes a report of the valid readings, average reading and the number of removed readings'''
    valid_reading= sensor_reading(readings, threshold) # defines list of which to report on with prevoius function
    print(f"--- SENSOR REPORT: {name.upper()} ---\n" # prints the report 
      f"Valid readings      :    {len(valid_reading)/len(readings)*100:,.2f}%\n" # finds percentage valid readings
      f"Average reading     :    {sum(valid_reading)/len(valid_reading):,.2f}\n" # finds average reading value
      f"Removed readings    :    {len(readings)-len(valid_reading)}") # finds number of removed values
    




# Format for report:
# (Note: These are example numbers, not the expected values for the input given below)
#
# --- SENSOR REPORT: SENSOR NAME ---
# Valid readings      :    89.3%
# Average reading     :     5.01
# Removed readings    :        3

# Input for demonstration
sensor_name = "sensor a"
sensor_readings = [2.673, -3.876, 4.589, None, None, None, -6.111, 0.435, None, 0.005,
                   2.444, 10.897, 0.019, 10.222, -0.543, None, 8.097, 0.962, None, 1.005,
                   None, 0.765, 0.765, 0.765, 0.765, 7.937, -1.007, 4.405, None, None]
sensor_threshold = 0.010

report(sensor_name, sensor_readings, sensor_threshold)

# Output:

#--- SENSOR REPORT: SENSOR A ---
#Valid readings      :    53.33%
#Average reading     :    3.55
#Removed readings    :    1.88
