# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with abstract class for graph's gui interface.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      The package that provide classes for working with Qt library:
from   PyQt4                            import QtGui, QtCore
#      Submodules of standard python module for gui data plotting:
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg    as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
#      Parent class:
import graph                            as     graph
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class graph_gui(graph.graph,FigureCanvas):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,cns,parent):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters and parent classes.
        ___INPUT______________________________________________________________
        cns          - is the pointer to console
                       type: console class
        parent       - is the widget that will contain the graph.
                       type: QtGui.QWidget
        '''
        graph.graph.__init__(self,cns)
        self.parent = parent
        self.Obj = {'Module':'graph','Function':'___'}
        FigureCanvas.__init__(self, self.fig)        
        self.setParent(self.parent)
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.addWidget(self)
        self.parent.setLayout(self.plotLayout)
        FigureCanvas.updateGeometry(self)
        self.ToolBar    = None
        self.ToolBarBtn = None
        self.Hide()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create(self):
        graph.graph.Create(self)
        self.plotLayout.addWidget(self)
        FigureCanvas.updateGeometry(self)
        self.Hide()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Delete(self):
        graph.graph.Delete(self)
        self.plotLayout.removeWidget(self)
        self.ToolBar    = None
        self.ToolBarBtn = None
        FigureCanvas.updateGeometry(self)
        self.Hide()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Show(self):
        self.show()
        if self.ToolBarBtn!=None:
            self.ToolBarBtn.show()
            self.ToolBarBtn.activateWindow()
    def Hide(self):
        self.hide() 
        if self.ToolBar!=None:
            self.Hide_ToolBar()
        if self.ToolBarBtn!=None:
            self.ToolBarBtn.hide()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_ToolBar(self,wgt):
        self.ToolBar = NavigationToolbar(self,wgt)
        self.ToolBar.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
    def Get_ToolBar(self,wgt=None):
        self.Obj['Function']='Get_ToolBar'
        if self.ToolBar!=None and wgt==None:
            return self.ToolBar
        if wgt==None:
            if self.ToolBar!=None:
                return self.ToolBar
            else:
                self.cns.msg(self.Obj,'ToolBar is not constructed. Can not get.','E')
                return -1
        self.Set_ToolBar(wgt)
        return self.ToolBar
    def Show_ToolBar(self):
        self.Obj['Function']='Show_ToolBar'
        if self.ToolBar==None:
            self.cns.msg(self.Obj,'ToolBar is not constructed. Can not show.','E')
            return -1
        self.ToolBar.show()
    def Hide_ToolBar(self):
        self.Obj['Function']='Hide_ToolBar'
        if self.ToolBar==None:
            self.cns.msg(self.Obj,'ToolBar is not constructed. Can not hide.','E')
            return -1
        self.ToolBar.hide()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_ToolBarBtn(self,Btn=None):
        if Btn==None:
            self.ToolBarBtn = QtGui.QPushButton(self)
            self.ToolBarBtn.setGeometry(QtCore.QRect(0, 0, 31, 24))
            self.ToolBarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.ToolBarBtn.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/change_plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ToolBarBtn.setIcon(icon)
            self.ToolBarBtn.setIconSize(QtCore.QSize(80, 32))
            self.ToolBarBtn.setCheckable(True)
        else:
            self.ToolBarBtn = Btn
            self.ToolBarBtn.setParent(self)
        self.ToolBarBtn.toggled.connect(self.Event_ToolBarBtn)        
    def Event_ToolBarBtn(self,toggled):
        if toggled:
            self.Show_ToolBar()
        else:
            self.Hide_ToolBar()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        