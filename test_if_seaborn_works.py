
import streamlit as st
import seaborn as sns


penguins = sns.load_dataset("penguins")

st.title("Hello")
# fig = sns.pairplot(penguins, hue="species")
fig = sns.displot(penguins, x="flipper_length_mm", hue="species", kind="kde", fill=True)

st.pyplot(fig)
