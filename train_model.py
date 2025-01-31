import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
data = pd.read_csv('sensor_data.csv')

# Preprocess data
X = data[['temperature', 'voltage', 'power', 'cooling_rate']]
y = data['status'].apply(lambda x: 1 if x == 'Anomaly' else 0)  # 1 = Anomaly, 0 = Normal

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'anomaly_detection_model.pkl')

# Optionally, you can print the accuracy of the model
print("Model Training Completed.")
