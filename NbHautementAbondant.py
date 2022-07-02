from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def testPQ(p,q):
    return 3<p<q<100

def sommeDiviseursPlus(n):
    i=1
    s=n
    while i<=n//2:
        if n%i==0:
            s+=i
        i+=1
    return s
def testHondulant(n):
    i=1
    t=True
    while i<n and t:
        t=sommeDiviseursPlus(i)<sommeDiviseursPlus(n)
        i+=1
    return t

def Play():
    p=windows.nb1LineEdit.text()
    q=windows.nb2LineEdit.text()
    if not p.isnumeric() or not q.isnumeric or not testPQ(int(p),int(q)):
        windows.textEdit.clear()
        windows.textEdit.hide() 
        windows.label_3.setText("Saisir 2 entiers p et q avec 3<p<q<100")
    else:
        windows.label_3.setText("Les nombres hautement abondants compris entrte "+p+" et "+q+" sont :")
        ch=""
        for i in range(int(p),int(q)+1):
            if testHondulant(i):
                ch = ch+str(i)+"\n"
        if ch:
            windows.label_3.setText("Les nombres hautement abondants compris entrte "+p+" et "+q+" sont :")
            windows.textEdit.show()    
            windows.textEdit.setText(ch)
        else:
            windows.textEdit.clear()
            windows.textEdit.hide()
            windows.label_3.setText("Aucun nombre abondant compris entrte "+p+" et "+q+" !")

app = QApplication([])
windows = loadUi("InterfaceHautementAbondant.ui")
windows.show()
windows.nb1LineEdit.setFocus()
windows.textEdit.hide()
windows.textEdit.setReadOnly(True)
windows.pushButton.clicked.connect(Play)
app.exec_()