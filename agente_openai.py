import os
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

print("================================================")
print("   ATENDENTE AGENTE V1.0 - EXPRESSO CHICKEN")
print("   (Conectado ao Cérebro GPT e ao Banco SQL)")
print("================================================")

# 1. Configuração
api_key = os.getenv("OPENAI_API_KEY")
if not api_key: exit("Erro: Chave OPENAI_API_KEY não encontrada.")

# 2. Conexão com o Banco
db = SQLDatabase.from_uri("sqlite:///meu_banco_de_dados.db")

# 3. O Cérebro
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 4. O Agente (Agora com instruções de personalidade!)
# O prefixo diz ao agente QUEM ele é.
prefixo = """
Você é o 'Frangolino', o atendente virtual do Expresso Chicken Frango Frito.
Sua missão é ajudar os clientes consultando o banco de dados.
Seja sempre educado, use emojis (🐔, 🍟) e responda de forma clara.
NUNCA invente informações. Use apenas o que encontrar no banco de dados.
Se o cliente perguntar taxas de entrega, procure na tabela 'entregas'. Você é um garçom,
 não um analista de banco de dados. Quando o cliente confirmar o pedido, apenas anote e agradeça,
   não mostre a estrutura técnica das tabelas.
Se perguntar horário, procure na tabela 'configuracoes'.
"""

agente = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="openai-tools",
    verbose=True, # Deixe True para ver ele pensando!
    agent_executor_kwargs={"handle_parsing_errors": True},
    prefix=prefixo
)

# 5. Loop de Conversa
print("\nFrangolino: Olá! Sou o Frangolino 🐔. Em Que Posso Ajudar?")

while True:
    pergunta = input("\n> Você: ")
    
    if pergunta.lower() in ['sair', 'tchau', 'fim']:
        print("Frangolino: Tchau! Volte sempre! 🐔")
        break
        
    try:
        # O agente processa a pergunta
        resposta = agente.invoke(pergunta)
        print(f"\nFrangolino: {resposta['output']}")
    except Exception as e:
        print(f"\nFrangolino: Ops, me confundi um pouco. Pode repetir? (Erro: {e})")