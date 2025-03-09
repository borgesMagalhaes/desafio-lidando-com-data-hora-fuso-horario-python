# Sistema Bancário Básico

Este projeto é um exemplo de um sistema bancário simples em **Python** que demonstra três recursos importantes:

1. **Decorador de Log**: Um recurso para registrar (logar) sempre que certas funções são chamadas.  
2. **Gerador de Relatórios**: Uma função que retorna as transações de uma conta, uma a uma, e permite filtrar por tipo (DEPÓSITO ou SAQUE).  
3. **Iterador Personalizado**: Um jeito de “percorrer” diversas contas do banco, mostrando informações básicas de cada uma.

## Como Funciona

1. **Classe `Conta`**: Representa uma conta bancária. Ela tem:
   - Um número (`numero`)
   - Um saldo (`saldo`)
   - Um histórico de transações (lista de operações de depósito ou saque)
   
   Nessa classe, temos métodos para **depositar** e **sacar**, que usam o **decorador de log** (explicado abaixo).

2. **Decorador de Log** (`@log_decorator`):
   - Toda vez que chamamos as funções decoradas (por exemplo, `depositar` ou `sacar`), o decorador imprime uma mensagem dizendo que a função foi chamada e em qual horário.
   - Na prática, isso serve para **monitorar** o uso do sistema.

3. **Gerador de Relatórios** (`gerador_relatorio`):
   - É uma função que “gera” ou “produz” cada transação sem precisar criar uma lista completa de uma vez.  
   - Você pode pedir para ela trazer **todas** as transações ou apenas as de um tipo específico (apenas `DEPÓSITO` ou apenas `SAQUE`).

4. **Iterador Personalizado** (`ContaIterador`):
   - Para o **Banco** (que tem várias contas), criamos um iterador.  
   - Isso permite usar o comando `for` para percorrer cada conta do banco.  
   - Cada vez que o `for` pula para a próxima conta, retornamos (número da conta, saldo).

## Como Executar

1. **Instale o Python 3.7 ou superior** no seu computador.  
2. Baixe ou clone este projeto para uma pasta.  
3. No terminal (ou prompt), vá até a pasta onde está o arquivo principal, por exemplo:  
   ```bash
   cd caminho/da/pasta
```
python banco_decoradores_geradores_iteradores.py
```