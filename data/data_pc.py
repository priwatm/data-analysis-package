# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with class for main components construction.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      Standard python module for operating with array's:
import numpy       as np
#      The module with class for data loading, keeping and preparation:
import data_simple as ds
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class data_pc(ds.data_simple):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,cns):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters and parent class data_simple.
        ___INPUT______________________________________________________________
        cns          - is the pointer to console
                       type: console class
        '''
        ds.data_simple.__init__(self,cns)
        self.cns = cns
        self.Obj = {'Module':'data.data_pc','Function':'__init__'}
        self.Clear() # Initialize parameters
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Clear(self):
        '''
        ___DESCRIPTION________________________________________________________
        Set all parameters for None values.
        '''
        ds.data_simple.Clear(self)
        self.Y               = None   # Array with principal components
        self.Yr              = None   # Reduced array with principal components
        self.Wt              = None   # Transformation matrix
        self.Eig             = None   # Eigenvalues for principal components
        self.IsConstructedPC = False
        self.IsReducedPC     = False
        self.Scale_PC        = True
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Scale_PC(self,Scale_PC=True):
        '''
        ___INPUT______________________________________________________________
        Scale_PC     - (optional) if is True, then data will scale 
                       according to their sigma
                       type: bool
        '''
        self.Scale_PC = Scale_PC
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def PCproject(self, x, minfrac=0.):
        '''
        ___DESCRIPTION________________________________________________________
        Project x onto the principle axes, 
        dropping any axes where fraction of variance<minfrac
        ___INPUT______________________________________________________________
        x            - is a data vector or matrix for projection in PC subspace
                       type: list, np.ndarray
        minfrac      - is a minimal fraction of variance for reduction
                       type: float 
        ___OUTPUT_____________________________________________________________
        Yreduced     - is a reduced data vector or matrix in PC subspace
                       type: np.ndarray
        '''
        self.Obj['Function']='PCproject'
        x = np.asarray(x)
        if (x.shape[-1]!=self.X.shape[1]):
            self.cns.msg(self.Obj,'Not correct size. Can not project data.','E')
            return -1
        Y = np.dot(self.Wt, self.PCcenter(x).T).T
        mask = self.fracs>=minfrac
        if len(x.shape)==2:
            Yreduced = Y[:,mask]
        else:
            Yreduced = Y[mask]
        return Yreduced
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def PCcenter(self, x):
        '''
        ___DESCRIPTION________________________________________________________
        Center and optionally standardize the data using 
        the mean and sigma from training data.
        ___INPUT______________________________________________________________
        x            - is a data vector for centering
                       type: list, np.ndarray
        ___OUTPUT_____________________________________________________________
        x_centered   - is a centered data vector
                       type: np.ndarray
        '''
        self.Obj['Function']='PCcenter'
        if (x.shape[-1]!=self.X.shape[1]):
            self.cns.msg(self.Obj,'Not correct size. Can not center data.','E')
            return -1
        if self.Scale_PC:
            return (x - self.M)/self.sigma
        else:
            return (x - self.M)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Construct_PC(self):
        '''
        ___DESCRIPTION________________________________________________________
        Construct principal components for prepared data.
        '''
        self.Obj['Function']='Construct_PC'
        if not self.IsPrepared:
            self.cns.msg(self.Obj,'Data are not prepared. Can not construct PC.','E')
            return -1
        if self.X.shape[0] < self.X.shape[1]:
            self.cns.msg(self.Obj,'Number of objects is less than properties. Can not construct PC.','E')
            return -1
        a = self.PCcenter(self.X)
        U, self.Eig, self.Wt = np.linalg.svd(a, full_matrices=False)
        self.Eig = self.Eig**2
        self.Y = np.dot(self.Wt,a.T).T
        vars = self.Eig/float(len(self.Eig))
        self.fracs = vars/vars.sum()
        self.IsConstructedPC = True
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Reduce_PC(self,Thr=None,Dim=None):
        '''
        ___DESCRIPTION________________________________________________________
        Reduce dimension of parameters space according constructed PC.
        '''
        self.Obj['Function']='Reduce_PC'
        if not self.IsConstructedPC:
            self.cns.msg(self.Obj,'PC is not constructed. Can not reduce dimension.','E')
            return -1
        if Thr==None and Dim==None:
            self.cns.msg(self.Obj,'Thr or Dim must be set for PC.','E')
            return -1
        if Thr!=None and Dim!=None:
            self.cns.msg(self.Obj,'Only one of Thr and Dim must be set for PC.','E')
            return -1
        self.PC_Dim=Dim
        self.PC_Thr=Thr
        if Dim!=None:
            self.Yr = self.Y[:,0:Dim]
            self.PC_Dim=Dim
            vars = self.Eig[0:Dim]/float(len(self.Eig))
            self.PC_VarPart = vars/vars.sum()
        
        if Thr!=None:
            mask = self.fracs>=Thr
            self.Yr = self.Y[:,mask]
            self.PC_Dim=len(mask)
            self.PC_VarPart=self.fracs[len(mask)-1]
        self.IsReducedPC = True
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Get_Y(self,Class=None,Redused=False):
        self.Obj['Function']='Get_Y'
        if Class==None:
            if Redused:
                return self.Yr
            else:
                return self.Y
        if not Class in self.Classes:
            self.cns.msg(self.Obj,'Incorrect class number. Can not get Y.','E')
            return -1
        Rows = []
        for i,Cl_Curr in enumerate(self.ObjClasses):
            if Cl_Curr==Class:
                Rows.append(i)
        if Redused:
            return self.Yr[Rows,:]
        else:
            return self.Y[Rows,:]
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        
        
        
        
        
        
        
        