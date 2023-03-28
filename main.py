import sys
from PyQt5 import QtWidgets
from tab import Ui_MainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTreeView, QListWidget, QTabWidget, QPushButton, QWidget, QMainWindow
class AppDemo(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # tüm tablar arasında paylaşılacak bir QWidget nesnesi yaratılır
        self.tree_view_widget = QWidget(self)
        self.tree_view_widget.setGeometry(30, 30, 200, 300)

        # QWidget üzerine QTreeView nesnesi eklenir
        self.tree_view = QTreeView(self.tree_view_widget)
        self.tree_view.setGeometry(30, 10, 200, 300)
        
        # Add Tab butonu
        pushButton = QPushButton('Add Tab', self)
        pushButton.setGeometry(200, 400,100,30)
        pushButton.clicked.connect(self.add_new_tab)
        
        #Remove Tab butonu
        pushButton_2 = QPushButton('Remove Tab', self)
        pushButton_2.setGeometry(310, 400,100,30)
        pushButton_2.clicked.connect(self.remove_tab)
        # QStandardItemModel nesnesi oluşturulur ve treeview'e eklenir
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Tab List'])
        self.tree_view.setModel(self.model)

        self.checkBox.stateChanged.connect(self.cb_close)
        self.checkBox_2.stateChanged.connect(self.cb2_close)
        self.checkBox_3.stateChanged.connect(self.cb3_close)
        self.checkBox_4.stateChanged.connect(self.cb4_close)   
        self.tab.setStyleSheet("background-color: rgb(170, 170, 255);")
 
        self.tabWidget.setTabVisible(3, False)
        self.tabWidget.setTabVisible(1, False)
        self.tabWidget.setTabVisible(2, False)
        self.tabWidget.setTabVisible(4, False)
 
    
    def add_new_tab(self):
        print("pressed add")
        new_tab = QWidget()
        self.tabWidget.addTab(new_tab, "New Tab")
        self.tabWidget.setStyleSheet("background-color: rgb(100, 100, 205);")
        self.tabWidget.setCurrentWidget(new_tab)

        item=QStandardItem("New Tab")
        self.model.appendRow(item)

    def remove_tab(self):
        print("pressed remove")
        current_index = self.tabWidget.currentIndex()

        if current_index >= 4:
            self.tabWidget.setTabVisible(current_index, False)
            self.model.removeRow(current_index - 4)

    def cb_close(self):
        if self.checkBox.isChecked():
            self.tabWidget.setTabVisible(1, True)
            self.tab_2.setStyleSheet("background-color: rgb(163, 215, 190);")
            item = QStandardItem("Tab A")
            self.model.appendRow(item)
        else:
            self.tabWidget.setTabVisible(1, False)
            self.model.removeRows(0, 1)

    def cb2_close(self):
        if self.checkBox_2.isChecked():
            self.tabWidget.setTabVisible(2, True)
            self.tab_3.setStyleSheet("background-color: rgb(183, 255, 101);")
            item = QStandardItem("Tab B")
            self.model.appendRow(item)
        else:
            self.tabWidget.setTabVisible(2, False)
            self.model.removeRows(0, 1)

    def cb3_close (self):
        if self.checkBox_3.isChecked():
            self.tabWidget.setTabVisible(3, True)
            self.tab_4.setStyleSheet("background-color: rgb(255, 115, 141);")
            item = QStandardItem("Tab C")
            self.model.appendRow(item)
        else:
            self.tabWidget.setTabVisible(3, False)
            self.model.removeRows(0, 1)

    def cb4_close (self):
        if self.checkBox_4.isChecked():
            self.tabWidget.setTabVisible(4, True)
            self.tab_5.setStyleSheet("background-color: rgb(103, 105, 211);")
            item = QStandardItem("Tab D")
            self.model.appendRow(item)
        else:
            self.tabWidget.setTabVisible(4, False)
            self.model.removeRows(0, 1)
     
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AppDemo()
    window.show()
    sys.exit(app.exec_())