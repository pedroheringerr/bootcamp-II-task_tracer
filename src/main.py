"""Aplicação CLI do projeto TaskTracker."""


PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


def solicitar_titulo():
    """Solicita um título até que um valor não vazio seja informado."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode estar vazio.")


def solicitar_prioridade():
    """Solicita e normaliza uma prioridade válida."""
    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if prioridade in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[prioridade]
        print("Erro: prioridade inválida. Escolha Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    """Lê os dados de uma tarefa e adiciona o registro à lista."""
    print("\n--- Cadastrar nova tarefa ---")
    tarefa = {
        "título": solicitar_titulo(),
        "descrição": input("Descrição: ").strip(),
        "prioridade": solicitar_prioridade(),
        "data limite": input("Data limite (DD/MM/AAAA ou texto livre): ").strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso.")


def listar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas ou informa quando a lista está vazia."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa encontrada. Aproveite o seu dia livre!")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título: {tarefa['título']}")
        print(f"Descrição: {tarefa['descrição']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data limite']}")
        print(f"Status: {tarefa['status']}")


def exibir_menu():
    """Exibe o menu principal."""
    print("\n=== TaskTracker ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    """Executa o loop principal da aplicação."""
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Aplicação encerrada.")
            break
        else:
            print("Erro: opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
