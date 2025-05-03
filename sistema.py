import sqlite3

# Conexão com banco de dados SQLite
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

# Criação da tabela de contas
cursor.execute("""
CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL,
    saldo REAL DEFAULT 0
)
""")
conn.commit()


class Conta:
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito de R${valor:.2f}")
            self._atualizar_saldo()
            print("✅ Depósito realizado com sucesso.")
        else:
            print("❌ Valor inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido.")
        elif valor > self.saldo:
            print("❌ Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque de R${valor:.2f}")
            self._atualizar_saldo()
            print("✅ Saque realizado com sucesso.")

    def ver_saldo(self):
        print(f"💰 Saldo atual: R${self.saldo:.2f}")

    def ver_extrato(self):
        print("\n📄 Extrato:")
        if not self.historico:
            print("Nenhuma operação realizada.")
        else:
            for op in self.historico:
                print(f"• {op}")
        self.ver_saldo()

    def _atualizar_saldo(self):
        cursor.execute("UPDATE contas SET saldo = ? WHERE id = ?", (self.saldo, self.id))
        conn.commit()


def criar_conta():
    print("\n=== Cadastro de Conta ===")
    nome = input("Nome do titular: ")
    senha = input("Senha: ")
    saldo_inicial = float(input("Saldo inicial: R$"))

    cursor.execute("INSERT INTO contas (nome, senha, saldo) VALUES (?, ?, ?)", (nome, senha, saldo_inicial))
    conn.commit()
    print("✅ Conta criada com sucesso!")


def fazer_login():
    print("\n=== Login ===")
    nome = input("Nome: ")
    senha = input("Senha: ")

    cursor.execute("SELECT id, nome, saldo FROM contas WHERE nome = ? AND senha = ?", (nome, senha))
    resultado = cursor.fetchone()

    if resultado:
        print(f"🎉 Bem-vindo(a), {resultado[1]}!")
        return Conta(*resultado)
    else:
        print("❌ Nome ou senha inválidos.")
        return None


def menu():
    print("\n--- MENU ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Ver extrato")
    print("0 - Sair")


def main():
    while True:
        print("\n=== Sistema Bancário ===")
        print("1 - Criar conta")
        print("2 - Login")
        print("0 - Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            criar_conta()
        elif escolha == "2":
            conta = fazer_login()
            if conta:
                while True:
                    menu()
                    opcao = input("Escolha: ")
                    if opcao == "1":
                        valor = float(input("Valor para depósito: R$"))
                        conta.depositar(valor)
                    elif opcao == "2":
                        valor = float(input("Valor para saque: R$"))
                        conta.sacar(valor)
                    elif opcao == "3":
                        conta.ver_saldo()
                    elif opcao == "4":
                        conta.ver_extrato()
                    elif opcao == "0":
                        print("👋 Logout realizado.")
                        break
                    else:
                        print("❌ Opção inválida.")
        elif escolha == "0":
            print("Até mais!")
            break
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
