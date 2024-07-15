# Import necessary libraries
# Importing the required libraries for data manipulation, model training, and saving the model.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

# Load the dataset
# Loading the dataset from a CSV file.
dataset = pd.read_csv("Salary_Data.csv")

# Display the dataset
# Displaying the dataset to ensure it’s loaded correctly.
dataset

# Split input (YearsExperience) and output (Salary)
# Separating the features (YearsExperience) and target variable (Salary).
inputData = dataset[["YearsExperience"]]
outputData = dataset[["Salary"]]

# Split the data into training and testing sets (70% training, 30% testing)
# Dividing the dataset into training and testing sets with a 70-30 split ratio.
X_train, X_test, y_train, y_test = train_test_split(inputData, outputData, test_size=0.30, random_state=0)

# Instantiate the Linear Regression model
# Creating an instance of the Linear Regression model.
regressor = LinearRegression()

# Train the model using the training data
# Training the model with the training data.
regressor.fit(X_train, y_train)

# Get the slope (weight) of the regression line
# Retrieving the slope (weight) of the regression line.
weight = regressor.coef_
weight

# Get the bias (intercept) of the regression line
# Retrieving the bias (intercept) of the regression line.
bias = regressor.intercept_
bias

# Predict the test set results
# Predicting the salaries for the test set.
y_pred = regressor.predict(X_test)

# Calculate the R-squared score to evaluate the model performance
# Evaluating the model performance using the R-squared score.
r_score = r2_score(y_test, y_pred)
r_score

# Save the trained model to disk
# Saving the trained model to a file using pickle.
filename = "finalized_model_linear.sav"
pickle.dump(regressor, open(filename, 'wb'))

# Load the saved model to check
#Loading the saved model to verify it was saved correctly.
loaded_model = pickle.load(open("finalized_model_linear.sav", "rb"))

# Make a prediction using the loaded model for 15 years of experience
# Using the loaded model to predict the salary for an individual with 15 years of experience.
result = loaded_model.predict([[15]])
result
