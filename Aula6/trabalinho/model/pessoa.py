class Pessoa:
    def __init__(self, nome, sobrenome, cpf, id=0):
        self.__id = id
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf    
    #getter
    def get_nome(self): 
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome
    
    def get_cpf(self):
        return self.__cpf
        
    def get_id(self):
        return self.__id
    

