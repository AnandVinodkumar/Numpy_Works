import streamlit
import numpy
import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pandas.read_csv("C:/Users/Anand Vinodkumar/Desktop/Numpy Works/New_Diabetes/diabetes.csv")
df = pandas.DataFrame(data)

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

knn = KNeighborsClassifier()

model = knn.fit(X_train,Y_train)

y_pred = model.predict(X_test)

print(accuracy_score(y_pred,Y_test))

def input_features():

    preg = streamlit.number_input("Enter no of pregnancies",0,20,1)
    gluc = streamlit.number_input("Enter glucose value",0,300,120)
    bp = streamlit.number_input("Enter BP value",0,122,70)
    skinthick = streamlit.number_input("Enter Skinthick value",0,100,20)
    insulin = streamlit.number_input("Enter Insulin value",0,900,80)
    bmi = streamlit.number_input("Enter BMI value",0,70,25)
    dpf = streamlit.number_input("Enter DiabetesPedigreeFunction value",0,3,1)
    age = streamlit.number_input("Enter the age",1,120,33)

    data = {
        "Pregnancies" : preg,
        "Glucose" : gluc,
        "BloodPressure" : bp,
        "SkinThickness" : skinthick,
        "Insulin" : insulin,
        "BMI" : bmi,
        "DiabetesPedigreeFunction" : dpf,
        "Age" : age
    }

    input_df = pandas.DataFrame(data,index=[0])
    return input_df

features = input_features()

scaled_features = scaler.transform(features)

result = model.predict(scaled_features)
print(result)
if streamlit.button("Show Result"):
    final_result = "You have diabetes" if result[0] == 1 else "You do not have diabetes"
    streamlit.success(final_result)