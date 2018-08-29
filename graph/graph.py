# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with abstract class for graph construction.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      Submodules of standard python module for data plotting:
from matplotlib.figure import Figure
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class graph(object):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,cns):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters of calculation.
        ___INPUT______________________________________________________________
        cns          - is the pointer to console
                       type: console class
        '''
        self.cns        = cns
        self.Obj        = {'Module':'graph','Function':'___'}
        self.fig        = Figure()       
        self.ax         = self.fig.add_subplot(111)
        self.fig.subplots_adjust(left=0.1, bottom=0.2, right=0.9, top=0.9,
                                 wspace=0.01, hspace=0.01) 
        self.lines      = dict()
        self.lines_num  = 0
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create(self):
        self.fig        = Figure()       
        self.ax         = self.fig.add_subplot(111)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Delete(self):
        self.fig        = None       
        self.ax         = None 
        self.lines      = dict()
        self.lines_num  = 0
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Title(self,Title=None):
        if self.ax==None:
            self.cns.msg(self.Obj,'Graph is not created correctly.','E')
            return -1
        if Title!=None:
            self.ax.set_title(Title)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Labels(self,Xlbl=None,Ylbl=None):
        if self.ax==None:
            self.cns.msg(self.Obj,'Graph is not created correctly.','E')
            return -1
        if Xlbl!=None:
            self.ax.set_xlabel(Xlbl)
        if Ylbl!=None:
            self.ax.set_ylabel(Ylbl)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Limits(self,Xlim=None,Ylim=None):
        if self.ax==None:
            self.cns.msg(self.Obj,'Graph is not created correctly.','E')
            return -1
        if Xlim!=None:
            self.ax.set_xlim(Xlim[0],Xlim[1])
        if Ylim!=None:
            self.ax.set_xlim(Ylim[0],Ylim[1])
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_XTicks(self,X,Ticks,AutoLimit=True): 
        if self.ax==None:
            self.cns.msg(self.Obj,'Graph is not created correctly.','E')
            return -1
        self.ax.set_xticks(X)
        self.ax.set_xticklabels(Ticks)
        if AutoLimit:
            self.Set_Limits(Xlim=[X[0]-1,X[-1]+1])
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Grid(self,Grid=True):
        if self.ax==None:
            self.cns.msg(self.Obj,'Graph is not created correctly.','E')
            return -1
        self.ax.grid(Grid)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Legend(self,Legend=False):
        if self.ax==None:
            self.cns.msg(self.Obj,'Graph is not created correctly.','E')
            return -1
        if Legend:
            self.ax.legend()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_LogAxis(self,LogX=False,LogY=False):
        if self.ax==None:
            self.cns.msg(self.Obj,'Graph is not created correctly.','E')
            return -1
        if LogX:
            self.ax.set_xscale('log')
        if LogY:
            self.ax.set_yscale('log')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        