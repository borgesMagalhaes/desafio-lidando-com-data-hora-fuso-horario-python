import functools
from datetime import datetime


# 1) DECORADOR DE LOG
def log_decorator(func):
    """
    Decorador que registra a chamada de função com data/hora.
    Pode-se adaptar para gravar em arquivo, banco de dados etc.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG - {agora}] Chamando função: {func.__name__}")
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper


# CLASSE CONTA
class Conta:
    """
    Representa uma conta bancária simples.
    """
    def __init__(self, numero, saldo_inicial=0.0):
        self.numero = numero
        self.saldo = saldo_inicial
       
        self.historico_transacoes = []
    
    @log_decorator 
    def depositar(self, valor):
        if valor <= 0:
            print("ERRO: valor de depósito inválido.")
            return
        
        self.saldo += valor
        self._registrar_transacao("DEPÓSITO", valor)
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
    
    @log_decorator  
    def sacar(self, valor):
        if valor <= 0:
            print("ERRO: valor de saque inválido.")
            return
        if valor > self.saldo:
            print("ERRO: saldo insuficiente.")
            return
        
        self.saldo -= valor
        self._registrar_transacao("SAQUE", valor)
        print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
    
    def _registrar_transacao(self, tipo, valor):
        agora = datetime.now()
        transacao = {
            "data": agora.strftime("%Y-%m-%d"),
            "hora": agora.strftime("%H:%M:%S"),
            "tipo": tipo,
            "valor": valor
        }
        self.historico_transacoes.append(transacao)


# 2) GERADOR DE RELATÓRIOS
def gerador_relatorio(conta, tipo_filtro=None):
    """
    Gera transações de uma conta, uma a uma, 
    opcionalmente filtrando por tipo ('DEPÓSITO' ou 'SAQUE').
    """
    for t in conta.historico_transacoes:
        if tipo_filtro is None or t["tipo"] == tipo_filtro:
            yield t


# 3) ITERADOR PERSONALIZADO PARA VÁRIAS CONTAS
class ContaIterador:
    """
    Iterador que percorre uma lista de contas e retorna 
    informações básicas (número e saldo).
    """
    def __init__(self, contas):
        self._contas = contas
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self._contas):
            raise StopIteration
        conta_atual = self._contas[self._index]
        self._index += 1
        return (conta_atual.numero, conta_atual.saldo)

class Banco:
    """
    Classe para gerenciar várias contas.
    """
    def __init__(self):
        self.contas = []
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
    def __iter__(self):
        """
        Torna a instância do banco “iterável”, retornando nosso 
        iterador personalizado que percorre as contas.
        """
        return ContaIterador(self.contas)

if __name__ == "__main__":
    # Criando um banco e algumas contas
    banco = Banco()
    
    conta1 = Conta("001", saldo_inicial=500.0)
    conta2 = Conta("002", saldo_inicial=1000.0)
    
    banco.adicionar_conta(conta1)
    banco.adicionar_conta(conta2)
    
    # Realizando operações (decoradas com log)
    conta1.depositar(200.0)
    conta1.sacar(100.0)
    
    conta2.depositar(500.0)
    conta2.sacar(250.0)
    
    # 2) Usando o gerador para relatórios
    print("\n=== RELATÓRIO DE SAQUES DA CONTA 1 ===")
    for transacao in gerador_relatorio(conta1, tipo_filtro="SAQUE"):
        print(transacao)
    
    print("\n=== RELATÓRIO DE TODOS OS MOVIMENTOS DA CONTA 2 ===")
    for transacao in gerador_relatorio(conta2):
        print(transacao)
    
    # 3) Iterador personalizado sobre o banco
    print("\n=== ITERANDO SOBRE TODAS AS CONTAS DO BANCO ===")
    for info_conta in banco:
        print(f"Número da conta: {info_conta[0]} | Saldo: R${info_conta[1]:.2f}")
