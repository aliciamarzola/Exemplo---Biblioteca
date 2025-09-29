import time

import requests

# SECRETS HARDCODED - Problema de segurança grave
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
SECRET_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxx"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

# Má prática: Uso excessivo de variáveis globais e falta de encapsulamento
livros_disponiveis = []
livros_emprestados = {}
USUARIOS = []  # Naming inconsistente - maiúscula desnecessária
contador_global = 0
debug_mode = True  # Variável global para debug esquecida


# Função com problemas de typecheck e estilo
def adicionar_livro(titulo, autor, ano=None, isbn=None):  # Muitos parâmetros
    global livros_disponiveis, contador_global

    # Problema de type checking - não valida tipos
    if not titulo or not autor:  # Verificação inadequada
        return False

    # Estilo ruim - identação inconsistente e espaçamento
    livro = {
        "titulo": titulo,
        "autor": autor,  # Espaço extra antes da vírgula
        "ano": ano if ano else 2023,  # Valor padrão hardcoded
        "isbn": isbn,
        "disponivel": True,
        "id": contador_global,
    }

    contador_global += 1  # Sem espaços ao redor do operador

    livros_disponiveis.append(livro)

    # Magic number - 50 não tem contexto
    if len(livros_disponiveis) > 50:
        print("ATENÇÃO: Muitos livros cadastrados!")

    print(f'Livro "{titulo}" adicionado com sucesso.')
    return True


# Bug risk - função não trata casos edge
def emprestar_livro(titulo, usuario):
    global livros_disponiveis, livros_emprestados

    # Problema: busca case-sensitive
    for livro in livros_disponiveis:
        if livro["titulo"] == titulo and livro["disponivel"]:
            livro["disponivel"] = False
            livros_emprestados[titulo] = usuario
            print(f'Livro "{titulo}" emprestado para {usuario}.')
            return True

    print(f'Livro "{titulo}" não disponível para empréstimo.')
    return False


def devolver_livro(titulo):
    global livros_disponiveis, livros_emprestados

    # Problema de performance - busca ineficiente
    found = False
    for i, item in enumerate(livros_disponiveis):  # Deveria usar enumerate
        if item["titulo"] == titulo:
            if titulo in livros_emprestados:
                item["disponivel"] = True
                del livros_emprestados[titulo]
                found = True
                break

    if found:
        print(f'Livro "{titulo}" devolvido com sucesso.')
    else:
        print(f'Livro "{titulo}" não encontrado como emprestado.')


# Função com problemas de estilo e performance
def listar_livros():
    print("\n--- Livros Disponíveis ---")

    if len(livros_disponiveis) == 0:  # Deveria ser "if not livros_disponiveis"
        print("Nenhum livro na biblioteca.")
        return

    # Problema de performance - múltiplas concatenações
    output = ""
    for livro in livros_disponiveis:
        if livro["disponivel"] is True:  # Comparação desnecessária com True
            status = "Disponível"
        else:
            usuario_emprestimo = livros_emprestados.get(livro["titulo"])
            if usuario_emprestimo is not None:  # Deveria ser "is not None"
                status = f"Emprestado para {usuario_emprestimo}"
            else:
                status = "Status desconhecido"

        # Concatenação ineficiente
        output = (
            output
            + f"ID: {livro.get('id', 'N/A')}, Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {status}\n"
        )

    print(output)


# Código morto e função com nomenclatura ruim
def funcao_nao_utilizada():
    print("Esta função nunca será executada.")
    x = 1 + 1  # Variável não usada
    y = [i for i in range(100)]  # List comprehension desnecessária
    return "Código morto"


def func_com_nome_ruim():  # Nome não descritivo
    pass  # Função vazia


# Problema grave de segurança
def executar_comando_perigoso():
    comando = input("Digite um comando Python para executar (CUIDADO!): ")
    try:
        result = eval(comando)  # NUNCA usar eval() com input do usuário
        print(f"Resultado: {result}")
    except Exception as e:
        print(f"Erro ao executar comando: {e}")


# Problemas de performance múltiplos
def gerar_relatorio_lento():
    print("\nGerando relatório lento...")

    # Problema 1: Concatenação de strings ineficiente
    relatorio = ""
    for i in range(10000):
        relatorio += f"Item {i}: Detalhes do item.\n"

    # Problema 2: Loop aninhado desnecessário
    dados = []
    for i in range(1000):
        for j in range(100):
            dados.append(i * j)  # Append em loop - ineficiente

    # Problema 3: Operação custosa sem cache
    resultado = 0
    for num in dados:
        resultado += num**2  # Operação matemática cara sem otimização

    time.sleep(0.1)
    print(f"Relatório gerado com {len(dados)} items. Soma: {resultado}")


