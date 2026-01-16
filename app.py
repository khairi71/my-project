import streamlit as st
import pandas as pd

st.title("Работа с CSV файлом")

# Читаем файл, который лежит в том же репозитории
df = pd.read_csv("data.csv")

# Выводим таблицу
st.write("Данные из файла:")
st.dataframe(df)
