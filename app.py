# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st 
import joblib as jb

import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn.model_selection import cross_val_score

model = jb.load('modelo.pk1')

#Cabecalho
st.subheader("Informações dos dados")

#Nome do usuário
user_input = st.sidebar.text_input("Digite seu nome")
st.write("Paciente: ", user_input)

def get_user_data():
    Idade = st.sidebar.slider("Idade", 18,120,30)
    TOT = st.radio("TOT", ["sim", "nao"])
    SVD = st.radio("SVD", ["sim", "nao"])
    PAI = st.radio("PAI", ["sim", "nao"])
    Infeccao = st.radio("Infeccao", ["sim", "nao"])
    CVC = st.radio("CVC", ["sim", "nao"])
    Sedacao = st.radio("Sedacao", ["sim", "nao"])
    Comorbidade = st.radio("Comorbidade", ["sim", "nao"])
    SAPS = st.sidebar.slider("SAPS", 0,200,55)
    Temperatura = st.sidebar.slider("Temperatura", 34,40,36)
    PAS = st.sidebar.slider("PAS", 60,300,130)
    FC = st.sidebar.slider("FC", 40,200,90)
    Creatinina = st.sidebar.slider("Creatinina", 0.1,20.0,1.1)
    
    user_data = {"Idade": Idade,
                "TOT": TOT,
                "SVD": SVD,
                "PAI": PAI,
                "Infeccao": Infeccao,
                "CVC": CVC,
                "Sedacao": Sedacao,
                "Comorbidade": Comorbidade,
                "SAPS": SAPS,
                "Temperatura": Temperatura,
                "PAS": PAS,
                "FC": FC,
                "Creatinina": Creatinina,
                }
    features = pd.DataFrame(user_data, index = [0])
                           
    categoriaColuna = ["TOT", "SVD", "PAI", "Infeccao", "CVC", "Sedacao", "Comorbidade"]
    for coluna in categoriaColuna:
      features = pd.concat([features, pd.get_dummies(features[coluna], prefix=coluna)], axis=1)
      features = features.drop(columns=[coluna])
    return features

user_input_variables = get_user_data()

#Gráfico
graf = st.bar_chart(user_input_variables)

st.subheader("Dados do usuario")
st.write(user_input_variables)

#Predicao
prediction = model.predict(user_input_variables)
st.subheader("Previsão: ")
st.write(prediction)

#0 = não tem pretensão a ter
#1 = tem pretensão

