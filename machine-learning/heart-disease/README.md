# Heart-Disease-Prediction

A web application which uses Machine Learning models to predict the heart condition of a user by providing some inputs about the user's health like age, blood pressure, cholesterol level etc.

It uses a regression model to analyze the parameters explained below and predicts whether the user is diagnosed with heart disease or not. The model is trained using a dataset provided by Kaggle. Our model upon training gives an accuracy of nearly 85% which we plan to improve further.

## Attributes
- age
- sex
- chest pain type (4 values)[typical angina(0)/atypical angina(1)/non-anginal pain(2)/asymptotic(3)]
- resting blood pressure
- serum cholestoral in mg/dl
- fasting blood sugar > 120 mg/dl(yes/no)
- resting electrocardiographic results (Normal(0),ST-Wave Abnormality(1),left ventricular hypertrophy(2))
- maximum heart rate achieved
- exercise induced angina
- oldpeak = ST depression induced by exercise relative to rest
- the slope of the peak exercise ST segment
- number of major vessels (0-3) colored by flourosopy
- thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

## Model
After trying each  mehod as described below, and getting the respective accuracies:

|Model|Accuracy|
----------------
|Logistic Regression|~86%|
|Support Vector Machines|~80%|
|K-Nearest-Neighbors|~84%|
|Decision Tree|~84%|
|Random Forest|~85%|

We are using the **Logistic Regression model** and getting an accuracy of **86.78%**.

## Authors of the database
We hereby thank them for their efforts for creating and making the dataset accessible.

Creators:
1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.

Donor:
* David W. Aha (aha '@' ics.uci.edu) (714) 856-8779