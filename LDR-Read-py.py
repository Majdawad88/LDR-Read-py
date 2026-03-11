#git clone https://github.com/Majdawad88/LDR-Read-py.git

import serial
import csv
import time

ser = serial.Serial('COM16', 9600)
with open('light_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Time", "LightLevel"])
    for i in range(200): # Collect 200 data points
        line = ser.readline().decode('utf-8').strip()
        if line:
            writer.writerow([i, int(line)])
            print(f"Logged: {i}, {line}", flush=True)
