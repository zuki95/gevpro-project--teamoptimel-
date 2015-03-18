import sys
from PyQt4 import QtGui

class ButtonBlock(QtGui.QWidget):

    def __init__(self, *args):
        super(QtGui.QWidget, self).__init__()
        grid = QtGui.QGridLayout()
        names = ('0,0', '0,1', '0,2', '0,3', '0,4', '', '1,0', '1,1', '1,2', '1,3', '1,4',
                 '0,0', '0,1', '0,2', '0,3', '0,4', '', '1,0', '1,1', '1,2', '1,3', '1,4',
                 '0,0', '0,1', '0,2', '0,3', '0,4', '', '1,0', '1,1', '1,2', '1,3', '1,4',
                 '0,0', '0,1', '0,2', '0,3', '0,4', '', '1,0', '1,1', '1,2', '1,3', '1,4',
                 '0,0', '0,1', '0,2', '0,3', '0,4', '', '1,0', '1,1', '1,2', '1,3', '1,4',
                 '0,0', '0,1', '0,2', '0,3', '0,4', '', '1,0', '1,1', '1,2', '1,3', '1,4',
                 '1,0', '1,1', '1,2', '1,3', '1,4', '', '1,0', '1,1', '1,2', '1,3', '1,4')
        for i, name in enumerate(names):
            button = QtGui.QPushButton(name, self)
            button.clicked.connect(self.make_calluser(name))
            row, col = divmod(i, 11)
            grid.addWidget(button, row, col)
        self.setLayout(grid)

    def make_calluser(self, name):
        def calluser():
            print(name)

        return calluser

app = QtGui.QApplication(sys.argv)
tb = ButtonBlock()
tb.show()
app.exec_()