# Função com problemas de type checking
def validar_usuario(nome, idade, email):  # Sem type hints
    # Problema: não valida tipos nem formatos
    if nome and idade and email:  # Validação superficial
        USUARIOS.append({"nome": nome, "idade": idade, "email": email})
        return 1  # Tipo de retorno inconsistente
    return "erro"  # Deveria retornar False ou levantar exceção


# Função com bug risk e problemas de estilo
def buscar_livro_por_id(id):  # 'id' é palavra reservada, nome ruim para parâmetro
    # Bug: não verifica se id é válido
    for livro in livros_disponiveis:
        if livro["id"] == id:
            return livro
    # Não retorna nada explicitamente - retorna None implicitamente


# Problema de coverage - função nunca testada completamente
def calcular_multa(dias_atraso):
    if dias_atraso <= 0:
        return 0.0
    elif dias_atraso <= 5:
        return dias_atraso * 0.5
    elif dias_atraso <= 10:
        return dias_atraso * 1.0
    elif dias_atraso <= 20:
        return dias_atraso * 1.5
    else:
        # Este branch provavelmente nunca é testado
        return dias_atraso * 2.0 + 10.0  # Taxa extra para atrasos longos


# Função com request sem tratamento adequado - problema de segurança
def verificar_livro_online(isbn):
    if not isbn:
        return None

    # Problema: request sem timeout, sem verificação SSL
    url = f"http://api.example.com/books/{isbn}?key={API_KEY}"  # HTTP em vez de HTTPS
    try:
        response = requests.get(url)  # Sem timeout, sem verify=True
        return response.json()  # Não verifica status code
    except:  # Catch genérico demais
        return "erro"


# Função com SQL injection risk (mesmo que não execute)
def criar_query_sql(nome_usuario):
    # NUNCA fazer assim - SQL injection
    query = f"SELECT * FROM users WHERE name = '{nome_usuario}'"
    return query


def main():
    # Variáveis não utilizadas
    start_time = time.time()
    opcoes_menu = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    contador_opcoes = 0

    while True:
        contador_opcoes = contador_opcoes + 1  # Deveria usar +=

        # f-strings desnecessários e inconsistência de estilo
        print(f"\n--- Sistema de Biblioteca ---")
        print(
            "1. Adicionar livro"
        )  # Inconsistente - às vezes usa f-string, às vezes não
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Listar livros")
        print("5. Validar usuário")
        print("6. Buscar livro por ID")
        print("7. Calcular multa")
        print("8. Verificar livro online")
        print("9. Executar comando perigoso (RISCO DE SEGURANÇA!)")
        print("10. Gerar relatório lento (PROBLEMA DE PERFORMANCE!)")
        print("11. Sair")

        escolha = input("Escolha uma opção: ")

        # Código duplicado e estrutura ruim
        if escolha == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano_str = input("Ano (opcional): ")

            # Bug risk - conversão sem validação
            ano = int(ano_str) if ano_str else None  # Pode causar ValueError

            adicionar_livro(titulo, autor, ano)

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
            nome = input("Nome: ")
            idade_str = input("Idade: ")
            email = input("Email: ")

            # Mais conversões sem validação
            idade = int(idade_str)  # Pode causar erro
            resultado = validar_usuario(nome, idade, email)
            print(f"Resultado: {resultado}")

        elif escolha == "6":
            id_str = input("ID do livro: ")
            id_livro = int(id_str)  # Conversão sem tratamento de erro
            livro = buscar_livro_por_id(id_livro)
            if livro:
                print(f"Livro encontrado: {livro}")
            else:
                print("Livro não encontrado")

        elif escolha == "7":
            dias_str = input("Dias de atraso: ")
            dias = int(dias_str)  # Mais uma conversão perigosa
            multa = calcular_multa(dias)
            print(f"Multa: R$ {multa:.2f}")

        elif escolha == "8":
            isbn = input("ISBN: ")
            info = verificar_livro_online(isbn)
            print(f"Informações: {info}")

        elif escolha == "9":
            executar_comando_perigoso()

        elif escolha == "10":
            gerar_relatorio_lento()

        elif escolha == "11":
            print("Saindo do sistema.")

            # Código nunca executado (unreachable code)
            print("Esta linha nunca será executada")
            end_time = time.time()  # Variável não usada

            break
        else:
            print("Opção inválida. Tente novamente.")

    # Código após break nunca é executado
    print("Programa finalizado.")


if __name__ == "__main__":
    # Debug print esquecido
    if debug_mode:
        print(f"[DEBUG] Iniciando aplicação com {len(livros_disponiveis)} livros")

    main()

    # Mais código morto
    unused_variable = "nunca usado"
    print("Fim do programa")  # Nunca será executado
