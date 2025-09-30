from clientes import Cliente
from contas import Conta

joao=Cliente("João da Silva", "777-1234")
maria=Cliente("Maria da Silva", "555-4321")

c1 = Conta(joao, '1111', 1000)
c1.resumo()
c1.saque(500)
c1.resumo()
c1.saque(50)
c1.resumo()
c1.deposito(200)
c1.resumo()