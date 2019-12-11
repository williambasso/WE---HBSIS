import sys
sys.path.append("C:/Users/900224/Desktop/Aula6/trabalinho/")

from dao.basedao import BaseDao
from model.funcionario import Funcionario
from model.linguagem_programacao import LinguagemProgramacao
from model.equipe_trabalho import EquipeTrabalho

class FuncionarioDao(BaseDao):
    #Listar Dados Funcionario
    def listar(self):
        lista = []
        comando = """
        select 
            f.nome
            ,f.sobrenome
            ,f.cpf
            ,f.salario
            ,f.cargo
            ,f.pis
            ,f.id
            ,l.id
            ,l.nome_linguagem
            ,e.id
            ,e.nome_equipe
            from funcionarios as f
            join linguagens_programacao as l
            on f.linguagem_programacao = l.id
            join equipe_trabalho as e
            on f.equipe_trabalho = e.id
         """
        self.cursor.execute(comando)
        for f in self.cursor.fetchall():
            linguagem = LinguagemProgramacao(f[8], f[7])
            equipe = EquipeTrabalho(f[10],f[9])
            func = Funcionario(f[0],f[1],f[2],f[3],f[4],f[5],linguagem, equipe ,f[6])
            lista.append(func)

        return lista
        #buscar func id
    def buscar_por_id(self, id):
        comando = f"""
        select 
            f.nome
            ,f.sobrenome
            ,f.cpf
            ,f.salario
            ,f.cargo
            ,f.pis
            ,f.id
            ,l.id
            ,l.nome_linguagem
            ,e.id
            ,e.nome_equipe
            from funcionarios as f
            join linguagens_programacao as l
            on f.linguagem_programacao = l.id
            join equipe_trabalho as e
            on f.equipe_trabalho = e.id
            where f.id = {id}
         """
        self.cursor.execute(comando)
        f = self.cursor.fetchone()
        linguagem = LinguagemProgramacao(f[8], f[7])
        equipe = EquipeTrabalho(f[10],f[9])
        func = Funcionario(f[0],f[1],f[2],f[3],f[4],f[5],linguagem, equipe ,f[6])
        return func
    #Inserir Func
    def inserir(self, func: Funcionario):
        comando = f""" INSERT INTO funcionarios(
            nome, sobrenome, cpf, cargo, salario, pis, equipe_trabalho, linguagem_programacao

                    ) VALUES(
                        '{func.get_nome()}'
                        ,'{func.get_sobrenome()}'
                        ,'{func.get_cpf()}'
                        ,'{func.get_cargo()}'
                        ,{func.get_salario()}
                        ,{func.get_pis()}
                        ,{func.get_linguagem().get_id()}
                        ,{func.get_equipe().get_id()}
                    )"""

        self.cursor.execute(comando)
        self.conn.commit()
    #Alterar Func
    def alterar(self, func: Funcionario):
        comando = f'UPDATE funcionarios set nome = "{func.get_nome()}", sobrenome = "{func.get_sobrenome()}" , cpf = {func.get_cpf()}, cargo = "{func.get_cargo()}", salario = {func.get_salario()}, pis = {func.get_pis()}, equipe_trabalho = {func.get_equipe().get_id()}, linguagem_programacao = {func.get_linguagem().get_id()}  where id = {func.get_id()}'
        self.cursor.execute(comando)
        self.conn.commit()
    #Deletar Func
    def deletar(self, id):
        comando = f'DELETE from funcionarios where id = {id}'
        self.cursor.execute(comando)
        self.conn.commit()



