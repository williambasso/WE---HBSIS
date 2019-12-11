from model.pessoa import Pessoa
from model.linguagem_programacao import LinguagemProgramacao
from model.equipe_trabalho import EquipeTrabalho

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario, cargo, pis, linguagem:LinguagemProgramacao=None, equipe:EquipeTrabalho=None, id=0):
        super().__init__(nome, sobrenome, cpf, id)
        self.__salario = salario
        self.__cargo = cargo
        self.__pis = pis
        self.__linguagem = linguagem
        self.__equipe = equipe
    #getter
    def get_salario(self):
        return self.__salario

    def get_cargo(self):
        return self.__cargo
    
    def get_pis(self):
        return self.__pis

    def get_linguagem(self):        
        return self.__linguagem

    def get_equipe(self):
        return self.__equipe
