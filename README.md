Loan Data Analytics ETL and Power BI Visualization Project

This project focuses on building a complete data pipeline for loan prediction and analysis by integrating data engineering, machine learning, and business intelligence.

The project addresses a real-world problem faced by financial institutions—enhancing the loan approval process, minimizing default risk, and gaining insights into applicant behavior through data.

The pipeline includes the following stages:

1. Data Extraction
Raw loan applicant data in CSV format was extracted using Python’s pandas library. Key fields included gender, marital status, dependents, education, employment status, applicant and co-applicant income, loan amount, loan term, credit history, property area, and loan status. An initial inspection was performed to detect missing values, inconsistent formats, and outliers.

2. Data Transformation
Missing values were imputed using the mode for categorical variables (e.g., gender, self_employed) and the median for numerical variables (e.g., LoanAmount, Loan_Amount_Term). Categorical features were encoded using label encoding (for the target variable) and one-hot encoding (for features such as education and property area). The cleaned and transformed dataset was then prepared for loading.

3. Data Loading
A connection was established between Python and a local PostgreSQL database using SQLAlchemy. The processed dataset was uploaded to a new PostgreSQL table using pandas’ .to_sql() method. This enabled structured storage, query capabilities, and integration with BI tools.

4. Machine Learning Modeling
The dataset was split into training and test sets (70–30 ratio) using scikit-learn. A logistic regression model was selected due to its simplicity and suitability for binary classification tasks. Independent variables included numerical and encoded categorical attributes. The model achieved approximately 76% accuracy on the test dataset using the accuracy_score metric.






5. Visualization with Power BI
Power BI was connected to the PostgreSQL database to enable real-time data access. An interactive dashboard was created with ten visualizations highlighting applicant characteristics, approval rates, credit history impact, and income-to-loan relationships. These visualizations support business users in making informed decisions.

 ![image](https://github.com/user-attachments/assets/5c6f079f-7189-47b7-b059-98ac0c57dace)


Business Value
Automates the loan data pipeline from raw extraction to actionable insights.
Enhances decision-making accuracy through predictive modeling.
Supports strategic planning and bias mitigation via transparent reporting dashboards.
Demonstrates the integration of Python, SQL, machine learning, and Power BI for practical business problem-solving.

This project reflects the application of data analytics, machine learning, and visualization in addressing operational challenges in the financial sector.
