import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("schools_combined.csv")

my_page = st.sidebar.radio("Page Navigation",["Page 1","Page 2","Page 3","Page 4","Page 5"])

if my_page == "Page 1":
st.title("Data")

st.header("Public School Data in the Philippines")

st.write(df.head())


data_load_state = st.text("Loading....")

st.write(df.head(30))

data_load_state.markdown("Loading....***done***!")

grade_level = df.groupby("year_level")["enrollment"].sum()



data_load_state = st.text("Loading....")
# indicates if plotting on the figues or on subplots
fig = plt.figure(figsize=(8,6))

# the main code to create the graph
plt.bar(grade_level.index, grade_level.values)

# additional elements that can be customzed
plt.title("Students in Public Schools", fontsize=16)
plt.ylabel("Number of Enrollees", fontsize=12)
plt.xlabel("Year Level", fontsize=12)
year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
        "first year", "second year", "third year", "fourth year"]
plt.xticks(range(len(grade_level.index)), year, rotation=45)

# display graph
plt.show()
st.pyplot(fig)
data_load_state.markdown("Loading....***done***!")

if st.checkbox("check",value=False):
    st.subheader("Data")
    data_load_state = st.text("Loading...")
    st.write(df.head(20))
    data_load_state.markdown("Loading....***done***!")

# option = st.selectbox(
#     'Which region do you want to see?',
#      df['region'].unique())
# 'You selected: ', option

option = st.sidebar.selectbox(
    'Which region do you want to see?',
     df['region'].unique())
'You selected: ', option
grade_level = df[df["region"]==option].groupby("year_level")["enrollment"].sum()

fig = plt.figure(figsize=(8,6))

# the main code to create the graph
plt.bar(grade_level.index, grade_level.values)

# additional elements that can be customzed
plt.title("Students in Public Schools", fontsize=16)
plt.ylabel("Number of Enrollees", fontsize=12)
plt.xlabel("Year Level", fontsize=12)
year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
        "first year", "second year", "third year", "fourth year"]
plt.xticks(range(len(grade_level.index)), year, rotation=45)

# display graph
plt.show()
st.pyplot(fig)
