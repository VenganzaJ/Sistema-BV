# Form implementation generated from reading ui file 'Designer/untitled.ui'
#
# Created by: PyQt6 UI code generator 6.8.0.dev2410141303
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 650))
        MainWindow.setWindowTitle("")
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1024, 600))
        self.tabWidget.setMaximumSize(QtCore.QSize(1024, 600))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(350, 20, 301, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.Ag_LibEstado_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ag_LibEstado_LEdit.sizePolicy().hasHeightForWidth())
        self.Ag_LibEstado_LEdit.setSizePolicy(sizePolicy)
        self.Ag_LibEstado_LEdit.setObjectName("Ag_LibEstado_LEdit")
        self.gridLayout.addWidget(self.Ag_LibEstado_LEdit, 4, 1, 1, 1)
        self.agr_lib_btm = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.agr_lib_btm.setObjectName("agr_lib_btm")
        self.gridLayout.addWidget(self.agr_lib_btm, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(241, 57))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.Ag_LibISBN_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.Ag_LibISBN_LEdit.setObjectName("Ag_LibISBN_LEdit")
        self.gridLayout.addWidget(self.Ag_LibISBN_LEdit, 3, 1, 1, 1)
        self.Ag_LibAutor_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.Ag_LibAutor_LEdit.setObjectName("Ag_LibAutor_LEdit")
        self.gridLayout.addWidget(self.Ag_LibAutor_LEdit, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.Ag_LibTitulo_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.Ag_LibTitulo_LEdit.setObjectName("Ag_LibTitulo_LEdit")
        self.gridLayout.addWidget(self.Ag_LibTitulo_LEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.cancel_agr_lib_btm = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.cancel_agr_lib_btm.setObjectName("cancel_agr_lib_btm")
        self.gridLayout.addWidget(self.cancel_agr_lib_btm, 6, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(710, 20, 291, 521))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.edit_LibEstado_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.edit_LibEstado_LEdit.setObjectName("edit_LibEstado_LEdit")
        self.gridLayout_2.addWidget(self.edit_LibEstado_LEdit, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_10.setMaximumSize(QtCore.QSize(241, 57))
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)
        self.selct_isbn_comboBx = QtWidgets.QComboBox(parent=self.gridLayoutWidget_2)
        self.selct_isbn_comboBx.setObjectName("selct_isbn_comboBx")
        self.gridLayout_2.addWidget(self.selct_isbn_comboBx, 1, 1, 1, 1)
        self.edit_LibTitulo_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.edit_LibTitulo_LEdit.setObjectName("edit_LibTitulo_LEdit")
        self.gridLayout_2.addWidget(self.edit_LibTitulo_LEdit, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.edit_lib_btm = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.edit_lib_btm.setObjectName("edit_lib_btm")
        self.gridLayout_2.addWidget(self.edit_lib_btm, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.edit_LibAutor_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.edit_LibAutor_LEdit.setObjectName("edit_LibAutor_LEdit")
        self.gridLayout_2.addWidget(self.edit_LibAutor_LEdit, 3, 1, 1, 1)
        self.canc_edit_lib_btm = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.canc_edit_lib_btm.setObjectName("canc_edit_lib_btm")
        self.gridLayout_2.addWidget(self.canc_edit_lib_btm, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.tab)
        self.line.setGeometry(QtCore.QRect(310, -20, 21, 621))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.tab)
        self.line_2.setGeometry(QtCore.QRect(670, -20, 21, 621))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 281, 521))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.list_libros = QtWidgets.QListView(parent=self.verticalLayoutWidget_2)
        self.list_libros.setObjectName("list_libros")
        self.verticalLayout_2.addWidget(self.list_libros)
        self.consultar_libro_btm = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.consultar_libro_btm.setObjectName("consultar_libro_btm")
        self.verticalLayout_2.addWidget(self.consultar_libro_btm)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(350, 40, 291, 491))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.reg_usr_btm = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.reg_usr_btm.setObjectName("reg_usr_btm")
        self.gridLayout_3.addWidget(self.reg_usr_btm, 4, 0, 1, 1)
        self.Reg_UsrName_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_3)
        self.Reg_UsrName_LEdit.setObjectName("Reg_UsrName_LEdit")
        self.gridLayout_3.addWidget(self.Reg_UsrName_LEdit, 2, 1, 1, 1)
        self.Reg_UsrRol_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_3)
        self.Reg_UsrRol_LEdit.setObjectName("Reg_UsrRol_LEdit")
        self.gridLayout_3.addWidget(self.Reg_UsrRol_LEdit, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_14.setMaximumSize(QtCore.QSize(241, 57))
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)
        self.Reg_UsrID_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_3)
        self.Reg_UsrID_LEdit.setObjectName("Reg_UsrID_LEdit")
        self.gridLayout_3.addWidget(self.Reg_UsrID_LEdit, 1, 1, 1, 1)
        self.cancel_reg_usr_btm = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.cancel_reg_usr_btm.setObjectName("cancel_reg_usr_btm")
        self.gridLayout_3.addWidget(self.cancel_reg_usr_btm, 5, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(parent=self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(310, -30, 21, 621))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(parent=self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(660, -30, 21, 621))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(700, 40, 291, 491))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_26 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        self.label_26.setMaximumSize(QtCore.QSize(241, 57))
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)
        self.selct_usrID_comboBx = QtWidgets.QComboBox(parent=self.gridLayoutWidget_4)
        self.selct_usrID_comboBx.setObjectName("selct_usrID_comboBx")
        self.gridLayout_5.addWidget(self.selct_usrID_comboBx, 1, 1, 1, 1)
        self.Edit_Reg_UsrRol_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_4)
        self.Edit_Reg_UsrRol_LEdit.setObjectName("Edit_Reg_UsrRol_LEdit")
        self.gridLayout_5.addWidget(self.Edit_Reg_UsrRol_LEdit, 3, 1, 1, 1)
        self.Edit_Reg_UsrName_LEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_4)
        self.Edit_Reg_UsrName_LEdit.setObjectName("Edit_Reg_UsrName_LEdit")
        self.gridLayout_5.addWidget(self.Edit_Reg_UsrName_LEdit, 2, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 2, 0, 1, 1)
        self.edit_usr_btm = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.edit_usr_btm.setObjectName("edit_usr_btm")
        self.gridLayout_5.addWidget(self.edit_usr_btm, 4, 0, 1, 1)
        self.cancel_edit_lib_btm = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.cancel_edit_lib_btm.setObjectName("cancel_edit_lib_btm")
        self.gridLayout_5.addWidget(self.cancel_edit_lib_btm, 5, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 281, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_21 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.listUsuarios = QtWidgets.QListView(parent=self.verticalLayoutWidget)
        self.listUsuarios.setObjectName("listUsuarios")
        self.verticalLayout.addWidget(self.listUsuarios)
        self.consultar_usuarios_btm = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.consultar_usuarios_btm.setObjectName("consultar_usuarios_btm")
        self.verticalLayout.addWidget(self.consultar_usuarios_btm)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.line_5 = QtWidgets.QFrame(parent=self.tab_3)
        self.line_5.setGeometry(QtCore.QRect(360, 0, 21, 621))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(20, 30, 311, 521))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_6)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_6.addWidget(self.pushButton_13, 5, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 2, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 1, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_33.setObjectName("label_33")
        self.gridLayout_6.addWidget(self.label_33, 3, 0, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_6)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_6.addWidget(self.lineEdit_20, 2, 1, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_6)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_6.addWidget(self.lineEdit_21, 1, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_34.setMaximumSize(QtCore.QSize(241, 57))
        self.label_34.setObjectName("label_34")
        self.gridLayout_6.addWidget(self.label_34, 0, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_35.setObjectName("label_35")
        self.gridLayout_6.addWidget(self.label_35, 4, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_22.sizePolicy().hasHeightForWidth())
        self.lineEdit_22.setSizePolicy(sizePolicy)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_6.addWidget(self.lineEdit_22, 4, 1, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_6)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_6.addWidget(self.lineEdit_23, 3, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_6)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_6.addWidget(self.pushButton_14, 6, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(410, 30, 311, 521))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_7)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_7.addWidget(self.pushButton_15, 5, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(parent=self.gridLayoutWidget_7)
        self.label_36.setObjectName("label_36")
        self.gridLayout_7.addWidget(self.label_36, 2, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(parent=self.gridLayoutWidget_7)
        self.label_37.setObjectName("label_37")
        self.gridLayout_7.addWidget(self.label_37, 1, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(parent=self.gridLayoutWidget_7)
        self.label_38.setObjectName("label_38")
        self.gridLayout_7.addWidget(self.label_38, 3, 0, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_7)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_7.addWidget(self.lineEdit_24, 2, 1, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_7)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_7.addWidget(self.lineEdit_25, 1, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(parent=self.gridLayoutWidget_7)
        self.label_39.setMaximumSize(QtCore.QSize(241, 57))
        self.label_39.setObjectName("label_39")
        self.gridLayout_7.addWidget(self.label_39, 0, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(parent=self.gridLayoutWidget_7)
        self.label_40.setObjectName("label_40")
        self.gridLayout_7.addWidget(self.label_40, 4, 0, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_26.sizePolicy().hasHeightForWidth())
        self.lineEdit_26.setSizePolicy(sizePolicy)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_7.addWidget(self.lineEdit_26, 4, 1, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_7)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_7.addWidget(self.lineEdit_27, 3, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_7)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_7.addWidget(self.pushButton_16, 6, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 281, 521))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_27 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_4.addWidget(self.label_27)
        self.listView_4 = QtWidgets.QListView(parent=self.verticalLayoutWidget_4)
        self.listView_4.setObjectName("listView_4")
        self.verticalLayout_4.addWidget(self.listView_4)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_4.addWidget(self.pushButton_12)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 24))
        self.menubar.setObjectName("menubar")
        self.menuSalir = QtWidgets.QMenu(parent=self.menubar)
        self.menuSalir.setObjectName("menuSalir")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuSalir.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_4.setText(_translate("MainWindow", "Estado"))
        self.agr_lib_btm.setText(_translate("MainWindow", "Agregar"))
        self.label_3.setText(_translate("MainWindow", "ISBN"))
        self.label_5.setText(_translate("MainWindow", "Agregar un Nuevo Libro"))
        self.label_2.setText(_translate("MainWindow", "Autor"))
        self.label.setText(_translate("MainWindow", "Titulo"))
        self.cancel_agr_lib_btm.setText(_translate("MainWindow", "Cancelar"))
        self.label_10.setText(_translate("MainWindow", "Editar Informacion de los Libros"))
        self.label_9.setText(_translate("MainWindow", "Titulo"))
        self.label_8.setText(_translate("MainWindow", "ISBN"))
        self.edit_lib_btm.setText(_translate("MainWindow", "Editar"))
        self.label_6.setText(_translate("MainWindow", "Estado"))
        self.label_7.setText(_translate("MainWindow", "Autor"))
        self.canc_edit_lib_btm.setText(_translate("MainWindow", "Cancelar"))
        self.label_11.setText(_translate("MainWindow", "Libros Disponibles"))
        self.consultar_libro_btm.setText(_translate("MainWindow", "Consultar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Gestion de Libros"))
        self.reg_usr_btm.setText(_translate("MainWindow", "Registrar"))
        self.label_13.setText(_translate("MainWindow", "Rol"))
        self.label_16.setText(_translate("MainWindow", "ID"))
        self.label_14.setText(_translate("MainWindow", "Registrar Nuevo Usuario"))
        self.label_15.setText(_translate("MainWindow", "Nombre"))
        self.cancel_reg_usr_btm.setText(_translate("MainWindow", "Cancelar"))
        self.label_26.setText(_translate("MainWindow", "Editar Informacion de los Libros"))
        self.label_25.setText(_translate("MainWindow", "Rol"))
        self.label_23.setText(_translate("MainWindow", "ID"))
        self.label_22.setText(_translate("MainWindow", "Nombre"))
        self.edit_usr_btm.setText(_translate("MainWindow", "Editar"))
        self.cancel_edit_lib_btm.setText(_translate("MainWindow", "Cancelar"))
        self.label_21.setText(_translate("MainWindow", "Consultar Información de Usuarios"))
        self.consultar_usuarios_btm.setText(_translate("MainWindow", "Consultar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Gestion de Usuarios"))
        self.pushButton_13.setText(_translate("MainWindow", "Registrar"))
        self.label_31.setText(_translate("MainWindow", "Usuario"))
        self.label_32.setText(_translate("MainWindow", "Libro"))
        self.label_33.setText(_translate("MainWindow", "Fecha de Prestamo"))
        self.label_34.setText(_translate("MainWindow", "Registrar Prestamos"))
        self.label_35.setText(_translate("MainWindow", "Fecha de Devolucion"))
        self.pushButton_14.setText(_translate("MainWindow", "Cancelar"))
        self.pushButton_15.setText(_translate("MainWindow", "Registrar"))
        self.label_36.setText(_translate("MainWindow", "Usuario"))
        self.label_37.setText(_translate("MainWindow", "Libro"))
        self.label_38.setText(_translate("MainWindow", "Fecha de Prestamo"))
        self.label_39.setText(_translate("MainWindow", "Registrar Devolucion"))
        self.label_40.setText(_translate("MainWindow", "Fecha de Devolucion"))
        self.pushButton_16.setText(_translate("MainWindow", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Gestión de Préstamos"))
        self.label_27.setText(_translate("MainWindow", "Hiztorial de Prestamos y Devoluciones"))
        self.pushButton_12.setText(_translate("MainWindow", "Consultar Historial"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Historial"))
        self.menuSalir.setTitle(_translate("MainWindow", "Salir"))
