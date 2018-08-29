# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with class for graph histogram construction.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      Parent class:
import graph_gui           as     graph_gui
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class graph_hist(graph_gui.graph_gui):
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
        self.Obj = {'Module':'graph_hist','Function':'__init__'}
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create(self):
        graph_gui.graph_gui.Create(self)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Delete(self):
        graph_gui.graph_gui.Delete(self)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Add_Line(self,Y=None,Lbl='None',NumBins=10,normed=1):
        '''
        ___DESCRIPTION________________________________________________________
        Plot XY.
        '''
        if Y!=None:
            self.lines[self.lines_num] = self.ax.hist(Y, NumBins, normed=1, label=Lbl)
            # facecolor='green', alpha=0.75
        else:
            self.lines[self.lines_num] = self.ax.hist([], NumBins, normed=1, label=Lbl)
            # facecolor='green', alpha=0.75 
        self.lines_num+=1
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Add_Data(self,Y,LineNum=None):
        '''
        ___DESCRIPTION________________________________________________________
        Plot XY.
        '''
        self.Obj['Function']='Set_Data'
        if LineNum == None:
            self.Add_Line(self,Y=None,Lbl='None',NumBins=10,normed=1)
            return
        if LineNum >= self.lines_num:
            self.cns.msg(self.Obj,'Incorrect number of line. Can not set data.','E')
            return -1
        self.lines[LineNum].set_data(Y)
        #self.fig.canvas.draw()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        