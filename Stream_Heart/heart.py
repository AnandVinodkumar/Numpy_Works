import streamlit
import numpy
import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

data = pandas.read_csv("C:/Users/Anand Vinodkumar/Desktop/Numpy Works/Stream_Heart/heart (1).csv")
df = pandas.DataFrame(data)

df = df.drop(columns=['Age','Sex'])

le = LabelEncoder()

df['ChestPainType'] = le.fit_transform(df['ChestPainType'])
df['RestingECG'] = le.fit_transform(df['RestingECG'])
df['ExerciseAngina'] = le.fit_transform(df['ExerciseAngina'])
df['ST_Slope'] = le.fit_transform(df['ST_Slope'])

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

streamlit.header("Heart Disease Prediction")

def input_features():

    cpt = streamlit.text_input("Enter your Chest Pain Type","")
    rbp = streamlit.number_input("Enter your Resting BP",0,250,0)
    chol = streamlit.number_input("Enter your cholestrol",0,650,0)
    fbs = streamlit.number_input("Enter your Fasting BS",0,1,0)
    recg = streamlit.text_input("Enter your Resting ECG (Y/N)","")
    mhr = streamlit.number_input("Enter your Maximum HR",60,210,60)
    ea = streamlit.text_input("Enter your Exercise Angina","")
    op = streamlit.number_input("Enter your Oldpeak",-2.5,6.5,-2.5)
    st = streamlit.text_input("Enter your ST_Slope value","")

    data = {
        "ChestPainType" : cpt,
        "RestingBP" : rbp,
        "Cholesterol" : chol,
        "FastingBS" : fbs,
        "RestingECG" : recg,
        "MaxHR" : mhr,
        "ExerciseAngina" : ea,
        "Oldpeak" : op,
        "ST_Slope" : st
    }

    input_df = pandas.DataFrame(data,index=[0])
    print(input_df)
    return input_df

features = input_features()

features['ChestPainType'] = le.fit_transform(features['ChestPainType'])
features['RestingECG'] = le.fit_transform(features['RestingECG'])
features['ExerciseAngina'] = le.fit_transform(features['ExerciseAngina'])
features['ST_Slope'] = le.fit_transform(features['ST_Slope'])

scaled_features = scaler.transform(features)

result = model.predict(scaled_features)

if streamlit.button("Predict"):

    final_result = "You have Heart Disease" if result[0] == 1 else "You do not have Heart Disease"
    streamlit.success(final_result)
