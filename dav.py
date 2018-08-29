# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The main module in package of data analysis and visualization (dav).
  This package transform input data to the subspace of lower dimension
  with using of principal components method and plot them in different forms.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Module's import
#      Standard python module with system functions:
import sys
#      Standard python module for operating with array's:
import numpy as np
#      The package that provide classes for working with Qt library:
from   PyQt4                       import QtGui
#      The module with class for output text messages:
import console.console             as console
#      The main form (ui) of the application that was created in Qt designer:
import appMainWindow.ui            as ui
#      The main window of the application:
import appMainWindow.appMainWindow as appMainWindow
#      The module with class for data loading,keeping, preparation
#      and transormation to main components subspace:
import data.data_pc                as data_pc
#      The modules with classes for plots and histograms construction:
import graph.graph_curves  as gc
import graph.graph_hist    as gh
import graph.graph_bar     as gb
#      The module with clas for plot many graphs in tabs:
import graphs.graphs_tab   as gst
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class dav(object):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self):
        '''
        ___DESCRIPTION________________________________________________________
        Initialize parameters and create gui application.
        '''
        self.Obj   = {'Module':'dav','Function':'__init__'}
        # Initialization of application:
        self.app   = QtGui.QApplication([])     
        # Loading of UI that was constructed in Qt designer:
        self.UI    = ui.Ui_MainWindow()         
        # Creation of application's main window: 
        self.AMW   = appMainWindow.appMainWindow(self.UI) 
        # Console class initialization:
        self.cns   = console.console(Verb=3)    
        # Console messages will be printed in Tedt_Console widget:
        self.cns.SetGuiTedt(self.UI.Tedt_Console)
        # Console error and warning messages will be showed 
        # in special modal window, that is created by call:
        self.cns.SetGuiWgt(self.AMW)
        # Set main signals in application:
        self.Set_AppInteractions() 
        # Create data (Initialization of data class):
        self.Create_Data()
        # Create graphs Initialization of graphs classes):
        self.Create_Graphs() 
        # Max number of graphs in one tab:
        self.GrFigMax = 10        
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def AppStart(self):
        '''
        ___DESCRIPTION________________________________________________________
        Open gui application.
        '''
        self.Obj['Function']='AppStart'
        # Show the main window on display:
        self.AMW.show()                       
        self.cns.msg(self.Obj,'GUI application is going to start.','P')
        # Start of the UI application. (Then the function app.exec_() 
        # finish work, the standard exit method from system module is called):
        sys.exit(self.app.exec_())
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_AppInteractions(self):
        '''
        ___DESCRIPTION________________________________________________________
        Set signals for main application actions
        (create signal-slot connections).
        '''
        # Creation of dialog for file openning:
        def showDialog():
           filename = QtGui.QFileDialog.getOpenFileName(self.AMW, 'Open file', '../data/')
           self.UI.LEdt_ImportFileName.setText(filename)
        # Then "Choos eFile" button is clicked, then "showDialog" function is called:
        self.UI.Btn_Import_ChooseFile.clicked.connect(showDialog)
        # Then "Import" button is clicked, then "Import" function is called:
        self.UI.Btn_Import.clicked.connect(self.Import)
        # Then "Prepare Date" button is clicked, then "PrepareDate" function is called:
        self.UI.Btn_PrepareDate.clicked.connect(self.Prepare_Data)
        # Then "Btn_CalculatePC" button is clicked, then "CalculatePC" function is called:
        self.UI.Btn_CalculatePC.clicked.connect(self.CalculatePC)
        # Then "Btn_ReducePC" button is clicked, then "ReducePC" function is called:
        self.UI.Btn_ReducePC.clicked.connect(self.ReducePC)
        # Then "MultiGraphPlot" button is clicked, then "MultiGraphPlot" function is called:
        self.UI.Btn_MultiGraphPlot1.clicked.connect(self.MultiPlot1)
        self.UI.Btn_MultiGraphPlot2.clicked.connect(self.MultiPlot2)
        # Then "Reset" button is clicked, then "Reset" function is called:
        self.UI.Btn_Reset.clicked.connect(self.Reset)
        # Then gui is openned, then active tab is the Info tab:
        self.UI.MainTab.setCurrentIndex(4)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create_Data(self):
        self.Data  = data_pc.data_pc(self.cns) 
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Create_Graphs(self):
        self.Gr_Import_M  = gst.graphs_tab (self.cns,self.UI.Wgt_Import_M)
        self.Gr_Import_MV = gb.graph_bar   (self.cns,self.UI.Wgt_Import_MV) 
        self.Gr_PCsigma   = gc.graph_curves(self.cns,self.UI.Wgt_Transform)
        self.Gr_Main1     = gst.graphs_tab (self.cns,self.UI.Wgt_MultiGraphPlot1)
        self.Gr_Main2     = gst.graphs_tab (self.cns,self.UI.Wgt_MultiGraphPlot2)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Init_Labels(self):
        self.UI.Lbl_NumObj.setText(str(0))
        self.UI.Lbl_NumPrp.setText(str(0))
        self.UI.Lbl_NumCls.setText(str(0))
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Reset(self):
        self.Gr_Import_M.Delete()
        self.Gr_Import_MV.Delete()
        self.Create_Data()
        self.Create_Graphs()
        self.Init_Labels()
        self.cns.msg(self.Obj,'Program is restarted.','R')
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Import(self):
        self.Obj['Function']='Import'
        # Read all information about data file from forms:
        self.Data.Set_Fpath(self.UI.LEdt_ImportFileName.text())
        I,J = [None,None],[None,None]
        if self.UI.RBtn_ThirstRowNumber.isChecked(): 
            I[0] = int(self.UI.LEdt_ThirstRowNumber.text())
        if self.UI.RBtn_LastRowNumber.isChecked(): 
            I[1] = int(self.UI.LEdt_LastRowNumber.text())
        if self.UI.RBtn_ThirstColumnNumber.isChecked(): 
            J[0] = int(self.UI.LEdt_ThirstColumnNumber.text())
        if self.UI.RBtn_LastColumnNumber.isChecked(): 
            J[1] = int(self.UI.LEdt_LastColumnNumber.text())  
        self.Data.Set_RC_limits(I,J)
        if self.UI.RBtn_SplitterMask.isChecked(): 
            self.Data.Set_Splitter(self.UI.LEdt_SplitterMask.text())
        self.Data.Set_Transpose(self.UI.RBtn_PropInC.isChecked())
        N_O,N_P = False,False
        if self.UI.RBtn_NamesInFile_Obj.isChecked(): 
            N_O = True
        if self.UI.RBtn_NamesInFile_Param.isChecked(): 
            N_P = True
        self.Data.Set_NamesInFile(N_O,N_P)
        if self.UI.RBtn_ClassesInFile.isChecked(): 
            self.Data.Set_LastPrpIsCls(True)
        # Load data:
        self.Data.Load_Data()
        self.cns.msg(self.Obj,'Data are loaded from file.','R')
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Prepare_Data(self):
        self.Obj['Function']='Prepare_Data'
        if not self.Data.IsLoaded:
            self.cns.msg(self.Obj,'Data are not loaded. Can not prepare.','E')
            return -1
        # Calculate statistical moments of data matrix:
        self.Data.Prepare_Data()
        self.cns.msg(self.Obj,'Data are prepared.','R')
        # Plot tab-graphs for data (values distribution for all parameters):
        for i,Name in enumerate(self.Data.PrpNames):
            self.Gr_Import_M.Create_Graph('hist',Name)
            self.Gr_Import_M.Get_Graph(Name).Set_Title("Distribution of parameter's values")
            self.Gr_Import_M.Get_Graph(Name).Set_ToolBar(self.UI.Wgt_Mpl_ToolBar)
            self.Gr_Import_M.Get_Graph(Name).Set_Labels('Values','Counts')
            self.Gr_Import_M.Get_Graph(Name).Set_Grid(False)  
            self.Gr_Import_M.Get_Graph(Name).Add_Line(Y=self.Data.X[:,i],
                                                      Lbl=Name,
                                                      NumBins=min(10,int(self.Data.X.shape[0]/10)),
                                                      normed=1)
            self.Gr_Import_M.Get_Graph(Name).Set_Legend(True)                
        self.Gr_Import_M.Show()
        # Plot bar-graphs for data (mean and sigma for all classes):
        self.Gr_Import_MV.Set_Title('Mean and sigma for all classes')
 
        x = np.arange(1,len(self.Data.PrpNames)+1)
        self.Gr_Import_MV.Set_XTicks(x,self.Data.PrpNames)
        for i,Cl in enumerate(self.Data.Classes):
            self.Gr_Import_MV.Add_Line(X      = x,
                                       Y      = self.Data.Mcl[i],
                                       Ydelta = self.Data.Vcl[i]**0.5,
                                       Lbl    = Cl )
        self.Gr_Import_MV.Set_ToolBarBtn()
        self.Gr_Import_MV.Set_ToolBar(self.UI.Wgt_Mpl_ToolBar)
        self.Gr_Import_MV.Set_Labels(None,None)
        self.Gr_Import_MV.Set_Grid(False) 
        self.Gr_Import_MV.Set_Legend(True)
        self.Gr_Import_MV.Show()
        self.cns.msg(self.Obj,'Graps for input data are prepared.','R')
        # Show values of data lengths:
        self.UI.Lbl_NumObj.setText(str(self.Data.X.shape[0]))
        self.UI.Lbl_NumPrp.setText(str(self.Data.X.shape[1]))
        self.UI.Lbl_NumCls.setText(str(len(self.Data.Classes)))
        self.cns.msg(self.Obj,"Values for input data's lengths are calculated.",'R')
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def CalculatePC(self):
        self.Obj['Function']='CalculatePC'
        if not self.Data.IsPrepared:
            self.cns.msg(self.Obj,'Data are not prepared. Can not construct PC.','E')
            return -1
        if self.UI.RBtn_PC_scale.isChecked(): 
            self.Data.Set_Scale_PC(True)
        else:
            self.Data.Set_Scale_PC(False)   
        self.Data.Construct_PC()
        self.cns.msg(self.Obj,'Principal components are calculated.'+self.Data.Fpath+'.','R')
        self.Gr_PCsigma.Set_Title('Fraction of variance for principal components')
        x = np.arange(1,len(self.Data.fracs)+1)
        y = self.Data.fracs
        self.Gr_PCsigma.Add_Line(X=x,Y=y,Lbl='None')
        self.Gr_PCsigma.Set_XTicks(x,[int(t) for t in x],AutoLimit=False)
        self.Gr_PCsigma.Set_Limits(Xlim=[x[0],x[-1]])
        self.Gr_PCsigma.Set_ToolBarBtn()
        self.Gr_PCsigma.Set_ToolBar(self.UI.Wgt_Mpl_ToolBar)
        self.Gr_PCsigma.Set_Labels('Number of parameter','Fraction')
        self.Gr_PCsigma.Set_LogAxis(False,True)
        self.Gr_PCsigma.Set_Grid(True) 
        self.Gr_PCsigma.Set_Legend(False)
        self.Gr_PCsigma.Show()
        self.cns.msg(self.Obj,'Grap for PC sigma is prepared.','R')          
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def ReducePC(self):
        self.Obj['Function']='ReducePC'
        if not self.Data.IsConstructedPC:
            self.cns.msg(self.Obj,'PC is not constructed. Can not reduce dimension.','E')
            return -1
        if self.UI.RBtn_PC_thr.isChecked(): 
            Thr = float(self.UI.LEdt_PC_thr.text())
        else:
            Thr = None
        if self.UI.RBtn_PC_dim.isChecked(): 
            Dim = int(self.UI.LEdt_PC_dim.text())
        else:
            Dim = None
        self.Data.Reduce_PC(Thr,Dim)
        self.cns.msg(self.Obj,"Dimension of input data is reduced.",'R')
        # Show values of data lengths:
        self.UI.Lbl_PCdim.setText(str(self.Data.PC_Dim))
        self.UI.Lbl_PCvar.setText('%7.2e'%self.Data.PC_VarPart)
        self.cns.msg(self.Obj,"Values for reduced dimension are calculated.",'R')
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def MultiPlot1(self):
        self.Obj['Function']='MultiPlot1'
        if self.UI.RBtn_MultiGraphPlot_UsePC1.isChecked()     and \
           self.UI.RBtn_MultiGraphPlot_UsePCred1.isChecked():
               self.cns.msg(self.Obj,'Only one option Y/Yred may be selected.','W')
               return -1
        if self.UI.RBtn_MultiGraphPlot_UsePC1.isChecked(): 
            if not self.Data.IsConstructedPC:
                self.cns.msg(self.Obj,'PC is not prepared for data. Can not plot.','E')
                return -1
            self.MultiPlot(self.Gr_Main1,'Y')
        elif self.UI.RBtn_MultiGraphPlot_UsePCred1.isChecked(): 
            if not self.Data.IsReducedPC:
                self.cns.msg(self.Obj,'Data are not reduced in PC. Can not plot.','E')
                return -1
            self.MultiPlot(self.Gr_Main1,'Yr')
        else:
            if not self.Data.IsPrepared:
                self.cns.msg(self.Obj,'Data are not prepared. Can not plot.','E')
                return -1
            self.MultiPlot(self.Gr_Main1,'X')
        self.Gr_Main1.Show()
        self.cns.msg(self.Obj,"Main graph 1 is prepared.",'R')
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def MultiPlot2(self):
        self.Obj['Function']='MultiPlot2'
        if self.UI.RBtn_MultiGraphPlot_UsePC2.isChecked()     and \
           self.UI.RBtn_MultiGraphPlot_UsePCred2.isChecked():
               self.cns.msg(self.Obj,'Only one option Y/Yred may be selected.','W')
               return -1
        if self.UI.RBtn_MultiGraphPlot_UsePC2.isChecked(): 
            if not self.Data.IsConstructedPC:
                self.cns.msg(self.Obj,'PC is not prepared for data. Can not plot.','E')
                return -1
            self.MultiPlot(self.Gr_Main2,'Y')
        elif self.UI.RBtn_MultiGraphPlot_UsePCred2.isChecked(): 
            if not self.Data.IsReducedPC:
                self.cns.msg(self.Obj,'Data are not reduced in PC. Can not plot.','E')
                return -1
            self.MultiPlot(self.Gr_Main2,'Yr')
        else:
            if not self.Data.IsPrepared:
                self.cns.msg(self.Obj,'Data are not prepared. Can not plot.','E')
                return -1
            self.MultiPlot(self.Gr_Main2,'X')
        self.Gr_Main2.Show()
        self.cns.msg(self.Obj,"Main graph 2 is prepared.",'R')
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def MultiPlot(self,Gr,Dtype='X'):
        Cnum = 0
        Colors = ['r','g','b','m','y']
        if Dtype=='X':
           ParamMax = self.Data.X.shape[1]
        elif Dtype=='Y':
           ParamMax = self.Data.Y.shape[1]
        elif Dtype=='Yr':
           ParamMax = self.Data.Yr.shape[1]
        else:
           self.cns.msg(self.Obj,'Unknown type of data.','E')
           return -1
        for i in range(ParamMax):
            for j in range(i+1,ParamMax):
                Cnum+=1
                if Cnum>=self.GrFigMax:
                    self.cns.msg(self.Obj,'Too many parameters for plot.','W')
                    return -1
                Name = '%s%d vs %s%d'%(Dtype,i+1,Dtype,j+1)
                Gr.Create_Graph('scatter',Name)
                Gr.Get_Graph(Name).Set_ToolBar(self.UI.Wgt_Mpl_ToolBar)
                Gr.Get_Graph(Name).Set_Labels('%s%d'%(Dtype,i+1),'%s%d'%(Dtype,j+1))
                Gr.Get_Graph(Name).Set_Grid(False)  
                for k,Cl in enumerate(self.Data.Classes):
                    if Dtype=='X':
                       Valfull = self.Data.Get_X(Cl)
                    elif Dtype=='Y':
                       Valfull = self.Data.Get_Y(Cl,Redused=False)
                    elif Dtype=='Yr':
                       Valfull = self.Data.Get_Y(Cl,Redused=True)
                    X    = Valfull[:,i]
                    Y    = Valfull[:,j]
                    Gr.Get_Graph(Name).Add_Line(X,Y,'Class '+str(Cl),color=Colors[k])
                Gr.Get_Graph(Name).Set_Legend(True)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if __name__ == "__main__":
    # Create the object of main (dav) class and start gui application:
    DAV  = dav()
    DAV.AppStart()
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=