from db import conectar


def buscar_por_nome(nome):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT id, pontuacao FROM ranking WHERE nome=%s", (nome,))
    resultado = cur.fetchone()

    cur.close()
    conn.close()

    return resultado


def inserir(nome, data, hora, pontuacao):
    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO ranking (nome,data,hora,pontuacao)
        VALUES (%s,%s,%s,%s)
        RETURNING id
        """,
        (nome, data, hora, pontuacao)
    )

    id_novo = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return id_novo


def atualizar(id_jogador, data, hora, pontuacao):
    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE ranking
        SET pontuacao=%s, data=%s, hora=%s
        WHERE id=%s
        """,
        (pontuacao, data, hora, id_jogador)
    )

    conn.commit()
    cur.close()
    conn.close()


def listar_top10():
    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, nome, pontuacao
        FROM ranking
        ORDER BY pontuacao DESC
        LIMIT 10
        """
    )

    dados = cur.fetchall()

    cur.close()
    conn.close()

    return dados
