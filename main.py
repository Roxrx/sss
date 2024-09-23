from turtle import width
import streamlit as st
import random

st.title('Лабораторная работа №1')
st.subheader('Исследование кислотного аккумулятора')
st.header('Цель работы')
st.text('Изучить схемы построения и работу выпрямительных устройств.')



st.text('Рисунок 1. Схема однополупериодного выпрямителя')


st.text('Рисунок 2 - Двух-полупериодный выпрямитель с нулевой точкой')
RLoad = st.slider("Сопротивление нагрузки", 0.01, 2.2, 1.0)
st.write("Сопротивление нагрузки", RLoad, 'Ом')
ILoad = 2.2/(RLoad+0.02)
st.write("Ток разряда", ILoad, 'А')
st.write("Напряжение разряда", RLoad*ILoad, 'U')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
idx = random.randint(1,100)
st.write("Рандомное число", idx)

st.write("---")

col1, col2 = st.columns (2)
col1.write ('Рисунок 1. Схема однополупериодного выпрямителя')


col2.write ('Рисунок 2 - Двух-полупериодный выпрямитель с нулевой точкой')

