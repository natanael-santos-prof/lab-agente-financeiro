import streamlit as st
from openai import OpenAI

# Configuração visual da tela de chat
st.set_page_config(page_title="Bia - Análise de Gastos", page_icon="📉")
st.title("📊 Bia - Sua Especialista em Análise de Gastos")
st.markdown("Compartilhe seus gastos diários ou mensais comigo para organizarmos suas finanças!")

# ATENÇÃO: Cole sua chave nova da OpenAI aqui para testar no computador
API_KEY = "SUA_CHAVE_AQUI"
client = OpenAI(api_key=API_KEY)

# Histórico da conversa na tela
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa onde o usuário digita
if prompt := st.chat_input("Ex: Recebi R$ 2000 e gastei R$ 500 em mercado e R$ 200 em lazer..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Instruções focadas APENAS em análise de gastos e sem termos difíceis
        contexto_sistema = """
        Você é a Bia, uma assistente virtual muito paciente e focada EXCLUSIVAMENTE em Análise de Gastos para iniciantes.
        Seu único objetivo é ajudar o usuário a organizar o orçamento dele (receitas e despesas).
        
        Regras de comportamento:
        1. Responda em português simples e acolhedor, sem usar palavras difíceis de economia.
        2. Pegue os valores enviados pelo usuário, classifique-os em categorias (como Alimentação, Transporte, Lazer, Contas Fixas) e mostre a conta de quanto sobrou ou faltou.
        3. Dê uma dica simples de como diminuir os gastos relatados.
        4. Se o usuário perguntar sobre investimentos, ações, robôs de PIX ou qualquer outro assunto que não seja organizar gastos, responda estritamente: 'Peço desculpas, mas minha especialidade é ajudar você a analisar e organizar seus gastos mensais. Vamos focar em arrumar o seu orçamento primeiro?'.
        """

        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": contexto_sistema},
                {"role": "user", "content": prompt}
            ]
        )
        
        response_text = resposta.choices.message.content
        
        with st.chat_message("assistant"):
            st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
    except Exception as e:
        st.error(f"Erro ao processar: {e}")
