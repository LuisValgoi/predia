import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dropout
from keras.wrappers.scikit_learn import KerasRegressor

st.beta_set_page_config(
	layout="wide",
	initial_sidebar_state="expanded",
	page_title='PREDIA – Modelo Híbrido Multifatorial',
	page_icon=None,
)

# função para carregar o dataset
@st.cache
def get_data():
    data = pd.read_csv("model/dataset.csv")
    return data

# função para retornar as colunas necessarias para o lstm
def get_features_to_drop_lstm():
    return ['DATA', 'VENDAS', 'SEMANA_PAGAMENTO', 'PRECIPITACAO', 'TEMPERATURA', 'POS_DATA_FESTIVA', 'FDS', 'VESPERA_DATA_FESTIVA', 'ALTA_TEMPORADA']

# funcao para retornar o modelo base de lstm
def get_base_model_lstm():
    lstm = Sequential()
    lstm.add(LSTM(190, return_sequences=True))
    lstm.add(Dropout(0.2))
    lstm.add(LSTM(190, return_sequences=True))
    lstm.add(Dropout(0.2))
    lstm.add(LSTM(190, return_sequences=False))
    lstm.add(Dropout(0.2))
    lstm.add(Dense(1))
    lstm.compile(loss='mean_squared_error', optimizer='adam')
    return lstm

# função para treinar o modelo lstm
def train_model_lstm():
    # # separa o dataset em treino e teste
    # data = get_data()
    # x = data.drop(columns=get_features_to_drop_lstm(),axis=1)
    # y = data["VENDAS"]
    # X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=1, shuffle=False)

    # # realiza o feature scaling
    # scaler = preprocessing.MinMaxScaler()
    # X_train = scaler.fit_transform(X_train)
    # X_test = scaler.transform(X_test)

    # # reshape to 3D
    # X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
    # X_train = np.array(y_train).reshape((y_train.shape[0], 1, y_train.shape[1]))
    # X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

    # # instancia o modelo
    # lstm_regressor = KerasRegressor(build_fn=get_base_model_lstm)

    # # treina o modelo
    # lstm_regressor.fit(X_train, y_train, epochs=200, batch_size=20, shuffle=False, verbose=False)

    # # retorna
    # return lstm_regressor

    return None

# função para retornar as colunas necessarias para o gb
def get_features_to_drop_gb():
    return ['DATA', 'VENDAS', 'SEMANA_PAGAMENTO', 'PRECIPITACAO', 'FDS', 'UMIDADE', 'TEMPERATURA', 'VESPERA_DATA_FESTIVA', 'FDS', 'UMIDADE', 'TEMPERATURA', 'VESPERA_DATA_FESTIVA', 'POS_DATA_FESTIVA']

# função para treinar o modelo gb
def train_model_gb():
    # separa o dataset em treino e teste
    data = get_data()
    x = data.drop(columns=get_features_to_drop_gb(), axis=1)
    y = data["VENDAS"]
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.05, random_state=1, shuffle=False)

    # instancia o modelo
    gb_regressor = GradientBoostingRegressor(alpha=0.9, ccp_alpha=0.0, criterion='mse', init=None,
                                             learning_rate=0.1, loss='ls', max_depth=25,
                                             max_features=None, max_leaf_nodes=None,
                                             min_impurity_decrease=0.0, min_impurity_split=None,
                                             min_samples_leaf=21, min_samples_split=16,
                                             min_weight_fraction_leaf=0.0, n_estimators=139,
                                             n_iter_no_change=None, presort='deprecated',
                                             random_state=1, subsample=1.0, tol=0.0001,
                                             validation_fraction=0.1, verbose=0, warm_start=False)

    # realiza o feature scaling
    scaler = preprocessing.MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # treina o modelo
    gb_regressor.fit(X_train, y_train)

    # retorna
    return gb_regressor

# função para retornar as colunas necessarias para o mlp
def get_features_to_drop_mlp():
    return ['DATA', 'VENDAS', 'SEMANA_PAGAMENTO', 'PRECIPITACAO', 'QTD_CONCORRENTES', 'VESPERA_DATA_FESTIVA', 'FDS', 'QTD_CONCORRENTES', 'VESPERA_DATA_FESTIVA', 'FDS', 'ALTA_TEMPORADA']

