import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import streamlit as st
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind
import statsmodels.api as sm
from io import StringIO

def anotherfunction(data_frame):
    selected_parameter1 = st.selectbox("Выберите параметр 1", data_frame.columns, key = "<6>")
    sel1_cat = st.checkbox('Категориальная переменная 1', key = "<1>")
    selected_parameter2 = st.selectbox("Выберите параметр 2", data_frame.columns, key = "<7>")
    sel2_cat = st.checkbox('Категориальная переменная 2', key = "<2>")

    
    if st.button('Получить', key = "<5>"):
        fig, (ax0, ax1) = plt.subplots(nrows=2, ncols=1)
        if sel1_cat:
            category_column = data_frame[selected_parameter1]
            category_counts = category_column.value_counts()
            ax0.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%")
            ax0.axis('equal')
            ax0.set_title(selected_parameter1)
        else:
            ax0.hist(data_frame[selected_parameter1], bins='auto')
            ax0.set_title(selected_parameter1)
        
        if sel2_cat:
            category_column = data_frame[selected_parameter2]
            category_counts = category_column.value_counts()
            ax1.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%")
            ax1.axis('equal')
            ax1.set_title(selected_parameter2)
        else:
            ax1.hist(data_frame[selected_parameter2], bins='auto')
            ax1.set_title(selected_parameter2)
        fig.tight_layout()

        st.pyplot(plt)
    sd = st.selectbox("Выберите метод",["t-test", "u-test"], key = "<4>")
    if st.button('Вычислить', key = "<3>"):
        if sd == "t-test":
            tstat, pvalue, df = sm.stats.ttest_ind(
                data_frame[selected_parameter1], data_frame[selected_parameter2])
            st.write("t-statistic:", tstat)
            st.write("p-value:", pvalue)
        elif sd == "u-test":
            u_statistic, p_value = mannwhitneyu(data_frame[selected_parameter1], data_frame[selected_parameter2], method="auto")
            st.write("U-statistic:", u_statistic)
            st.write("p-value:", p_value)

def run():
    st.title("Аттестация")
    uploaded_file = st.file_uploader("Загрузите набор данных")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
        anotherfunction(dataframe) 
       
    
if __name__=='__main__':
    run()
