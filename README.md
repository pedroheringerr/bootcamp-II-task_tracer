# TaskTracker

Aplicação de linha de comando para cadastro e visualização de tarefas do Bootcamp
II. O projeto transforma o planejamento lógico da Fase 1 em uma aplicação Python
funcional, com validação de título e prioridade e status inicial automático.

## Funcionalidades

- Cadastrar uma tarefa com título, descrição, prioridade e data limite.
- Validar o preenchimento do título.
- Aceitar as prioridades `Alta`, `Média`/`Media` e `Baixa`, normalizando a exibição.
- Definir automaticamente o status como `Pendente`.
- Visualizar todas as tarefas cadastradas.
- Informar quando ainda não existem tarefas.
- Manter o menu ativo até a opção de saída.

## Tecnologias utilizadas

- Python 3
- Git
- Interface de linha de comando (CLI)

## Estrutura de diretórios

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

O arquivo `docs/planejamento_logico.pdf` é a cópia do planejamento entregue na
Fase 1. O PDF original foi mantido fora do projeto e não foi alterado.

## Pré-requisitos

- Python 3.8 ou superior.
- Git, caso queira versionar o projeto localmente.

## Como executar

No diretório `tasktracker-projeto`, execute:

```bash
python3 src/main.py
```

Escolha uma opção do menu. Os dados ficam em memória durante a execução e são
perdidos quando a aplicação é encerrada, conforme o escopo da Fase 2.

## Exemplo de uso

```text
=== TaskTracker ===
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
Escolha uma opção: 1

--- Cadastrar nova tarefa ---
Título: Estudar Python
Descrição: Revisar estruturas de repetição
Prioridade (Alta, Média ou Baixa): Media
Data limite (DD/MM/AAAA ou texto livre): 30/10/2026
Tarefa cadastrada com sucesso.
```

## Testes

Não há suíte automatizada nesta fase. A validação manual pode ser feita executando
o programa e conferindo cadastro válido, título vazio, prioridade inválida,
listagem com e sem tarefas e saída pelo menu.

## Execução com Docker

### Construir a imagem

Na raiz do projeto, execute:

```bash
docker build -t tasktracker-app .
```

### Rodar o container diretamente

```bash
docker run --rm -it tasktracker-app
```

### Rodar com Docker Compose

O serviço está configurado com entrada padrão aberta e terminal virtual para
preservar a interação da aplicação CLI:

```bash
docker compose run --rm tasktracker
```

O `docker-compose.yml` constrói a imagem `tasktracker-app` e inicia
`python src/main.py`.
