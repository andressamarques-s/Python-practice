# ===============================
# CONTADOR DE PALAVRAS LONGAS
# ===============================

def contar_palavras_longas():
    texto = input("Digite um texto: ").split()
    palavras_longas = []

    for palavra in texto:
        if len(palavra) > 10:
            palavras_longas.append(palavra)

    if palavras_longas:
        print("\nPalavras com mais de 10 letras:")
        for palavra in palavras_longas:
            print(f"- {palavra}")
    else:
        print("Nenhuma palavra contém mais de 10 letras.")


# ===============================
# GERADOR DE SENHA SEGURA
# ===============================

import random

def gerar_senha():
    maiusculas = "QWERTYUIOPASDFGHJKLZXCVBNM"
    minusculas = maiusculas.lower()
    numeros = "0123456789"
    especiais = "!@#$%&*"

    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiais)
    ]

    todos = maiusculas + minusculas + numeros + especiais

    senha.extend(random.choices(todos, k=8))
    random.shuffle(senha)

    return ''.join(senha)


# ===============================
# JOGO DE ADIVINHAÇÃO
# ===============================

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))

            if not 1 <= chute <= 100:
                print("Número fora do intervalo.")
                continue

            tentativas += 1

            if chute == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
            elif chute > numero_secreto:
                print("Muito alto!")
            else:
                print("Muito baixo!")

        except ValueError:
            print("Digite apenas números inteiros.")

# ===============================
# GERENCIADOR DE TAREFAS
# ===============================

def gerenciar_tarefas():
    tarefas = []

    while True:
        print("\n===== MENU =====")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ").strip()

            if tarefa:
                tarefas.append(tarefa)
                print("Tarefa adicionada.")
            else:
                print("Tarefa vazia.")

        elif opcao == "2":
            if tarefas:
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")

        elif opcao == "3":
            if not tarefas:
                print("Nenhuma tarefa para remover.")
                continue

            try:
                indice = int(input("Digite o número da tarefa: "))

                if 1 <= indice <= len(tarefas):
                    removida = tarefas.pop(indice - 1)
                    print(f"Tarefa '{removida}' removida.")
                else:
                    print("Número inválido.")

            except ValueError:
                print("Digite um número válido.")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


# ===============================
# CAIXA ELETRÔNICO
# ===============================

def caixa_eletronico():
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        valor = int(input("Digite o valor do saque: "))

        if valor <= 0:
            print("Valor deve ser positivo.")
            return

        if valor % 2 != 0:
            print("Valor deve ser múltiplo de 2.")
            return

        print("\nNotas entregues:")

        for cedula in cedulas:
            quantidade = valor // cedula

            if quantidade > 0:
                print(f"{quantidade} nota(s) de R$ {cedula}")

            valor = valor % cedula

    except ValueError:
        print("Digite apenas números inteiros.")


# ===============================
# MENU PRINCIPAL
# ===============================

while True:
    print("\n======= PROJETOS PYTHON =======")
    print("1. Contador de palavras")
    print("2. Gerador de senha")
    print("3. Jogo de adivinhação")
    print("4. Calculadora")
    print("5. Lista de tarefas")
    print("6. Caixa eletrônico")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        contar_palavras_longas()

    elif escolha == "2":
        print("Senha gerada:", gerar_senha())

    elif escolha == "3":
        jogar()

    elif escolha == "4":
        calculadora()

    elif escolha == "5":
        gerenciar_tarefas()

    elif escolha == "6":
        caixa_eletronico()

    elif escolha == "7":
        print("Encerrando programa.")
        break

    else:
        print("Opção inválida.")
