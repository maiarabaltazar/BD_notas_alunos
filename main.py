#Importa todas as funções definidas em database.py.
from database import create_database, inserir_aluno, inserir_nota, excluir_aluno, excluir_nota, atualizar_aluno, atualizar_nota, consultar_alunos, consultar_notas, consultar_notas_por_aluno

# Função para exibir o menu e interagir com o usuário
def menu():
    while True:
        print(" ")
        print("1. Inserir aluno")
        print("2. Inserir nota")
        print("3. Excluir aluno")
        print("4. Excluir nota")
        print("5. Atualizar aluno")
        print("6. Atualizar nota")
        print("7. Consultar alunos")
        print("8. Consultar notas")
        print("9. Consultar notas por aluno")
        print("0. Sair")
        print(" ")

        escolha = input("Escolha uma opção: ")

        try:
            if escolha == '1':
                nome = input("Nome do aluno: ")
                matricula = int(input("Matrícula do aluno: "))
                inserir_aluno(nome, matricula)
                print("Aluno inserido com sucesso!")
            elif escolha == '2':
                aluno_id = int(input("ID do aluno: "))
                disciplina = input("Disciplina: ")
                nota = float(input("Nota: "))
                inserir_nota(aluno_id, disciplina, nota)
                print("Nota inserida com sucesso!")
            elif escolha == '3':
                aluno_id = int(input("ID do aluno: "))
                excluir_aluno(aluno_id)
                print("Aluno excluído com sucesso!")
            elif escolha == '4':
                nota_id = int(input("ID da nota: "))
                excluir_nota(nota_id)
                print("Nota excluída com sucesso!")
            elif escolha == '5':
                aluno_id = int(input("ID do aluno: "))
                nome = input("Novo nome (deixe em branco para não alterar): ")
                matricula = input("Nova matrícula (deixe em branco para não alterar): ")
                atualizar_aluno(aluno_id, nome if nome else None, int(matricula) if matricula else None)
                print("Aluno atualizado com sucesso!")
            elif escolha == '6':
                nota_id = int(input("ID da nota: "))
                disciplina = input("Nova disciplina (deixe em branco para não alterar): ")
                nota = input("Nova nota (deixe em branco para não alterar): ")
                atualizar_nota(nota_id, disciplina if disciplina else None, float(nota) if nota else None)
                print("Nota atualizada com sucesso!")
            elif escolha == '7':
                alunos = consultar_alunos()
                for aluno in alunos:
                    print(aluno)
            elif escolha == '8':
                notas = consultar_notas()
                for nota in notas:
                    print(nota)
            elif escolha == '9':
                aluno_id = int(input("ID do aluno: "))
                notas = consultar_notas_por_aluno(aluno_id)
                for nota in notas:
                    print(nota)
            elif escolha == '0':
                print("Programa encerrado!")
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

#Verifica se o script está sendo executado diretamente e, se estiver, cria o banco de dados e chama a função menu para iniciar a interação com o usuário.
if __name__ == "__main__":
    create_database()  # Cria o banco de dados e as tabelas se ainda não existirem
    menu()  # Inicia o menu para interação com o usuário