# função para treinar o modelo mlp
def train_model_mlp():
    # separa o dataset em treino e teste
    data = get_data()
    x = data.drop(columns=get_features_to_drop_mlp(), axis=1)
    y = data["VENDAS"]
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.05, random_state=1, shuffle=False)

    # instancia o modelo
    mlp_regressor = MLPRegressor(activation='identity', alpha=0.0001, batch_size=300, beta_1=0.9,
                                 beta_2=0.999, early_stopping=True, epsilon=1e-08,
                                 hidden_layer_sizes=(149), learning_rate='constant',
                                 learning_rate_init=0.001, max_fun=15000, max_iter=100,
                                 momentum=0.9, n_iter_no_change=10, nesterovs_momentum=True,
                                 power_t=0.5, random_state=1, shuffle=False, solver='lbfgs',
                                 tol=0.0001, validation_fraction=0.1, verbose=False,
                                 warm_start=True)

    # realiza o feature scaling
    scaler = preprocessing.MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # treina o modelo
    mlp_regressor.fit(X_train, y_train)

    # retorna
    return mlp_regressor

########################################################################

# criando um dataframe
data = get_data()

# treinando os modelos
LSTM = train_model_lstm()
GB = train_model_gb()
MLP = train_model_mlp()

########################################################################

# título
st.title("PREDIA – Modelo Híbrido Multifatorial")
# subtítulo
st.markdown("App utilizado para exibir a solução de Machine Learning construída para a predição de almoços do Restaurante Nostra Bréscia.")

########################################################################

# verificando o dataset
st.subheader("Selecionando apenas um pequeno conjunto de atributos")
allcols = ['DATA', 'VENDAS', 'FDS', 'DATA_FESTIVA', 'VESPERA_DATA_FESTIVA', 'POS_DATA_FESTIVA', 'FERIADO', 'ALTA_TEMPORADA', 'QTD_CONCORRENTES', 'TEMPERATURA', 'UMIDADE', 'VENDAS_ONTEM']
defaultcols = ['DATA', 'VENDAS', 'FDS', 'DATA_FESTIVA', 'FERIADO', 'ALTA_TEMPORADA', 'QTD_CONCORRENTES', 'TEMPERATURA', 'VENDAS_ONTEM']
cols = st.multiselect("Atributos", allcols, default=defaultcols)
st.dataframe(data[cols].head(10))

########################################################################

# plot a distribuição dos dados
st.subheader("Distribuição vendas por período")
faixa_valores = st.slider("Faixa de Vendas de Almoços", int(data.VENDAS.min()), int(data.VENDAS.max()), (100, 150))
dados = data[data['VENDAS'].between(left=faixa_valores[0], right=faixa_valores[1])]

f1 = px.histogram(dados, x="DATA", y="VENDAS", nbins=100,title="Distribuição de Vendas de Almoço")
f1.update_xaxes(title="Período")
f1.update_yaxes(title="Almoços Vendidos")
st.plotly_chart(f1)

########################################################################

# plot a relação de VENDAS x FERIADO
st.subheader("Relação de Almoços Vendidos por Quantidade de Concorrentes Abertos")
f7 = px.box(dados, x="QTD_CONCORRENTES", y="VENDAS",color="QTD_CONCORRENTES", notched=True)
f7.update_xaxes(title="Quantidade de Concorrentes Abertos")
f7.update_yaxes(title="Almoços Vendidos")
st.plotly_chart(f7)

########################################################################

# plot a relação de VENDAS x FERIADO
st.subheader("Relação de Almoços Vendidos por Temperatura")
f8 = px.box(dados, x="TEMPERATURA", y="VENDAS",color="TEMPERATURA", notched=True)
f8.update_xaxes(title="Temperatura")
f8.update_yaxes(title="Almoços Vendidos")
st.plotly_chart(f8)

########################################################################

# plot a relação de VENDAS x FDS
st.subheader("Relação de Almoços Vendidos por Finais de Semanas")
f2 = px.box(dados, x="FDS", y="VENDAS", color="FDS", notched=True)
f2.update_xaxes(title="Finais de Semana")
f2.update_yaxes(title="Almoços Vendidos")
st.plotly_chart(f2)

########################################################################

# plot a relação de VENDAS x FERIADO
st.subheader("Relação de Almoços Vendidos por Feriados")
f3 = px.box(dados, x="FERIADO", y="VENDAS",color="FERIADO", notched=True)
f3.update_xaxes(title="Feriados")
f3.update_yaxes(title="Almoços Vendidos")
st.plotly_chart(f3)

########################################################################

# plot a relação de VENDAS x VESPERA_DATA_FESTIVA
st.subheader("Relação de Almoços Vendidos por Vésperas de Datas Festivas")
f4 = px.box(dados, x="VESPERA_DATA_FESTIVA", y="VENDAS",color="VESPERA_DATA_FESTIVA", notched=True)
f4.update_xaxes(title="Vésperas de Datas Festivas")
f4.update_yaxes(title="Almoços Vendidos")
st.plotly_chart(f4)

########################################################################

# plot a relação de VENDAS x POS_DATA_FESTIVA
st.subheader("Relação de Almoços Vendidos por Dias Após Datas Festivas")
f5 = px.box(dados, x="POS_DATA_FESTIVA", y="VENDAS",color="POS_DATA_FESTIVA", notched=True)
f5.update_xaxes(title="Dias Após Datas Festivas")
f5.update_yaxes(title="Almoços Vendidos")
st.plotly_chart(f5)

