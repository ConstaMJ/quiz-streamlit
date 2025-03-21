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
            font-size: 24px;
            font-weight: bold;
            color: red;
        }
        .question {
            font-size: 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='title'>Jogo de Perguntas e Respostas</p>", unsafe_allow_html=True)

perguntas = [
    {"pergunta": "Qual é a capital de Moçambique?", "opcoes": ["Manica", "Beira", "Maputo", "Lilongwe"], "resposta": "Maputo"},
    {"pergunta": "Consta MJ está frequentando que curso no IIMa?", "opcoes": ["Eletricidade de Manutenção Industrial", "Técnico de Construção Civil", "Engenharia Informática", "Mecânica de Manutenção Industrial"], "resposta": "Técnico de Construção Civil"},
    {"pergunta": "Em que ano o Consta MJ começou a estudar no IIMa?", "opcoes": ["2022", "2023", "2024", "2025"], "resposta": "2024"},
    {"pergunta": "Quantos cursos existem no Instituto Industrial de Matundo?", "opcoes": ["1 curso", "2 cursos", "3 cursos", "4 cursos"], "resposta": "3 cursos"},
    {"pergunta": "Quem programou esse jogo?", "opcoes": ["Constantino MJ", "Claudio MM", "Elias LE", "Tiago CV"], "resposta": "Constantino MJ"}
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
    
    st.progress((st.session_state.pergunta_atual + 1) / len(perguntas))
    st.markdown(f"<p class='question'>{pergunta_atual['pergunta']}</p>", unsafe_allow_html=True)
    
    tempo = st.empty()
    tempo.markdown(f"<p class='timer'>Tempo restante: {st.session_state.tempo_restante} segundos</p>", unsafe_allow_html=True)
    
    escolha = st.radio("Escolha uma opção", pergunta_atual["opcoes"], index=None)
    
    if st.button("RESPONDER") and escolha is not None and not st.session_state.respondido:
        st.session_state.respondido = True
        if escolha == pergunta_atual["resposta"]:
            st.success("\U0001F389 Resposta correta!")
            st.session_state.pontuacao += 1
        else:
            st.error(f"\U0001F622 Resposta errada! A resposta certa era: {pergunta_atual['resposta']}")
        
    if st.session_state.respondido:
        if st.button("PRÓXIMA PERGUNTA"):
            st.session_state.pergunta_atual += 1
            st.session_state.tempo_restante = 30
            st.session_state.respondido = False
            st.rerun()
else:
    st.markdown("## 🎉 Fim do jogo!")
    st.write(f"Pontuação final: **{st.session_state.pontuacao}** de **{len(perguntas)}**")
    if st.button("🔄 REINICIAR JOGO"):
        st.session_state.pontuacao = 0
        st.session_state.pergunta_atual = 0
        st.session_state.tempo_restante = 30
        st.session_state.respondido = False
        st.rerun()
