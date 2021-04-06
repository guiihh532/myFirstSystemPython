from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    if formulario.radioButton.isChecked() :
        print("Categoria Informãtica Foi Selecionado")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Alimentos foi selecionada")
    else :
        print("Categoria eletronicos foi selecionado")
    
    print("teste")
    print("Código", linha1)
    print("Descrição", linha2)
    print("Preço", linha3)




app=QtWidgets.QApplication([])
formulario=uic.loadUi("pyForm/formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()

app.exec()