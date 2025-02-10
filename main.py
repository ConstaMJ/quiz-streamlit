import streamlit as st
import time

st.set_page_config(page_title="Quiz Interativo", page_icon="😎", layout="centered")
st.title("Jogo de perguntas e respostas")

perguntas = [
  {"pergunta": "Qual e a capital de Mocambique?", "opcoes": ["Manica", "Beira", "Maputo", "Lilongwe"], "resposta": "Maputo"},
  {"pergunta": "Consta MJ esta frequentando que curso no IIMa?", "opcoes": ["Electricidade de Manutencao Industrial", "Tecnico de Construcao Civil", "Engenharia Informatica", "Mecanica de Manutencao Industrial"], "resposta": "Tecnico de Construcao Civil"},
{"pergunta": "Em que ano o Consta MJ comecou a estudar no IIMa?", "opcoes": ["2022", "2023", "2024", "2025"], "resposta": "2024"}
]

if "pontuacao" not in st.session_state:
  st.session_state.pontuacao = 0
if "pergunta_atual" not in st.session_state:
  st.session_state.pergunta_atual = 0
if "tempo_restante" not in st.session_state:
  st.session_state.tempo_restante = 30
if "respondido" not in st.session_state:
  st.session_state.respondido = False

def atualizar_temporizador():
  if st.session_state.tempo_restante > 0 and not st.session_state.respondido:
    time.sleep(1)
    st.session_state.tempo_restante -= 1
    st.rerun()
  elif st.session_state.tempo_restante == 0:
    st.session_state.pergunta_atual += 1
    st.session_state.tempo_restante = 30
    st.session_state.respondido = False
    st.rerun()

if st.session_state.pergunta_atual < len(perguntas):
  pergunta_atual = perguntas[st.session_state.pergunta_atual]
  st.subheader(pergunta_atual["pergunta"])
  tempo = st.empty()
  tempo.subheader(f"Tempo restante: {st.session_state.tempo_restante} segundos")
  escolha = st.radio("Escolha uma opcao", pergunta_atual["opcoes"])
  if st.button("RESPONDER") and not st.session_state.respondido:
    st.session_state.respondido = True
    if escolha == pergunta_atual["resposta"]:
      st.success("Resposta correta!")
      st.session_state.pontuacao += 1
    else:
      st.error(f"Resposta errada! A resposta certa era: {pergunta_atual['resposta']}")
    time.sleep(2)
    st.session_state.pergunta_atual += 1
    st.session_state.tempo_restante = 30
    st.session_state.respondido = False
    st.rerun()
  if not st.session_state.respondido:
    atualizar_temporizador()

else:
  st.subheader("Fim do jogo!")
  st.write(f"Pontuacao final: {st.session_state.pontuacao} de {len(perguntas)}")
  if st.button("REINICIAR"):
    st.session_state.pontuacao = 0
    st.session_state.pergunta_atual = 0
    st.session_state.tempo_restante = 30
    st.session_state.respondido = False
    st.rerun()