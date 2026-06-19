# 📊 Bia - Assistente Inteligente de Organização de Gastos

Olá! Seja muito bem-vindo(a) ao meu projeto desenvolvido para o segundo desafio prático (Lab) da plataforma **DIO**. 

Muitas pessoas acham planilhas de finanças muito difíceis, chatas ou cheias de termos técnicos que ninguém entende. A **Bia** foi criada para resolver exatamente isso: ela é uma assistente virtual conversacional focada em ajudar qualquer pessoa a entender e organizar suas despesas do dia a dia de forma simples e acolhedora.

---

### 🤔 Por que este projeto foi criado e para que serve? (O Motivo)

O principal motivo deste projeto é a **educação financeira acessível**. Saber para onde o dinheiro está indo é o primeiro passo para não ficar no vermelho, mas a maioria das pessoas desiste porque os aplicativos atuais são complicados. 

A Bia serve para:
* **Simplificar o controle de dinheiro**: O usuário só precisa digitar uma frase comum (ex: *"Recebi R$ 2000, gastei R$ 400 em mercado e R$ 150 em transporte"*).
* **Calcular o saldo automaticamente**: Ela soma os ganhos, subtrai os gastos e mostra o diagnóstico real de forma clara.
* **Dar dicas amigáveis de economia**: Ela analisa onde a pessoa gastou mais e sugere um ponto fácil de corte ou economia.

---

### ⚙️ Como o projeto funciona por dentro? (Sem termos técnicos)

A estrutura do projeto segue os 6 passos exigidos pelo desafio da DIO para criar um assistente virtual inteligente:

1. **Documentação (A Ideia)**: Definição clara de que a Bia é especialista apenas em analisar o orçamento (entradas e saídas).
2. **Base de Conhecimento (Os Dados)**: O programa lê uma pasta de dados (`Data/perfil_investidor.json`) para saber o nome do usuário e personalizar o atendimento.
3. **Instruções do Robô (Prompts)**: Criamos regras firmes para a inteligência artificial. Se o usuário tentar falar de investimentos arriscados, ações ou outros assuntos, ela recusa educadamente e foca apenas em organizar as despesas atuais.
4. **Tela Funcional (Aplicativo)**: Construído em Python usando uma ferramenta chamada *Streamlit*, que cria uma página de bate-papo limpa e bonita no navegador.
5. **Avaliação (Testes)**: O robô foi testado com simulações de orçamentos apertados para garantir que suas dicas fazem sentido matemático e prático.
6. **Apresentação (O Valor)**: Um protótipo funcional focado em ajudar pessoas comuns a darem o primeiro passo rumo à organização financeira.

---

### 🚀 Como testar no seu computador

1. Baixe os arquivos deste repositório para o seu computador.
2. Abra o terminal na pasta e instale as ferramentas necessárias com o comando:
   ```bash
   pip install -r src/requirements.txt
   ```
3. Abra o arquivo de código e coloque sua chave da OpenAI.
4. Inicie o chat digitando o comando abaixo no terminal:
   ```bash
   python -m streamlit run src/app.py
   ```

