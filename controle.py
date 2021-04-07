from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pikapau10",
    database="cadastro_produto"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""

    if formulario.radioButton.isChecked() :
        print("Categoria Informãtica Foi Selecionado")
        categoria = "Informãtica"
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Alimentos foi selecionada")
        categoria = "Alimentos"
    else :
        print("Categoria eletronicos foi selecionado")
        categoria = "eletronicos"
    
    print("teste")
    print("Código", linha1)
    print("Descrição", linha2)
    print("Preço", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()




app=QtWidgets.QApplication([])
formulario=uic.loadUi("pyForm/formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()

app.exec()



# Criando table

