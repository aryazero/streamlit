import streamlit as st
import pandas as pd 
import numpy as np 
from streamlit_option_menu import option_menu

option = st.sidebar.selectbox(
    'Menu :',
    ('Home','Dataframe')
)

if option == 'Home' or option == '':
    st.write("""# Test""") #menampilkan halaman utama
elif option == 'Dataframe':
    st.write("""## Dataframe""") #menampilkan judul halaman dataframe

    df = pd.read_csv('./diabetes_latih.csv')

    X_train = df.values
    X_train = np.delete(X_train,8, axis=1)
    
    y_train = df['Outcome'].values
    
    df = pd.read_csv('./diabetes_uji.csv')
    
    X_test = df.values
    X_test = np.delete(X_test,8,axis=1)
    
    y_test = df['Outcome'].values

    from keras.models import Sequential
    from keras.layers import Dense
    
    model = Sequential()
    
    model.add(Dense(12, activation='relu', input_shape=(8,)))
    
    model.add(Dense(8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    df.head()
