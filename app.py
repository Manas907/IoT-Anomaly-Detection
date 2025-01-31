import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from PIL import Image
import random
import time

# Load model
model = joblib.load('anomaly_detection_model.pkl')

# Function to simulate real-time sensor data
def generate_sensor_data():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temperature = random.uniform(70.0, 100.0)  # Simulate temperature data
    voltage = random.uniform(215.0, 240.0)     # Simulate voltage data
    power = random.uniform(150.0, 200.0)       # Simulate power data
    cooling_rate = random.uniform(30.0, 40.0)  # Simulate cooling rate data
    humidity = random.uniform(50.0, 80.0)      # Simulate humidity data
    load = random.uniform(70.0, 90.0)          # Simulate load data
    energy_consumption = random.uniform(150.0, 180.0)  # Simulate energy consumption data
    status = 'Anomaly' if temperature > 90 else 'Normal'  # Anomaly if temperature > 90
    
    return {
        "timestamp": timestamp,
        "temperature": temperature,
        "voltage": voltage,
        "power": power,
        "cooling_rate": cooling_rate,
        "humidity": humidity,
        "load": load,
        "energy_consumption": energy_consumption,
        "status": status
    }

# Streamlit UI for language selection
language = st.selectbox("Select Language / 言語選択 / ಭಾಷೆ ಆರಿಸಿ", ["English", "日本語", "ಕನ್ನಡ"])

# Define messages for each language
messages = {
    "English": {
        "title": "IoT Anomaly Detection System",
        "description": "This system predicts anomalies in factory machines based on sensor data.",
        "alert": "Anomaly Detected!",
        "table_columns": ['Timestamp', 'Temperature', 'Voltage', 'Power', 'Cooling Rate', 'Humidity', 'Load', 'Energy Consumption', 'Status'],
        "temperature_label": 'Temperature (°C)',
        "voltage_label": 'Voltage (V)',
        "power_label": 'Power (W)',
        "cooling_rate_label": 'Cooling Rate (%)',
        "humidity_label": 'Humidity (%)',
        "load_label": 'Load (%)',
        "energy_consumption_label": 'Energy Consumption (kWh)',
    },
    "日本語": {
        "title": "IoT異常検出システム",
        "description": "このシステムはセンサーデータに基づいて工場機械の異常を予測します。",
        "alert": "異常が検出されました！",
        "table_columns": ['タイムスタンプ', '温度', '電圧', '電力', '冷却率', '湿度', '負荷', 'エネルギー消費', 'ステータス'],
        "temperature_label": '温度 (°C)',
        "voltage_label": '電圧 (V)',
        "power_label": '電力 (W)',
        "cooling_rate_label": '冷却率 (%)',
        "humidity_label": '湿度 (%)',
        "load_label": '負荷 (%)',
        "energy_consumption_label": 'エネルギー消費量 (kWh)',
    },
    "ಕನ್ನಡ": {
        "title": "ಐಒಟಿ ಅಸಮಾನತೆ ಪತ್ತೆಹಚ್ಚುವ ವ್ಯವಸ್ಥೆ",
        "description": "ಈ ವ್ಯವಸ್ಥೆ ಸಂವೇದಿ ಡೇಟಾ ಆಧರಿಸಿ ಕಾರ್ಖಾನೆ ಯಂತ್ರಗಳ ಅಸಮಾನತೆಯನ್ನು ಪೂರ್ವನಿರ್ಧಾರ ಮಾಡುತ್ತದೆ.",
        "alert": "ಅಸಮಾನತೆ ಪತ್ತೆಹಚ್ಚಲಾಗಿದೆ!",
        "table_columns": ['ಟೈಮ್‌ಸ್ಟ್ಯಾಂಪ್', 'ತಾಪಮಾನ', 'ವೋಲ್ಟೇಜ್', 'ಪವರ್', 'ಕೂಲಿಂಗ್ ದರ', 'ಹ್ಯುಮಿಡಿಟಿ', 'ಲೋಡ್', 'ಎನರ್ಜಿಯ ಉಪಯೋಗ', 'ಸ್ಥಿತಿ'],
        "temperature_label": 'ತಾಪಮಾನ (°C)',
        "voltage_label": 'ವೋಲ್ಟೇಜ್ (V)',
        "power_label": 'ಪವರ್ (W)',
        "cooling_rate_label": 'ಕೂಲಿಂಗ್ ದರ (%)',
        "humidity_label": 'ಹ್ಯುಮಿಡಿಟಿ (%)',
        "load_label": 'ಲೋಡ್ (%)',
        "energy_consumption_label": 'ಎನರ್ಜಿಯ ಉಪಯೋಗ (kWh)',
    }
}

# Display messages based on the selected language
st.title(messages[language]["title"])
st.write(messages[language]["description"])

# Generate data once every time the user interacts with the app
sensor_data = generate_sensor_data()
df = pd.DataFrame([sensor_data])

# Display the generated data in the selected language
st.write(f"{messages[language]['temperature_label']}: {sensor_data['temperature']} °C")
st.write(f"{messages[language]['voltage_label']}: {sensor_data['voltage']} V")
st.write(f"{messages[language]['power_label']}: {sensor_data['power']} W")
st.write(f"{messages[language]['cooling_rate_label']}: {sensor_data['cooling_rate']} %")
st.write(f"{messages[language]['humidity_label']}: {sensor_data['humidity']} %")
st.write(f"{messages[language]['load_label']}: {sensor_data['load']} %")
st.write(f"{messages[language]['energy_consumption_label']}: {sensor_data['energy_consumption']} kWh")
st.write(f"Status: {sensor_data['status']}")

# Anomaly detection
if sensor_data['status'] == 'Anomaly':
    st.write(messages[language]["alert"])

# Load dataset
data = pd.read_csv('sensor_data.csv')

# Display historical data
st.subheader("Historical Sensor Data")
st.write(data)

# Display temperature graph
st.subheader("Temperature Over Time")
plt.plot(data['timestamp'], data['temperature'], label='Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.xticks(rotation=45)
plt.title('Temperature Over Time')
plt.tight_layout()
st.pyplot(plt)

# Prediction and Anomaly Detection
def predict_anomaly(data):
    X = data[['temperature', 'voltage', 'power', 'cooling_rate']]
    prediction = model.predict(X)
    data['status'] = ['Anomaly' if x == 1 else 'Normal' for x in prediction]
    return data

# Display anomaly detection results
st.subheader("Anomaly Detection Results")
predicted_data = predict_anomaly(data)
st.write(predicted_data)

# Alert message based on anomaly detection
anomalies = predicted_data[predicted_data['status'] == 'Anomaly']
if not anomalies.empty:
    st.warning(f"Anomalies detected! {len(anomalies)} abnormal readings.")
else:
    st.success("All machines are functioning normally.")

# Adding a gif animation (Ensure the file is in the correct path)
gif_path = "anime_animation.gif"  # Replace with your GIF file path
try:
    st.image(gif_path, caption="Enjoy the animation!", use_container_width=True)
except:
    st.warning("This content is not available in gif format.")
