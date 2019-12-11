class LinguagemProgramacao:
    def __init__(self, nome_linguagem, id=0):
        self.__id = id
        self.__nome_linguagem = nome_linguagem

    #getter
    def get_id(self):
        return self.__id

    def get_nome_linguagem(self):
        return self.__nome_linguagem

    def set_id(self, id):
        self.__id = id
