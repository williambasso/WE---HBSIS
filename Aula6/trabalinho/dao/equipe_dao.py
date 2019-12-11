from model.equipe_trabalho import EquipeTrabalho
from .basedao import BaseDao

class EquipeDao(BaseDao):
    #Listar Equipe
    def listar_todas(self):
        lista = []
        comando = "SELECT nome_equipe, id from equipe_trabalho"
        self.cursor.execute(comando)
        for e in self.cursor.fetchall():
            equipe = EquipeTrabalho(e[0], e[1])
            lista.append(equipe)
        return lista
    #Salvar Equipe
    def salva_equipe(self, equipe):
        comando = f'INSERT INTO equipe_trabalho VALUES(DEFAULT, "{equipe} ")'
        self.cursor.execute(comando)
        self.conn.commit()
        