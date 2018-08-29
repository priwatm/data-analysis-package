# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with class for graph with error bars construction.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      Parent class:
import graph_gui           as     graph_gui
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class graph_bar(graph_gui.graph_gui):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,cns,parent):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters and parent class.
        ___INPUT______________________________________________________________
        cns          - is the pointer to console
                       type: console class
        parent       - is the widget that will contain the graph.
                       type: QtGui.QWidget
        '''
        graph_gui.graph_gui.__init__(self,cns,parent)
        self.Obj = {'Module':'graph_bar','Function':'___'}
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create(self):
        graph_gui.graph_gui.Create(self)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Delete(self):
        graph_gui.graph_gui.Delete(self)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Add_Line(self,X=None,Y=None,Ydelta=None,Lbl='None'):
        '''
        ___DESCRIPTION________________________________________________________
        Plot XY.
        '''
        self.Obj['Function']='Add_Line'
        if X!=None and Y!=None and Ydelta!=None:
            self.lines[self.lines_num] = self.ax.errorbar(X,Y,yerr=Ydelta,fmt='o',label=Lbl)
        else:
            self.lines[self.lines_num] = self.ax.errorbar([],[],yerr=[],fmt='o',label=Lbl)
        self.lines_num+=1
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Add_Data(self,X,Y,LineNum=None):
        '''
        ___DESCRIPTION________________________________________________________
        Plot XY.
        '''
        self.Obj['Function']='Set_Data'
        if LineNum == None:
            self.Add_Line(self,X=None,Y=None,Lbl='None',NumBins=10,normed=1)
            return
        if LineNum >= self.lines_num:
            self.cns.msg(self.Obj,'Incorrect number of line. Can not set data.','E')
            return -1
        self.lines[LineNum].set_data(X,Y)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        