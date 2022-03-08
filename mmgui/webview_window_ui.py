# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\python\testplus_pc\mmgui\tools\..\mmgui\webview_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WebViewWindowUI(object):
    def setupUi(self, WebViewWindowUI):
        WebViewWindowUI.setObjectName("WebViewWindowUI")
        WebViewWindowUI.resize(1098, 829)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ic/resource/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WebViewWindowUI.setWindowIcon(icon)
        WebViewWindowUI.setStyleSheet("")
        self.containerWidget = QtWidgets.QWidget(WebViewWindowUI)
        self.containerWidget.setStyleSheet("")
        self.containerWidget.setObjectName("containerWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.containerWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        WebViewWindowUI.setCentralWidget(self.containerWidget)
        self.menubar = QtWidgets.QMenuBar(WebViewWindowUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 23))
        self.menubar.setObjectName("menubar")
        WebViewWindowUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WebViewWindowUI)
        self.statusbar.setObjectName("statusbar")
        WebViewWindowUI.setStatusBar(self.statusbar)
        self.consoleLogDockWidget = QtWidgets.QDockWidget(WebViewWindowUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleLogDockWidget.sizePolicy().hasHeightForWidth())
        self.consoleLogDockWidget.setSizePolicy(sizePolicy)
        self.consoleLogDockWidget.setMinimumSize(QtCore.QSize(200, 46))
        self.consoleLogDockWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.consoleLogDockWidget.setObjectName("consoleLogDockWidget")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.consoleLogDockWidget.setWidget(self.dockWidgetContents_4)
        WebViewWindowUI.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.consoleLogDockWidget)
        self.actionDocument = QtWidgets.QAction(WebViewWindowUI)
        self.actionDocument.setObjectName("actionDocument")
        self.actionDeviceManagerView = QtWidgets.QAction(WebViewWindowUI)
        self.actionDeviceManagerView.setObjectName("actionDeviceManagerView")
        self.actionConsoleView = QtWidgets.QAction(WebViewWindowUI)
        self.actionConsoleView.setObjectName("actionConsoleView")
        self.actionWelcome = QtWidgets.QAction(WebViewWindowUI)
        self.actionWelcome.setObjectName("actionWelcome")
        self.actionSettings = QtWidgets.QAction(WebViewWindowUI)
        self.actionSettings.setObjectName("actionSettings")
        self.actionNew = QtWidgets.QAction(WebViewWindowUI)
        self.actionNew.setObjectName("actionNew")
        self.actionReportManager = QtWidgets.QAction(WebViewWindowUI)
        self.actionReportManager.setObjectName("actionReportManager")
        self.actionUpgrade = QtWidgets.QAction(WebViewWindowUI)
        self.actionUpgrade.setObjectName("actionUpgrade")
        self.actionAbout = QtWidgets.QAction(WebViewWindowUI)
        self.actionAbout.setObjectName("actionAbout")
        self.action_4 = QtWidgets.QAction(WebViewWindowUI)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(WebViewWindowUI)
        self.action_5.setObjectName("action_5")
        self.actionExit = QtWidgets.QAction(WebViewWindowUI)
        self.actionExit.setObjectName("actionExit")
        self.actionExportReport = QtWidgets.QAction(WebViewWindowUI)
        self.actionExportReport.setObjectName("actionExportReport")
        self.actionImportReport = QtWidgets.QAction(WebViewWindowUI)
        self.actionImportReport.setObjectName("actionImportReport")
        self.actionOpenReport = QtWidgets.QAction(WebViewWindowUI)
        self.actionOpenReport.setObjectName("actionOpenReport")
        self.actionReportComparerView = QtWidgets.QAction(WebViewWindowUI)
        self.actionReportComparerView.setObjectName("actionReportComparerView")
        self.actionConsole2View = QtWidgets.QAction(WebViewWindowUI)
        self.actionConsole2View.setObjectName("actionConsole2View")
        self.actionAccount = QtWidgets.QAction(WebViewWindowUI)
        self.actionAccount.setObjectName("actionAccount")

        self.retranslateUi(WebViewWindowUI)
        QtCore.QMetaObject.connectSlotsByName(WebViewWindowUI)

    def retranslateUi(self, WebViewWindowUI):
        _translate = QtCore.QCoreApplication.translate
        WebViewWindowUI.setWindowTitle(_translate("WebViewWindowUI", "mmgui"))
        self.consoleLogDockWidget.setWindowTitle(_translate("WebViewWindowUI", "Devtools"))
        self.actionDocument.setText(_translate("WebViewWindowUI", "文档"))
        self.actionDeviceManagerView.setText(_translate("WebViewWindowUI", "设备管理器"))
        self.actionConsoleView.setText(_translate("WebViewWindowUI", "调试控制台(js)"))
        self.actionWelcome.setText(_translate("WebViewWindowUI", "欢迎使用"))
        self.actionSettings.setText(_translate("WebViewWindowUI", "首选项"))
        self.actionNew.setText(_translate("WebViewWindowUI", "新建测试"))
        self.actionReportManager.setText(_translate("WebViewWindowUI", "报告管理器"))
        self.actionUpgrade.setText(_translate("WebViewWindowUI", "版本升级"))
        self.actionAbout.setText(_translate("WebViewWindowUI", "关于"))
        self.action_4.setText(_translate("WebViewWindowUI", "导入"))
        self.action_5.setText(_translate("WebViewWindowUI", "导出"))
        self.actionExit.setText(_translate("WebViewWindowUI", "退出"))
        self.actionExportReport.setText(_translate("WebViewWindowUI", "导出报告"))
        self.actionImportReport.setText(_translate("WebViewWindowUI", "导入报告"))
        self.actionOpenReport.setText(_translate("WebViewWindowUI", "打开本地报告"))
        self.actionReportComparerView.setText(_translate("WebViewWindowUI", "报告对比器"))
        self.actionConsole2View.setText(_translate("WebViewWindowUI", "调试控制台"))
        self.actionAccount.setText(_translate("WebViewWindowUI", "账户"))


from mmgui import res_rc
