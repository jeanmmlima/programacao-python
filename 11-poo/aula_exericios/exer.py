from abc import ABC, abstractmethod
 
class Funcionario(ABC):
    
    @abstractmethod
    def calcular_salario():
        pass
    
class FuncionarioHorista(Funcionario):
    
    def __init__(self,num_horas_trabalhadas,valor_por_hora):
        self.num_horas_trabalhadas = num_horas_trabalhadas
        self.valor_por_hora = valor_por_hora
    def calcular_salario(self):
        return self.num_horas_trabalhadas * self.valor_por_hora
    
class FuncionarioCLT(Funcionario):

    def __init__(self,salario_fixo):
        self.salario_fixo = salario_fixo
    def calcular_salario(self):
        return self.salario_fixo
    
class FuncionarioComissionado(Funcionario):
    
    def __init__(self,salario_base,comissao):
        self.salario_base = salario_base
        self.comissao = comissao
    def calcular_salario(self):
        return self.salario_base + self.comissao
    

fh = FuncionarioHorista(40,200)
print(f'O salario do horista é de: ${fh.calcular_salario()}')

fCLT = FuncionarioCLT(3000)
print(f'O salario do CLT é de: ${fCLT.calcular_salario()}')

fComissionado = FuncionarioComissionado(2000,1000)
print(f'O salario do comissionado é de: ${fComissionado.calcular_salario()}')