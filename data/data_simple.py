# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with class for keeping data and calculating it's parameters.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      Standard python module for operating with array's:
import numpy     as np
#      The module with class for data loading (parent):
import data_load as dl
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class data_simple(dl.data_load):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,cns):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters and parent class data_load.
        ___INPUT______________________________________________________________
        cns          - is the pointer to console
                       type: console class
        '''
        dl.data_load.__init__(self,cns)
        self.cns = cns
        self.Obj = {'Module':'data.data_simple','Function':'__init__'}
        self.Clear() # Initialize parameters
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Clear(self):
        '''
        ___DESCRIPTION________________________________________________________
        Set all parameters for None values.
        '''
        dl.data_load.Clear(self)
        # Arrays with mean,variance for all parameters and Covariance matrix:
        self.M            = None 
        self.V            = None 
        self.sigma        = None 
        self.C            = None 
        # The same as above but for every class of input data:
        self.Mcl          = []
        self.Vcl          = []   
        self.Ccl          = [] 
        # Indicator for prepared data:
        self.IsPrepared   = False
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Prepare_Data(self):
        '''
        ___DESCRIPTION________________________________________________________
        Calculate statistical moments for data.
        '''
        self.Obj['Function']='Prepare_Data'
        if not self.IsLoaded:
            self.cns.msg(self.Obj,'Data are not loaded. Can not prepare.','E')
            return -1
        self.M = np.mean(self.X,axis=0)
        self.V = np.var (self.X,axis=0)
        self.sigma = self.V ** 0.5
        self.C = np.cov (self.X.T     )
        if self.Classes != None:
            for Cl in self.Classes:
                Xcl = self.Get_X(Cl)
                self.Mcl.append( np.mean(Xcl,axis=0) )
                self.Vcl.append( np.var (Xcl,axis=0) )
                self.Ccl.append( np.cov (Xcl.T     ) )
        self.IsPrepared = True
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Get_X(self,Class=None):
        self.Obj['Function']='Get_X'
        if Class==None:
            return self.X
        if not Class in self.Classes:
            self.cns.msg(self.Obj,'Incorrect class number. Can not get X.','E')
            return -1
        Rows = []
        for i,Cl_Curr in enumerate(self.ObjClasses):
            if Cl_Curr==Class:
                Rows.append(i)
        return self.X[Rows,:]
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        
        