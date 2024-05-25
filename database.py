#Importa o módulo sqlite3, que fornece uma interface para bancos de dados SQLite.
import sqlite3

# Função para criar o banco de dados e as tabelas
def create_database():
    # Conecta ao banco de dados 'alunos_notas.db' (ou cria se não existir)
    connection = sqlite3.connect('alunos_notas.db')
    #Cria um cursor, que permite executar comandos SQL no banco de dados.
    cursor = connection.cursor()

    # Cria a tabela 'aluno' se não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        matricula TEXT NOT NULL
    )
    ''')

    # Cria a tabela 'nota' se não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS nota (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        disciplina TEXT NOT NULL,
        nota REAL NOT NULL,
        FOREIGN KEY (aluno_id) REFERENCES aluno(id) 
    )
    ''')

    # Confirma as mudanças e fecha a conexão
    connection.commit()
    connection.close()

# Função para verificar a existência de um aluno pelo id
def aluno_existe(aluno_id):
    try:
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        cursor.execute('SELECT 1 FROM aluno WHERE id = ?', (aluno_id,))
        result = cursor.fetchone() # Recupera a primeira linha do resultado da consulta. Se a consulta não retornar nenhum resultado, fetchone() retornará None.
        return result is not None
    except sqlite3.Error as e: # usa o módolo sqlite3 com o método Error que ele fornece e chama esse erro de "e"
        print(f"Erro ao verificar existência do aluno: {e}") # passa qual foi o erro
        return False  # Retorna False indicando que a verificação falhou ou o aluno não existe
    finally: # Fecha a conexão com o banco de dados, seja qual for o resultado do try ou do except
        connection.close()

# Função para inserir um novo aluno na tabela 'aluno'
def inserir_aluno(nome, matricula):
    try:
        if not all(char.isalpha() or char.isspace() for char in nome):
            raise ValueError("Nome com utilização de caracteres incompatíveis.")
        # Verifica se a matrícula é um número inteiro
        if not isinstance(matricula, int): # função para verificcar tipos de dados. o raise levanta uma exceção ValueError com uma mensagem explicando o erro.
            raise ValueError("Matrícula deve ser um número inteiro.")
        
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO aluno (nome, matricula) VALUES (?, ?)', (nome, matricula))
        connection.commit()
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except sqlite3.Error as e:
        print(f"Erro ao inserir aluno: {e}")
    finally:
        connection.close()

# Função para inserir uma nova nota na tabela 'nota'
def inserir_nota(aluno_id, disciplina, nota):
    try:
        # Verifica se o aluno existe
        if not aluno_existe(aluno_id):
            raise ValueError("ID do aluno não existe.")
        # Verifica se o ID do aluno é um número inteiro
        if not isinstance(aluno_id, int):
            raise ValueError("ID do aluno deve ser um número inteiro.")
        # Verifica se a nota é um número
        if not isinstance(nota, (int, float)):
            raise ValueError("Nota deve ser um número.")
        
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO nota (aluno_id, disciplina, nota) VALUES (?, ?, ?)', (aluno_id, disciplina, nota))
        connection.commit()
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except sqlite3.Error as e:
        print(f"Erro ao inserir nota: {e}")
    finally:
        connection.close()

# Função para excluir um aluno da tabela 'aluno'
def excluir_aluno(aluno_id):
    try:
        # Verifica se o aluno existe
        if not aluno_existe(aluno_id):
            raise ValueError("ID do aluno não existe.")
        # Verifica se o ID do aluno é um número inteiro
        if not isinstance(aluno_id, int):
            raise ValueError("ID do aluno deve ser um número inteiro.")
        
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM aluno WHERE id = ?', (aluno_id,))
        connection.commit()
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except sqlite3.Error as e:
        print(f"Erro ao excluir aluno: {e}")
    finally:
        connection.close()

# Função para excluir uma nota da tabela 'nota'
def excluir_nota(nota_id):
    try:
        # Verifica se o ID da nota é um número inteiro
        if not isinstance(nota_id, int):
            raise ValueError("ID da nota deve ser um número inteiro.")
        
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM nota WHERE id = ?', (nota_id,))
        connection.commit()
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except sqlite3.Error as e:
        print(f"Erro ao excluir nota: {e}")
    finally:
        connection.close()

# Função para atualizar os dados de um aluno na tabela 'aluno'
def atualizar_aluno(aluno_id, nome=None, matricula=None):
    try:
        # Verifica se o aluno existe
        if not aluno_existe(aluno_id):
            raise ValueError("ID do aluno não existe.")
        # Verifica se o nome é uma string, se fornecido
        if nome is not None and not isinstance(nome, str):
            raise ValueError("Nome do aluno deve ser uma string.")
        # Verifica se a matrícula é um número inteiro, se fornecida
        if matricula is not None and not isinstance(matricula, int):
            raise ValueError("Matrícula deve ser um número inteiro.")
        
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        if nome:
            cursor.execute('UPDATE aluno SET nome = ? WHERE id = ?', (nome, aluno_id))
        if matricula:
            cursor.execute('UPDATE aluno SET matricula = ? WHERE id = ?', (matricula, aluno_id))
        connection.commit()
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar aluno: {e}")
    finally:
        connection.close()

# Função para atualizar os dados de uma nota na tabela 'nota'
def atualizar_nota(nota_id, disciplina=None, nota=None):
    try:
        # Verifica se o ID da nota é um número inteiro
        if not isinstance(nota_id, int):
            raise ValueError("ID da nota deve ser um número inteiro.")
        # Verifica se a nota é um número, se fornecida
        if nota is not None and not isinstance(nota, (int, float)):
            raise ValueError("Nota deve ser um número.")
        
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        if disciplina:
            cursor.execute('UPDATE nota SET disciplina = ? WHERE id = ?', (disciplina, nota_id))
        if nota is not None:
            cursor.execute('UPDATE nota SET nota = ? WHERE id = ?', (nota, nota_id))
        connection.commit()
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar nota: {e}")
    finally:
        connection.close()

# Função para consultar todos os alunos na tabela 'aluno'
def consultar_alunos():
    try:
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM aluno')
        alunos = cursor.fetchall()
        return alunos
    except sqlite3.Error as e:
        print(f"Erro ao consultar alunos: {e}")
        return []
    finally:
        connection.close()

# Função para consultar todas as notas na tabela 'nota'
def consultar_notas():
    try:
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        cursor.execute('SELECT aluno.nome, nota.disciplina, nota.nota FROM nota JOIN aluno ON nota.aluno_id = aluno.id')
        notas = cursor.fetchall()
        return notas
    except sqlite3.Error as e:
        print(f"Erro ao consultar notas: {e}")
        return []
    finally:
        connection.close()

# Função para consultar todas as notas de um aluno específico na tabela 'nota'
def consultar_notas_por_aluno(aluno_id):
    try:
        # Verifica se o aluno existe
        if not aluno_existe(aluno_id):
            raise ValueError("ID do aluno não existe.")
        # Verifica se o ID do aluno é um número inteiro
        if not isinstance(aluno_id, int):
            raise ValueError("ID do aluno deve ser um número inteiro.")
        
        connection = sqlite3.connect('alunos_notas.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM nota WHERE aluno_id = ?', (aluno_id,))
        notas = cursor.fetchall()
        return notas
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
        return []
    except sqlite3.Error as e:
        print(f"Erro ao consultar notas do aluno: {e}")
        return []
    finally:
        connection.close()