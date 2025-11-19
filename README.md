# 🤖 Agente de IA Conversacional para Delivery (Protótipo V1.0)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)]()
[![LangChain](https://img.shields.io/badge/LangChain-v0.2-green?style=flat-square)]()
[![Database: SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite)]()

## 💡 Sobre o Projeto

Este projeto é um **Protótipo Funcional de Agente de IA (IA Agentic)** desenvolvido para automatizar e otimizar o atendimento de pedidos no delivery **Expresso Chicken Frango Frito**.

**O problema resolvido:** Transformar o fluxo manual e propenso a erros do WhatsApp em um sistema de atendimento inteligente que acessa o banco de dados do cardápio em tempo real. Este projeto demonstra como aplicar o conceito de Agentes de IA para resolver um problema real de negócio.

## 🧠 Arquitetura e Tecnologia (O Conceito de Agente)

O sistema utiliza uma arquitetura de Agentes ReAct (Reasoning + Acting), onde o **GPT-3.5** é o motor de raciocínio. O agente não usa um modelo treinado do zero; ele usa o LLM para "pensar" e decide qual ferramenta usar para resolver a tarefa do cliente.

### Componentes Chave:

| Componente | Função no Sistema | Tecnologia Utilizada |
| :--- | :--- | :--- |
| **Cérebro de Raciocínio** | Entende a intenção e planeja o próximo passo. | OpenAI GPT-3.5-Turbo (via LangChain) |
| **Ferramentas (Tools)** | Acessa os dados reais do negócio (SQL). | **SQLDatabaseToolkit** (Conexão SQLite) |
| **Conhecimento** | Guarda o Cardápio, Preços e Taxas. | **SQLite 3** |
| **Lógica** | Gerencia o ciclo de conversa (ReAct). | **LangChain Agent Executor** |

## 🛠️ Como Executar (Faça o Teste)

Este projeto é um MVP (Produto Mínimo Viável).

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    ```
2.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configuração:**
    * Crie um arquivo `.env` na raiz do projeto e configure sua chave: `OPENAI_API_KEY="SUA_CHAVE_AQUI"`
    * **Banco de Dados:** O código (`agente_final.py`) está configurado para um caminho absoluto. Ajuste o caminho no script para apontar corretamente para o seu arquivo `meu_banco_de_dados.db`.
4.  **Dê a Partida:**
    ```bash
    python agente_final.py
    ```
5.  **Teste o Agente (Perguntas que ele deve resolver sozinho):**
    * `Quais são todas as opções de Porções e seus preços?`
    * `Quanto custa a entrega para o bairro Centro?`
    * `Qual o horário de funcionamento hoje?`

---
*Desenvolvido por [Gustavo Damaso](www.linkedin.com/in/gudamaso-dev-ia)