import sys
#IMPORTAÇÃO path
sys.path.append("C:/Users/900224/Desktop/Aula6/trabalinho/")
from flask import Flask, render_template, request, redirect
from model.equipe_trabalho import EquipeTrabalho
from model.linguagem_programacao import LinguagemProgramacao
from model.funcionario import Funcionario
from dao.equipe_dao import EquipeDao
from dao.linguagem_dao import LinguagemDao
from dao.funcionario_dao import FuncionarioDao


linguagem_dao = LinguagemDao()
equipe_dao = EquipeDao()
funcionario_dao = FuncionarioDao()
app = Flask(__name__)


#Rota de listar
@app.route('/')
def listar():
    listar = funcionario_dao.listar()
    return render_template('listagem.html', funcionario=listar)

#Rota cadastrar Funcionario
@app.route('/cadastro_funcionario')
def cadastrar_funcionario(): 
    lista_equip = equipe_dao.listar_todas()
    lista_ling = linguagem_dao.listar_todas()
    return render_template('cadastro_funcionario.html', lista_equip=lista_equip, lista_ling=lista_ling)

#Rota cadastrar linguagem
@app.route('/cadastro_linguagem')
def cadastrar_linguagem():
    return render_template('cadastro_linguagem.html')

#Rota salvar linguagem
@app.route('/salvar_linguagem', methods=['POST'])
def salvar_linguagem():
    linguagem = request.form['linguagem']
    linguagem_dao.salvar_linguagem(linguagem)
    return redirect('/')

#Rota cadastrar equipe
@app.route('/cadastro_equipe')
def cadastrar_equipe():
    return render_template('cadastro_equipe.html')

#Rota Salvar equipe
@app.route('/salvar_equipe', methods=['POST'])
def salvar_equipe():
    equipe = request.form['nome_equipe']
    equipe_dao.salva_equipe(equipe)
    return redirect('/')

#Rota Salvar Funcionario
@app.route('/salvar', methods=['POST'])
def salvar_funcionario():
    id = int(request.form['id'])
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    salario = request.form['salario']
    cargo = request.form['cargo']
    pis = request.form['pis']
    linguagem_id = int(request.form['linguagem_id'])
    equipe_id = int(request.form['equipe_id'])
    linguagem = LinguagemProgramacao('', linguagem_id)
    equipe = EquipeTrabalho('', equipe_id)
    funcionario = Funcionario(nome, sobrenome, cpf,
                              salario, cargo, pis, linguagem, equipe, id)

    if(id == 0):
        funcionario_dao.inserir(funcionario)
    else:
        funcionario_dao.alterar(funcionario)
    return redirect('/')

    #Rota Editar Func
@app.route('/editar_funcionario')
def editar():
    id = request.args['id']
    funcionario = funcionario_dao.buscar_por_id(id)
    lista_equipes = equipe_dao.listar_todas()
    lista_linguagens = linguagem_dao.listar_todas()
    return render_template('editar.html', funcionario = funcionario, lista_equipes= lista_equipes, lista_linguagens=lista_linguagens )

#Rota Excluir Func
@app.route('/excluir_funcionario')
def deletar():
    id = request.args['id']
    funcionario_dao.deletar(id)
    return redirect('/')


app.run(port=80, debug=True)
