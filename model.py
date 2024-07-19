import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data from CSV into a pandas DataFrame
data = pd.read_csv('dataset_jarak_langkah.csv')

# Assuming 'X' contains the features and 'y' contains the target variable
X = data[["Jarak (cm)" ,"Jarak Langkah (cm)"]]  # Replace with your feature columns
y = data['Jumlah Langkah']  # Replace with your target column

# Split the data into training and t
# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X, y)