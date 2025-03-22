from serial import Serial

# Open the serial port
ser = Serial('/dev/cu.usbserial-0001', 115200)
print(ser.name)

# Open a file object to save the data to, in append mode
with open("data.csv", "w") as file:
    # Write the header row to the file
    file.write("server_timestamp,client_timestamp,ID,sensor_values\n")

    # Read the data from the serial port and save it to the file
    while True:
        data = ser.readline().decode("utf-8", "ignore").strip()
        if data:  # Check if data is not empty
            # Assuming the data format is '10:00:00 10:00:01 Sensor1 15'
            parts = data.split(' ')
            if len(parts) == 4:
                # Reformat data to match CSV columns
                formatted_data = f"{parts[0]},{parts[1]},{parts[2]},{parts[3]}\n"
                file.write(formatted_data)

ser.close()

