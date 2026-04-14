import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="db_primeiro_banco",
        user="postgres",
        password="1234",
        port="5432"
    )

    print("✅ Conexão realizada com sucesso!")

    conn.close()

except Exception as erro:
    print("❌ Erro ao conectar:")
    print(erro)
