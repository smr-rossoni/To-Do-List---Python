# To-Do List in Python

def mostrar_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

def ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa adicionada ainda!")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")

def remover_tarefa(tarefas):
    ver_tarefas(tarefas)
    if tarefas:
        try:
            numero = int(input("Digite o número da tarefa para remover: "))
            if 1 <= numero <= len(tarefas):
                removida = tarefas.pop(numero - 1)
                print(f"Tarefa '{removida}' removida!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")

def main():
    tarefas = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            ver_tarefas(tarefas)
        elif escolha == "2":
            adicionar_tarefa(tarefas)
        elif escolha == "3":
            remover_tarefa(tarefas)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

