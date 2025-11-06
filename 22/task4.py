from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ✅ Step 1: Simulated ECG feature data (e.g., heart rate, RR interval, P-wave amplitude)
X = [
    [72, 0.85, 0.12],   # Normal
    [110, 0.60, 0.08],  # Tachycardia
    [55, 1.10, 0.15],   # Bradycardia
    [90, 0.75, 0.10],   # Normal
    [130, 0.50, 0.07],  # Tachycardia
    [48, 1.20, 0.18],   # Bradycardia
]

# ✅ Step 2: Corresponding labels
y = ['normal', 'tachycardia', 'bradycardia', 'normal', 'tachycardia', 'bradycardia']

# ✅ Step 3: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# ✅ Step 4: Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ Step 5: Make predictions and evaluate
predictions = model.predict(X_test)
print("🔍 Classification Report:")
print(classification_report(y_test, predictions))
