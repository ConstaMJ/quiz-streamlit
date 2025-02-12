import streamlit as st
import time

st.set_page_config(page_title="Quiz Interativo", page_icon="😎", layout="centered")
st.markdown("""
  <style>
  .title {
    text-align: center;
  font-size: 32px;
    font-weight: bold;
  }
  .timer {
  font-weight: bold;
  font-size: 24px;
  color: red;
  }
  .question {
  font-size: 20px;
  font-weight: bold;
  }
  </style>
""", unsafe_allow_html=True)

st.markdown("<p class='title'>Jogo de perguntas e respostas</p>", unsafe_allow_html=True)

perguntas = [
  {"pergunta": "Qual é a capital de Mocambique?", "opcoes": ["Manica", "Beira", "Maputo", "Lilongwe"], "resposta": "Maputo"},
  {"pergunta": "Consta MJ esta frequentando que curso no IIMa?", "opcoes": ["Electricidade de Manutencao Industrial", "Técnico de Construção Civil", "Engenharia Informatica", "Mecanica de Manutencao Industrial"], "resposta": "Técnico de Construção Civil"},
{"pergunta": "Em que ano o Consta MJ começou a estudar no IIMa?", "opcoes": ["2022", "2023", "2024", "2025"], "resposta": "2024"}
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
  st.progress((st.session_state.pergunta_atual + 1)/ len(perguntas))
  st.markdown(f"<p class='question'>{pergunta_atual['pergunta']}</p>", unsafe_allow_html=True)
  tempo = st.empty()
  tempo.markdown(f"<p class='timer'>Tempo restante: {st.session_state.tempo_restante} segundos</p>", unsafe_allow_html=True)
  escolha = st.radio("Escolha uma opcao", pergunta_atual["opcoes"], index=None)
  if st.button("RESPONDER") and escolha is not None and not st.session_state.respondido:
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
  if st.session_state.respondido:
    if st.button("PROXIMA PERGUNTA"):
      st.session_state.pergunta_atual += 1
      st.session_state.tempo_restante = 30
      st.session_state.respondido = False
      st.rerun()

else:
  st.markdown("## Fim do jogo!")
  st.write(f"Pontuacao final: **{st.session_state.pontuacao}** de **{len(perguntas)}**")
  if st.button("REINICIAR"):
    st.session_state.pontuacao = 0
    st.session_state.pergunta_atual = 0
    st.session_state.tempo_restante = 30
    st.session_state.respondido = False
    st.rerun()
