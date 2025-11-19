# agente_v1.py - Fundação do Agente Expresso Chicken (Versão Limpa)

import os
import sys 
from langchain_google_genai import ChatGoogleGenerativeAI

# Tenta carregar variáveis de ambiente de um arquivo .env, se python-dotenv estiver instalado
try:
    from dotenv import load_dotenv
    env_loaded = load_dotenv()
    if env_loaded:
        print("Arquivo .env carregado (variáveis de ambiente adicionadas ao processo).")
    else:
        # load_dotenv pode retornar False se .env não existir; isso não é erro
        print("Nenhum arquivo .env encontrado ou nada foi carregado por dotenv.")
except Exception:
    # Se python-dotenv não estiver instalado, não falhamos — apenas informamos.
    print("python-dotenv não encontrado. Para suporte a .env, instale: pip install python-dotenv")

print("--- Iniciando Agente V1.0 ---")

# --- 1. Carregando a Chave de API Secreta ---
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("\n!!! ERRO CRÍTICO !!!")
    print("A variável de ambiente GOOGLE_API_KEY não foi encontrada.")
    print("Configure-a nas variáveis de ambiente do Windows e REINICIE o VS Code/Terminal.")
    sys.exit(1) 
else:
    print(f"Chave de API do Google encontrada com sucesso! (Início: {google_api_key[:5]}...)")


# --- 2. Inicializando o "Cérebro" (O LLM Gemini) ---
try:
    # Permite sobrescrever o nome do modelo via variável de ambiente MODEL_NAME
    model_name = os.getenv("MODEL_NAME", "gemini-1.0-pro")
    print(f"Tentando conectar ao modelo: {model_name}")

    llm = ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=google_api_key,
        temperature=0.1  # Para respostas mais diretas
    )

    print("Conexão com o modelo estabelecida com sucesso!")

    # --- Teste Rápido de Conversa ---
    print("\n--- Testando o Cérebro ---")
    resposta_teste = llm.invoke("Olá! Quem é você?")
    # Nem todas as respostas terão o mesmo shape; cuidadoso ao acessar atributos
    try:
        content = resposta_teste.content
    except Exception:
        content = str(resposta_teste)
    print("Resposta do modelo:", content)

except Exception as e:
    err_text = str(e)
    print("\n!!! ERRO AO CONECTAR COM O MODELO !!!")
    print(f"Detalhes do erro: {err_text}")

    # Diagnóstico rápido para erros comuns
    if "not found" in err_text.lower() or "is not found" in err_text.lower():
        print("Possível causa: o nome do modelo (model=) não é suportado pela versão da API ou pela sua chave.")
        print("Sugestão: verifique a documentação do provedor ou defina a variável de ambiente MODEL_NAME para um modelo disponível.")
        print("Exemplo (PowerShell): $env:MODEL_NAME = 'nome-do-modelo' ; python .\\agente_v1.py")
    else:
        print("Verifique sua chave de API (se é válida), sua conexão com a internet, e as permissões da chave.")

    sys.exit(1)


print("\n--- Fundação do Agente V1.0 Pronta! ---")