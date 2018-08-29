# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with class for data loading.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      Standard python module for operating with array's:
import numpy as np
#      Standard python module for operating with excel files
#      (Examples http://habrahabr.ru/post/99923/):
import xlrd
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class data_load(object):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,cns):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters.
        ___INPUT______________________________________________________________
        cns          - is the pointer to console
                       type: console class
        '''
        self.cns = cns
        self.Obj = {'Module':'data.data_load','Function':'__init__'}
        self.Clear() # Initialize parameters
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Clear(self):
        '''
        ___DESCRIPTION________________________________________________________
        Set all parameters for None values.
        '''
        self.Fpath        = None
        self.Rows         = [None,None]
        self.Cols         = [None,None]
        self.Splitter     = ';'
        self.Transpose    = False
        self.NamesInFileO = False
        self.NamesInFileP = False
        self.LastPrpIsCls = False
        self.X            = None   # Array with data
        self.ObjNames     = []     # Are names of the objects
        self.PrpNames     = []     # Are names of the properties
        self.ObjClasses   = None
        self.Classes      = None
        self.IsLoaded     = False
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Fpath(self,Fpath):
        '''
        ___INPUT______________________________________________________________
        Fpath        - is the path to file with data
                       type: str (.xls)
        '''
        self.Obj['Function']='Set_Fpath'
        if ('.xls' in Fpath) or ('.csv' in Fpath) or ('.txt' in Fpath):
            self.Fpath = Fpath
        else:
            self.cns.msg(self.Obj,'Incorrect format of the file: '+Fpath,'E')
            return -1
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_RC_limits(self,Rows,Cols):
        '''
        ___INPUT______________________________________________________________
        Rows,Cols    - are min and max numbers for rows and columns, 
                       type: list [2]
        '''
        self.Rows      = Rows
        self.Cols      = Cols
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Splitter(self,Splitter):
        '''
        ___INPUT______________________________________________________________
        Splitter     - is a splitter for data in rows for csv files, 
                       type: str
        '''
        self.Splitter  = Splitter
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_Transpose(self,Transpose):
        '''
        ___INPUT______________________________________________________________
        Transpose    - if is True, then Objects are in Rows 
                       and Properties are in Columns in file structure
                       type: bool
        '''
        self.Transpose = Transpose
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_NamesInFile(self,NamesInFileO,NamesInFileP):
        '''
        ___INPUT______________________________________________________________
        N_O,N_P      - if is True, then in the first Column/Row
                       the names of Object/Parameters are presented
                       type: bool
        '''
        self.NamesInFileO = NamesInFileO
        self.NamesInFileP = NamesInFileP
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_LastPrpIsCls(self,LastPrpIsCls):
        '''
        ___INPUT______________________________________________________________
        LastPrpIsCls - if is True, then the last property is a number of class
                       type: bool
        '''
        self.LastPrpIsCls = LastPrpIsCls
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Load_Data(self):
        self.Obj['Function']='Load_Data'
        if '.csv' in self.Fpath or '.txt' in self.Fpath:
            self.Load_Data_csv()
        elif '.xls' in self.Fpath:
            self.Load_Data_xls()
        else:
            self.cns.msg(self.Obj,'Incorrect format of the file.','E')
            return -1
        if self.LastPrpIsCls:
            self.ObjClasses = []
            self.Classes    = []
            for Cl in self.X[:,-1]:
                Cl = int(Cl)
                self.ObjClasses.append(Cl)
                if not Cl in self.Classes:
                    self.Classes.append(Cl)
            self.X = self.X[:,0:-1]
            if self.PrpNames!=None:
                self.PrpNames = self.PrpNames[0:-1]
        self.IsLoaded = True
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Load_Data_xls(self):
        '''
        ___DESCRIPTION________________________________________________________
        Load data X from selected excel file.
        '''
        self.Obj['Function']='Load_Data_xls'
        try:
            rb = xlrd.open_workbook(self.Fpath,formatting_info=True)
        except Exception as e:
            self.cns.msg(self.Obj,'Can not open .xls file. Reason: '+str(e),'E')
            return -1 
        sheet = rb.sheet_by_index(0)
        # Read names of objects and properties:
        try:
            if (self.Transpose==False and self.NamesInFileP==True):
                self.PrpNames = sheet.row_values(0)[1:]
            if (self.Transpose==True  and self.NamesInFileO==True):
                self.ObjNames = sheet.row_values(0)[1:]
            if (self.Transpose==False and self.NamesInFileO==True):
                self.ObjNames = sheet.col_values(0)[1:]
            if (self.Transpose==True  and self.NamesInFileP==True):
                self.PrpNames = sheet.col_values(0)[1:]
        except:
            self.cns.msg(self.Obj,'Empty .xls file.','E')
            return -1 
        # Read values:
        Rows = [0,sheet.nrows]
        if (self.Transpose==False and self.NamesInFileP==True) or \
           (self.Transpose==True  and self.NamesInFileO==True):
            Rows[0] = 1
        if self.Rows[0]!=None:
            Rows[0] = self.Rows[0]-1
        if self.Rows[1]!=None:
            Rows[1] = self.Rows[1]-1
        Cols = [0,sheet.ncols]
        if (self.Transpose==False and self.NamesInFileO==True) or \
           (self.Transpose==True  and self.NamesInFileP==True):
            Cols[0] = 1
        if self.Cols[0]!=None:
            Cols[0] = self.Cols[0]-1
        if self.Cols[1]!=None:
            Cols[1] = self.Cols[1]-1
        self.X = np.zeros((Rows[1]-Rows[0],Cols[1]-Cols[0]))
        r=-1
        for rownum in range(Rows[0],Rows[1]):
            r+=1
            row = sheet.row_values(rownum)
            c=-1
            for colnum in range(Cols[0],Cols[1]):
                c+=1
                try:
                    self.X[r,c] = float(row[colnum])
                except:
                    self.cns.msg(self.Obj,'Unsupported values in .xls file.','E')
                    return -1
        if self.Transpose==True:
            self.X = self.X.T
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=