import pandas as pd
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data from CSV
df = pd.read_csv("data/train_u6lujuX_CVtuZ9i.csv")
print("Current columns:", df.columns.tolist())

# Clean data
df.dropna(inplace=True)  # Drop rows with missing values

# Replace Loan_Status values
df['Loan_Status'] = df['Loan_Status'].replace({'Y': 1, 'N': 0})

# Store Loan_ID separately in case needed
loan_ids = df['Loan_ID']

# Drop Loan_ID before encoding
df.drop(['Loan_ID'], axis=1, inplace=True)

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df, drop_first=True)

# Define features and target
X = df_encoded.drop('Loan_Status', axis=1)
y = df_encoded['Loan_Status']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Connect to PostgreSQL and load original cleaned data
from sqlalchemy import create_engine

# Define connection string for SQLAlchemy
engine = create_engine("postgresql+psycopg2://postgres:ABCD@localhost:5432/loan_prediction")

# Save data to PostgreSQL using SQLAlchemy
table_name = "loan_data_cleaned"
df_encoded.to_sql(table_name, con=engine, if_exists='replace', index=False)

print("Data successfully loaded into PostgreSQL!")

print("ETL complete and model trained.")
