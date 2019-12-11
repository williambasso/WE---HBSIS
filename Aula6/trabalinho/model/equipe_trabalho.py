
class EquipeTrabalho:
    def __init__(self, nome, id=0):
        self.__id = id
        self.__nome = nome
    #getter
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome

    # setter
    def set_nome(self, nome):
        self.__nome = nome

    def set_id(self, id):
        self.__id = id