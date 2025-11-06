from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Sample loan applicant data: [income, credit_score, loan_amount, years_employed]
X = [
    [50000, 700, 10000, 5],
    [30000, 600, 8000, 2],
    [80000, 750, 20000, 10],
    [25000, 580, 5000, 1],
    [60000, 720, 15000, 6],
    [40000, 650, 12000, 3]
]

# Labels: 1 = Approved, 0 = Rejected
y = [1, 0, 1, 0, 1, 0]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
print("🔍 Classification Report:")
print(classification_report(y_test, predictions))

# Example prediction
new_applicant = [[45000, 690, 9000, 4]]
decision = model.predict(new_applicant)
print("✅ Loan Approved" if decision[0] == 1 else "❌ Loan Rejected")