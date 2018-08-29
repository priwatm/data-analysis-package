# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with Main window class.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Module's import
#      The packages that provide classes for working with Qt library:
from   PyQt4        import QtGui
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class appMainWindow(QtGui.QMainWindow):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,UI):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters of the main window.
        '''
        self.UI  = UI
        QtGui.QMainWindow.__init__(self)     # Initialization of the parent class
        self.UI.setupUi(self)                # UI is associated with main window
        self.Set_AppSettings()               # Call of function 
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def Set_AppSettings(self):
        '''
        ___DESCRIPTION________________________________________________________
        (Inner function) Set additional application settings
        (that were not set in Qt designer).
        '''
        self.UI.RBtn_PropInR.setChecked(True)
        self.UI.RBtn_UsePC.setChecked(True)
        self.UI.RBtn_PC_dim.setChecked(True)
        self.UI.RBtn_ThirstRowNumber.clicked.connect(self.UI.LEdt_ThirstRowNumber.setEnabled)
        self.UI.RBtn_ThirstRowNumber.clicked.connect(self.UI.LEdt_ThirstRowNumber.setFocus)
        self.UI.RBtn_LastRowNumber.clicked.connect(self.UI.LEdt_LastRowNumber.setEnabled)
        self.UI.RBtn_LastRowNumber.clicked.connect(self.UI.LEdt_LastRowNumber.setFocus)
        self.UI.RBtn_ThirstColumnNumber.clicked.connect(self.UI.LEdt_ThirstColumnNumber.setEnabled)
        self.UI.RBtn_ThirstColumnNumber.clicked.connect(self.UI.LEdt_ThirstColumnNumber.setFocus)
        self.UI.RBtn_LastColumnNumber.clicked.connect(self.UI.LEdt_LastColumnNumber.setEnabled)
        self.UI.RBtn_LastColumnNumber.clicked.connect(self.UI.LEdt_LastColumnNumber.setFocus)
        self.UI.RBtn_SplitterMask.clicked.connect(self.UI.LEdt_SplitterMask.setEnabled)
        self.UI.RBtn_SplitterMask.clicked.connect(self.UI.LEdt_SplitterMask.setFocus)
        self.UI.Btn_Import_ChooseFile.clicked.connect(self.UI.Btn_Import.setFocus)
        self.UI.Btn_Import.clicked.connect(self.UI.Btn_PrepareDate.setFocus)
        
        self.UI.RBtn_PC_thr.clicked.connect(self.UI.LEdt_PC_thr.setEnabled)
        self.UI.RBtn_PC_thr.clicked.connect(self.UI.LEdt_PC_thr.setFocus)
        self.UI.RBtn_PC_thr.clicked.connect(self.UI.LEdt_PC_dim.clear)
        self.UI.RBtn_PC_thr.clicked.connect(self.UI.LEdt_PC_dim.setDisabled)

        self.UI.RBtn_PC_dim.clicked.connect(self.UI.LEdt_PC_dim.setEnabled) 
        self.UI.RBtn_PC_dim.clicked.connect(self.UI.LEdt_PC_dim.setFocus)
        self.UI.RBtn_PC_dim.clicked.connect(self.UI.LEdt_PC_thr.clear)
        self.UI.RBtn_PC_dim.clicked.connect(self.UI.LEdt_PC_thr.setDisabled)
        '''
        def Change_RBtn():
            if self.UI.RBtn_MultiGraphPlot_UsePC1.isChecked():
                self.UI.RBtn_MultiGraphPlot_UsePCred1.setChecked(False)
            if self.UI.RBtn_MultiGraphPlot_UsePCred1.isChecked():
                self.UI.RBtn_MultiGraphPlot_UsePC1.setChecked(False)
            if self.UI.RBtn_MultiGraphPlot_UsePC2.isChecked():
                self.UI.RBtn_MultiGraphPlot_UsePCred2.setChecked(False)
            if self.UI.RBtn_MultiGraphPlot_UsePCred2.isChecked():
                self.UI.RBtn_MultiGraphPlot_UsePC2.setChecked(False)
        self.UI.RBtn_MultiGraphPlot_UsePC1.clicked.connect   (Change_RBtn)
        self.UI.RBtn_MultiGraphPlot_UsePCred1.clicked.connect(Change_RBtn)
        self.UI.RBtn_MultiGraphPlot_UsePC2.clicked.connect   (Change_RBtn)
        self.UI.RBtn_MultiGraphPlot_UsePCred2.clicked.connect(Change_RBtn)
        '''
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        
        
        
        