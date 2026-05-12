import random
from datetime import datetime, timedelta

# Generate enriched sensor data
def generate_sensor_data(timestamp):
    return {
        'timestamp': timestamp,
        'temperature': round(random.uniform(-5, 50), 2),         # °C
        'pressure': round(random.uniform(930, 1055), 2),         # hPa
        'humidity': round(random.uniform(5, 100), 2),            # %
        'rainfall': round(random.uniform(0, 400), 2),            # mm
        'wind_speed': round(random.uniform(0, 160), 2),          # km/h
        'visibility': round(random.uniform(0.1, 10), 2),         # km
        'air_quality_index': random.randint(10, 500)             # AQI Index
    }

# Advanced AI rule-based disaster prediction
def predict_disaster(data):
    temp = data['temperature']
    hum = data['humidity']
    rain = data['rainfall']
    wind = data['wind_speed']
    press = data['pressure']
    vis = data['visibility']
    aqi = data['air_quality_index']

    if temp > 45 and hum < 25:
        return "Heatwave"
    elif temp < 0 and hum > 70:
        return "Cold Wave"
    elif rain > 250 and hum > 80:
        return "Flood"
    elif rain < 5 and hum < 20 and temp > 35:
        return "Drought"
    elif press < 970 and wind > 100:
        return "Storm"
    elif temp > 40 and hum < 20 and wind > 40:
        return "Wildfire"
    elif aqi > 300:
        return "Air Pollution Alert"
    elif vis < 1.0 and hum > 90:
        return "Fog Alert"
    else:
        return "Conditions Normal"

# Display each entry
def display_data(data, label):
    print(f"\n=== {label.upper()} ===")
    for key, value in data.items():
        print(f"{key.replace('_', ' ').title():18}: {value}")
    prediction = predict_disaster(data)
    print(f"Predicted Disaster   : {prediction}")
    return prediction

# Main driver
def main():
    now = datetime.now()
    prediction_log = []

    print("📡 ADVANCED ENVIRONMENTAL MONITORING AND DISASTER PREDICTION 📡")

    # Past (last 3 hours)
    for i in range(3, 0, -1):
        t = now - timedelta(hours=i)
        data = generate_sensor_data(t.strftime("%Y-%m-%d %H:%M:%S"))
        pred = display_data(data, f"Past -{i}h")
        prediction_log.append((data['timestamp'], pred))

    # Present
    current_data = generate_sensor_data(now.strftime("%Y-%m-%d %H:%M:%S"))
    pred = display_data(current_data, "Present")
    prediction_log.append((current_data['timestamp'], pred))

    # Future (next 6 hours)
    for i in range(1, 7):
        t = now + timedelta(hours=i)
        data = generate_sensor_data(t.strftime("%Y-%m-%d %H:%M:%S"))
        pred = display_data(data, f"Future +{i}h")
        prediction_log.append((data['timestamp'], pred))

    # Summary
    print("\n📊 SUMMARY REPORT 📊")
    for ts, pred in prediction_log:
        print(f"{ts} --> {pred}")

if __name__ == "__main__":
    main()
