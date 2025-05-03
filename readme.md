### 🏦 Simulador de Caixa Eletrônico (Python + SQLite)
Um projeto simples de terminal que simula um caixa eletrônico, permitindo criar contas, fazer login, sacar, depositar e ver extrato, com dados salvos em um banco SQLite. Suporta múltiplos usuários com autenticação individual.


## 🚀 Funcionalidades
- ✅ Cadastro de contas com nome, senha e saldo inicial

- 🔐 Login com autenticação (nome e senha)


## 💰 Operações bancárias:

- Depósito

- Saque

- Consulta de saldo

## Visualização de extrato

- 🧠 Histórico de operações durante a sessão (em memória)

- 🗂️ Persistência dos dados com SQLite

- 📂 Estrutura do Projeto

```graphql

SimuladorCaixa/
├── banco.db           # Arquivo SQLite gerado automaticamente
├── sistema.py         # Código principal da aplicação
└── README.md          # Documentação
```

## 🛠️ Requisitos
Python 3.7+

- Biblioteca sqlite3 (já incluída no Python)

## ▶️ Como Executar
- Clone ou baixe este repositório

- Navegue até a pasta do projeto

Execute o arquivo:

```bash

python sistema.py
```


📖 Aprendizados
Este projeto visa praticar os conceitos de:

- Lógica de programação

- Orientação a objetos

- Manipulação de banco de dados com SQLite

- Estrutura de menus e fluxo de autenticação