########################################################################

# plot a relação de VENDAS x FERIADO
st.subheader("Relação de Almoços Vendidos por Alta Temporada")
f6 = px.box(dados, x="ALTA_TEMPORADA", y="VENDAS",color="ALTA_TEMPORADA", notched=True)
f6.update_xaxes(title="Alta Temporada")
f6.update_yaxes(title="Almoços Vendidos")
st.plotly_chart(f6)

########################################################################

html = """
  <style>
    .sidebar .sidebar-content {
        padding: 2rem 1rem;
    }

    .reportview-container .main .block-container {
        padding: 2rem 1rem 10rem;
    }
  </style>
"""
st.markdown(html, unsafe_allow_html=True)

st.sidebar.title("Simule uma predição")
st.sidebar.subheader("Fatores Histórico")
VENDAS_ONTEM = st.sidebar.number_input("Quantos almoços foram vendidos ontem?", value=int(data.VENDAS_ONTEM.mean()), step=1)
st.sidebar.subheader("Fatores da Concorrência")
QTD_CONCORRENTES = st.sidebar.number_input("Quantos concorrentes estarão abertos?", value=int(data.QTD_CONCORRENTES.max()), step=1)
st.sidebar.subheader("Fatores de Natureza")
TEMPERATURA = st.sidebar.number_input("Qual a previsão de temperatura (em °C)?", value=int(data.TEMPERATURA.mean()), step=5)
UMIDADE = st.sidebar.number_input("Qual a previsão de umidade?", value=int(data.UMIDADE.mean()), step=5)
st.sidebar.subheader("Fatores do Local")
FERIADO = st.sidebar.selectbox("Será um feriado?", ("Sim", "Não"))
ALTA_TEMPORADA = st.sidebar.selectbox("Será uma data de alta temporada (Março à Dezembro) ?", ("Sim", "Não"))
DATA_FESTIVA = st.sidebar.selectbox("Será uma data festiva?", ("Sim", "Não"))
POS_DATA_FESTIVA = st.sidebar.selectbox("Será após uma data festiva?", ("Sim", "Não"))

# transformando o dado de entrada em valor binário
FERIADO = 1 if FERIADO == "Sim" else 0
ALTA_TEMPORADA = 1 if ALTA_TEMPORADA == "Sim" else 0
DATA_FESTIVA = 1 if DATA_FESTIVA == "Sim" else 0
POS_DATA_FESTIVA = 1 if POS_DATA_FESTIVA == "Sim" else 0

########################################################################

# inserindo um botão na tela
btn_predict = st.sidebar.button("Realizar Predição")

# verifica se o botão foi acionado
if btn_predict:
    # lstm_features = []
    # lstm_features.append(DATA_FESTIVA)
    # lstm_features.append(FERIADO)
    # lstm_features.append(QTD_CONCORRENTES)
    # lstm_features.append(UMIDADE)
    # lstm_features.append(VENDAS_ONTEM)
    # lstm_y_pred = LSTM.predict(scaler.transform([lstm_features])).round().astype(int)[0]

    x = data.drop(columns=get_features_to_drop_gb(), axis=1)
    y = data["VENDAS"]
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=1, shuffle=False)
    scaler = preprocessing.MinMaxScaler()
    scaler.fit_transform(X_train)
    gb_features = []
    gb_features.append(ALTA_TEMPORADA)
    gb_features.append(DATA_FESTIVA)
    gb_features.append(FERIADO)
    gb_features.append(QTD_CONCORRENTES)
    gb_features.append(VENDAS_ONTEM)
    gb_features = scaler.transform([gb_features])
    gb_y_pred = GB.predict(gb_features).round().astype(int)[0]

    x = data.drop(columns=get_features_to_drop_mlp(), axis=1)
    y = data["VENDAS"]
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=1, shuffle=False)
    scaler = preprocessing.MinMaxScaler()
    scaler.fit_transform(X_train)
    mlp_features = []
    mlp_features.append(DATA_FESTIVA)
    mlp_features.append(FERIADO)
    mlp_features.append(POS_DATA_FESTIVA)
    mlp_features.append(TEMPERATURA)
    mlp_features.append(UMIDADE)
    mlp_features.append(VENDAS_ONTEM)
    mlp_features = scaler.transform([mlp_features])
    mlp_y_pred = MLP.predict(mlp_features).round().astype(int)[0]

    qtd_almoco_ensemble = (gb_y_pred + mlp_y_pred) / 2

    # printa o texto
    st.sidebar.subheader(f"SERÃO VENDIDOS CERCA DE {int(round(qtd_almoco_ensemble))} ALMOÇOS")
