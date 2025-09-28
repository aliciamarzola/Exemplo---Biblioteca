import time

import numpy as np

# Má prática: Uso excessivo de variáveis globais e falta de encapsulamento
livros_disponiveis = []
livros_emprestados = {}


def adicionar_livro(titulo, autor):
    global livros_disponiveis
    livros_disponiveis.append({"titulo": titulo, "autor": autor, "disponivel": True})
    print(f'Livro "{titulo}" adicionado com sucesso.')


def emprestar_livro(titulo, usuario):
    global livros_disponiveis, livros_emprestados
    for livro in livros_disponiveis:
        if livro["titulo"] == titulo and livro["disponivel"]:
            livro["disponivel"] = False
            livros_emprestados[titulo] = usuario
            print(f'Livro "{titulo}" emprestado para {usuario}.')
            return
    print(f'Livro "{titulo}" não disponível para empréstimo.')


def devolver_livro(titulo):
    global livros_disponiveis, livros_emprestados
    if titulo in livros_emprestados:
        for livro in livros_disponiveis:
            if livro["titulo"] == titulo:
                livro["disponivel"] = True
                del livros_emprestados[titulo]
                print(f'Livro "{titulo}" devolvido com sucesso.')
                return
    print(f'Livro "{titulo}" não encontrado como emprestado.')


def listar_livros():
    print("\n--- Livros Disponíveis ---")
    if not livros_disponiveis:
        print("Nenhum livro na biblioteca.")
    for livro in livros_disponiveis:
        status = (
            "Disponível"
            if livro["disponivel"]
            else f"Emprestado para {livros_emprestados.get(livro['titulo'], 'Desconhecido')}"
        )
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {status}")


# Código morto: Esta função nunca é chamada no fluxo principal
def funcao_nao_utilizada():
    print("Esta função nunca será executada.")
    return "Código morto"


# Risco de segurança: Uso de eval() com entrada do usuário
def executar_comando_perigoso():
    comando = input("Digite um comando Python para executar (CUIDADO!): ")
    try:
        eval(comando)
        print("Comando executado.")
    except Exception as e:
        print(f"Erro ao executar comando: {e}")


# Problema de performance: Concatenação de strings ineficiente em loop
def gerar_relatorio_lento():
    print("\nGerando relatório lento...")
    relatorio = ""
    for i in range(10000):
        # Esta concatenação cria uma nova string a cada iteração, sendo ineficiente
        relatorio += f"Item {i}: Detalhes do item.\n"
    # Simula um processamento longo
    time.sleep(0.1)
    print("Relatório lento gerado (mas não exibido para evitar sobrecarga).")


def main():
    while True:
        print("\n--- Sistema de Biblioteca ---")  # f string desnecessária
        print("1. Adicionar livro")
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Listar livros")
        print("5. Executar comando perigoso (RISCO DE SEGURANÇA!)")
        print("6. Gerar relatório lento (PROBLEMA DE PERFORMANCE!)")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            adicionar_livro(titulo, autor)
        elif escolha == "2":
            titulo = input("Título do livro a emprestar: ")
            usuario = input("Nome do usuário: ")
            emprestar_livro(titulo, usuario)
        elif escolha == "3":
            titulo = input("Título do livro a devolver: ")
            devolver_livro(titulo)
        elif escolha == "4":
            listar_livros()
        elif escolha == "5":
            executar_comando_perigoso()
        elif escolha == "6":
            gerar_relatorio_lento()
        elif escolha == "7":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
