import streamlit
import pandas
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pandas.read_csv("C:/Users/Anand Vinodkumar/Desktop/Numpy Works/Mushrooms/mushrooms.csv")
df = pandas.DataFrame(data)
print(df)