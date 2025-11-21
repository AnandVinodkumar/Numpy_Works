import streamlit
import seaborn
from matplotlib import pyplot
import pandas

data = {"subjects": ["Maths", "Physics", "Biology"],
        "marks": [90, 80, 85]
}

pyplot.figure(figsize=(2,2))

seaborn.barplot(data=data,x="subjects",y="marks")

streamlit.pyplot(pyplot)