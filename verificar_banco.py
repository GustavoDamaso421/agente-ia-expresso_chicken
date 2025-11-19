import sqlite3

# O Caminho Absoluto (Exatamente o mesmo que você pôs no agente)
caminho_banco = r"C:\Users\expre\Desktop\Projeto_Westrock\meu_banco_de_dados.db"

print(f"--- Lendo o banco de dados em: {caminho_banco} ---")

try:
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()
    
    # Vamos contar quantos itens tem
    cursor.execute("SELECT COUNT(*) FROM cardapio")
    total = cursor.fetchone()[0]
    print(f"\nTotal de itens encontrados na tabela 'cardapio': {total}")
    
    if total > 0:
        print("\n--- Listando Todos os Itens ---")
        cursor.execute("SELECT categoria, nome_item, variacao, preco FROM cardapio")
        itens = cursor.fetchall()
        for item in items:
            print(f"[{item[0]}] {item[1]} ({item[2]}) - R$ {item[3]}")
    else:
        print("\nPERIGO: A tabela existe mas está VAZIA!")

    conn.close()

except Exception as e:
    print(f"\nErro ao ler o banco: {e}")