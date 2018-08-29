# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with class for graph with curves construction.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      Parent class:
import graph_gui           as     graph_gui
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class graph_scatter(graph_gui.graph_gui):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,cns,parent):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters  and parent class.
        ___INPUT______________________________________________________________
        cns          - is the pointer to console
                       type: console class
        parent       - is the widget that will contain the graph.
                       type: QtGui.QWidget
        '''
        graph_gui.graph_gui.__init__(self,cns,parent)
        self.Obj    = {'Module':'graph_curves','Function':'__init__'}
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create(self):
        graph_gui.graph_gui.Create(self)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Delete(self):
        graph_gui.graph_gui.Delete(self)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Add_Line(self,X=None,Y=None,Lbl='None',color=None,area=None):
        '''
        ___DESCRIPTION________________________________________________________
        Plot XY.
        '''
        #colors = np.random.rand(N)
        #plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        if area==None:
            area = 3.14 * (4 * 1)**2
        if color==None:
            color = 'b'
        self.Obj['Function']='Add_Line'
        if X!=None and Y!=None:
            self.lines[self.lines_num] = self.ax.scatter(X,Y, s=area, 
                                         c=color, label=Lbl)
        else:
            self.lines[self.lines_num] = self.ax.plot([],[], label=Lbl)
        self.lines_num+=1
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Add_Data(self,X,Y,LineNum=None):
        '''
        ___DESCRIPTION________________________________________________________
        Plot XY.
        '''
        self.Obj['Function']='Set_Data'
        if LineNum == None:
            self.Add_Line(self,X=None,Y=None,Lbl='None')
            return
        if LineNum >= self.lines_num:
            self.cns.msg(self.Obj,'Incorrect number of line. Can not set data.','E')
            return -1
        self.lines[LineNum].set_data(X,Y)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        