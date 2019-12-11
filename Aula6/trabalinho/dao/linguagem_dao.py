from model.linguagem_programacao import LinguagemProgramacao
from .basedao import BaseDao


class LinguagemDao(BaseDao):
        #listar Ling
    def listar_todas(self):
        lista = []
        comando = "SELECT nome_linguagem, id from linguagens_programacao"
        self.cursor.execute(comando)
        for l in self.cursor.fetchall():
            linguagem = LinguagemProgramacao(l[0], l[1])
            lista.append(linguagem)
        return lista
        #Salvar Ling
    def salvar_linguagem(self, linguagem):
        comando = f"INSERT INTO linguagens_programacao VALUES (DEFAULT, '{linguagem}')"
        self.cursor.execute(comando)
        self.conn.commit()
