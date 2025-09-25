import csv
from datetime import datetime

# Forward fill missing values for each sensor's temperature and humidity
def forward_fill(data):
    last_values = {}
    for row in data:
        sensor = row['sensor_id']
        if sensor not in last_values:
            last_values[sensor] = {'temperature': None, 'humidity': None}
        
        for field in ['temperature', 'humidity']:
            if row[field] == '' or row[field] is None:
                # Fill with last known value if exists
                row[field] = last_values[sensor][field]
            else:
                # Update last known value
                row[field] = float(row[field])
                last_values[sensor][field] = row[field]

# Apply rolling mean to remove drift (window size in rows)
def rolling_mean(data, window=3):
    # Group data by sensor_id
    grouped = {}
    for row in data:
        grouped.setdefault(row['sensor_id'], []).append(row)
    
    for sensor, rows in grouped.items():
        temps = [r['temperature'] if r['temperature'] is not None else 0 for r in rows]
        hums = [r['humidity'] if r['humidity'] is not None else 0 for r in rows]
        
        def roll_avg(values):
            result = []
            for i in range(len(values)):
                window_vals = values[max(0, i-window+1):i+1]
                avg = sum(window_vals) / len(window_vals)
                result.append(avg)
            return result
        
        temps_avg = roll_avg(temps)
        hums_avg = roll_avg(hums)
        
        for i, row in enumerate(rows):
            row['temperature'] = temps_avg[i]
            row['humidity'] = hums_avg[i]

# Standard scale temperature and humidity (zero mean, unit variance)
def standard_scale(data):
    temps = [row['temperature'] for row in data if row['temperature'] is not None]
    hums = [row['humidity'] for row in data if row['humidity'] is not None]
    
    def mean_std(values):
        mean = sum(values) / len(values) if values else 0
        variance = sum((x - mean) ** 2 for x in values) / len(values) if values else 0
        std = variance ** 0.5
        return mean, std if std != 0 else 1
    
    mean_temp, std_temp = mean_std(temps)
    mean_hum, std_hum = mean_std(hums)
    
    for row in data:
        if row['temperature'] is not None:
            row['temperature'] = (row['temperature'] - mean_temp) / std_temp
        if row['humidity'] is not None:
            row['humidity'] = (row['humidity'] - mean_hum) / std_hum

# Encode sensor_id as integers
def encode_sensor_ids(data):
    sensor_map = {}
    next_id = 0
    for row in data:
        sid = row['sensor_id']
        if sid not in sensor_map:
            sensor_map[sid] = next_id
            next_id += 1
        row['sensor_id_encoded'] = sensor_map[sid]

# Read CSV
def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Clean row fields
            data.append({
                'timestamp': row.get('timestamp', '').strip(),
                'sensor_id': row.get('sensor_id', '').strip(),
                'temperature': row.get('temperature', '').strip(),
                'humidity': row.get('humidity', '').strip()
            })
    return data

# Write CSV
def write_csv(data, filename):
    fieldnames = ['timestamp', 'sensor_id', 'sensor_id_encoded', 'temperature', 'humidity']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({
                'timestamp': row['timestamp'],
                'sensor_id': row['sensor_id'],
                'sensor_id_encoded': row['sensor_id_encoded'],
                'temperature': round(row['temperature'], 6) if row['temperature'] is not None else '',
                'humidity': round(row['humidity'], 6) if row['humidity'] is not None else ''
            })

def main():
    input_file = input("Enter IoT sensor CSV filename: ").strip()
    output_file = 'processed_' + input_file

    data = read_csv(input_file)
    forward_fill(data)
    rolling_mean(data, window=3)
    standard_scale(data)
    encode_sensor_ids(data)
    write_csv(data, output_file)

    print(f"✅ Processed data written to: {output_file}")

if __name__ == "__main__":
    main()
