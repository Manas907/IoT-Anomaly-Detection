# IoT Anomaly Detection System

## Overview

The **IoT Anomaly Detection System** is designed to predict anomalies in factory machines using sensor data. The system analyzes real-time sensor readings such as temperature, voltage, power, humidity, and more, to determine whether the machine is operating normally or showing abnormal behavior. With **Streamlit**, the system provides a user-friendly interface with multi-language support (English, Japanese, and Kannada) for better accessibility.

## Features

- **Real-time anomaly detection** based on sensor data
- **Multiple language support**: English, Japanese, and Kannada
- **Temperature, voltage, power, and other sensor readings**
- **Anomaly detection results** showing abnormal readings
- **Visualization of historical sensor data** in graphs and tables
- **User-friendly interface** built using **Streamlit**

## Technologies Used

- **IoT (Internet of Things)**: For real-time sensor data collection
- **Machine Learning**: For detecting anomalies in sensor data
- **Streamlit**: For creating an interactive and user-friendly web interface
- **Python Libraries**: NumPy, Pandas, Matplotlib, Scikit-learn, and others

## Output Example

The system displays the following information:

- **Real-time Sensor Data**:
    - Temperature (°C): 79.40°C
    - Voltage (V): 234.01V
    - Power (W): 197.59W
    - Cooling Rate (%): 30.56%
    - Humidity (%): 52.76%
    - Load (%): 85.73%
    - Energy Consumption (kWh): 166.55 kWh

- **Anomaly Detection Results**:
    - Status: Normal
    - Anomalies detected: 3 abnormal readings

- **Historical Sensor Data**:
    - Graphs and tables showing sensor data over time.

- **Language Support**:
    - Allows users to switch between English, Japanese, and Kannada for the interface.

## Installation

To install and run the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/iot-anomaly-detection.git
    ```

2. Navigate to the project directory:
    ```bash
    cd iot-anomaly-detection
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## How It Works

1. **Data Collection**: The system collects real-time sensor data from connected IoT devices.
2. **Data Analysis**: The data is processed and analyzed using machine learning algorithms to detect anomalies.
3. **Anomaly Detection**: The system identifies any abnormal readings and flags them as potential issues.
4. **Language Switching**: The user can switch between English, Japanese, and Kannada for easier interaction.
5. **Visualization**: The system presents historical sensor data in graphs and tables for better understanding.

## Usage

Once the application is running, the user will be able to:

- View real-time sensor data.
- See the status of machine operation (normal or abnormal).
- View historical data in graphical and tabular formats.
- Switch between English, Japanese, and Kannada for interface language.

## Contributing

Feel free to fork the repository and submit pull requests. You can contribute by fixing bugs, adding new features, or improving the documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
