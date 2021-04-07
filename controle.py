from PyQt5 import uic,QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pikapau10",
    database="cadastro_produto"
)
def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))

    print(valor_id)


def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("pyForm/saves/cadastro_Produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Produtos Cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 33
        pdf.drawString(10, 750 -y, str(dados_lidos[i][0]))
        pdf.drawString(110, 750 -y, str(dados_lidos[i][1]))
        pdf.drawString(210, 750 -y, str(dados_lidos[i][2]))
        pdf.drawString(310, 750 -y, str(dados_lidos[i][3]))
        pdf.drawString(410, 750 -y, str(dados_lidos[i][4]))

    pdf.save()
    print("PDF FOI GERADO COM SUCESSO")

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

    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

    formulario.radioButton.setCheckable(False)
    formulario.radioButton_2.setCheckable(False)
    formulario.radioButton_3.setCheckable(False)


def chama_segunda_tela() :
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range (0, 5):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        
 

app=QtWidgets.QApplication([])
formulario=uic.loadUi("pyForm/formulario.ui")
segunda_tela=uic.loadUi("pyForm/ListaProdutos.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_dados)

formulario.show()
app.exec()



# Criando table

