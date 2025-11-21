import streamlit
import seaborn
from matplotlib import pyplot
import pandas

x = [4,5,6,7,8]

y = [5,7,9,11,13]

# seaborn.scatterplot(x=x,y=y)

pyplot.figure(figsize=(2,2))

seaborn.scatterplot(x=x,y=y)

streamlit.pyplot(pyplot)