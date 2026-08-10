# 🍷 WinePredictor

## 📌 Project Overview

winepredictor is a Machine Learning classification project that uses the **K-Nearest Neighbors (KNN)** algorithm to classify wine into different classes.

In this project, the KNN model is created with a fixed **K value of 9** and its classification accuracy is calculated.

## 🎯 Objective

* Load the Wine dataset from a CSV file.
* Clean the dataset by removing missing values.
* Separate input features and the target class.
* Split the dataset into training and testing data.
* Scale the input features.
* Build a KNN classification model with **K = 9**.
* Train and test the model.
* Calculate the model accuracy.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* K-Nearest Neighbors (KNN)
* StandardScaler

## 🔄 Project Workflow

```text
Wine Dataset
     ↓
Load Dataset
     ↓
Clean Dataset
     ↓
Separate Features & Class
     ↓
Train-Test Split
     ↓
Feature Scaling
     ↓
KNN Model (K = 9)
     ↓
Train Model
     ↓
Predict Classes
     ↓
Calculate Accuracy
```

## 📂 Dataset

The project uses:

```text
WinePredictor.csv
```

The target column is:

```text
Class
```

All other columns are used as input features.

## 🤖 Algorithm Used

### K-Nearest Neighbors (KNN)

KNN is a Machine Learning classification algorithm that predicts the class of a data point based on its nearest neighbors.

For this project, the model is configured with:

```python
K = 9
```

The model is then trained using the scaled training data and used to predict the classes of the test data.

## 📊 Model Evaluation

The model performance is evaluated using **Accuracy Score**.

```python
accuracy_score(Y_test, Y_pred)
```

The final accuracy is displayed as a percentage.

## 📦 Requirements

* Python 3.x
* Pandas
* Scikit-learn

Install the required libraries:

```bash
pip install pandas scikit-learn
```

## ▶️ How to Run

### 1. Keep the dataset in the project folder

```text
WinePredictor.csv
```

### 2. Run the Python program

```bash
python Wine_K9.py
```

## 💡 Key Feature

The key feature of this project is the use of a **fixed K value of 9** in the KNN classification model.

```python
KNeighborsClassifier(n_neighbors=9)
```

## 👩‍💻 Author

**Shreya Jagtap**

B.Sc. Data Science & Artificial Intelligence
