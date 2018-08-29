# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module construct many graphs of selected type in one tab widget.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      The package that provide classes for working with Qt library:
from   PyQt4        import QtGui
#      Classes with different types of graphs:
import graph.graph_curves  as gc
import graph.graph_hist    as gh
import graph.graph_bar     as gb
import graph.graph_scatter as gs
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class graphs_tab(object):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,cns,parent):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters.
        ___INPUT______________________________________________________________
        cns          - is the pointer to console
                       type: console class
        parent       - is the widget that will contain the tab.
                       type: QtGui.QWidget
        '''
        self.cns    = cns
        self.parent = parent
        self.Obj    = {'Module':'graphs_tab','Function':'___'}
        self.Wtab   = QtGui.QTabWidget(self.parent) 
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.addWidget(self.Wtab)
        self.parent.setLayout(self.plotLayout)
        self.Graphs = dict()
        self.Hide()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create(self):
        self.Hide()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Delete(self):
        #self.Hide()
        for i,Name in enumerate(self.Graphs.iterkeys()):
            self.Wtab.removeTab(i)
        self.Graphs = dict()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Show(self):
        self.Wtab.show()
        for Name in self.Graphs.iterkeys():
            self.Graphs[Name].Show()
    def Hide(self):
        for Name in self.Graphs.iterkeys():
            self.Graphs[Name].Hide()
        self.Wtab.hide() 
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create_Graph(self,GrType,Name):
        '''
        ___DESCRIPTION________________________________________________________
        Create new graph of selected type and add it to tab.
        ___INPUT______________________________________________________________
        GrType       - is the type of graphs in the tab
                       type: str:
                           'curves','hist','bar'
        Name         - is the name of the graph
                       type: str
        '''
        self.Obj['Function']='Create_Graph'
        tab	= QtGui.QWidget()
        if GrType=='curves':
            self.Graphs[Name] = gc.graph_curves(self.cns,tab)
        elif GrType=='hist':
            self.Graphs[Name] = gh.graph_hist(self.cns,tab)
        elif GrType=='bar':
            self.Graphs[Name] = gb.graph_bar(self.cns,tab)
        elif GrType=='scatter':
            self.Graphs[Name] = gs.graph_scatter(self.cns,tab)
        else:
            self.cns.msg(self.Obj,'Unknown type of the graph.','E')
            return -1
        self.Graphs[Name].Set_ToolBarBtn()
        self.Wtab.addTab(tab,Name)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Get_Graph(self,Name):
        '''
        ___DESCRIPTION________________________________________________________
        Return a constructed before graph with given Name.
        ___INPUT______________________________________________________________
        Name         - is the name of the graph
                       type: str
        '''
        return self.Graphs[Name]
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        