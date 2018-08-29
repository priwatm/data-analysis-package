# -*- coding: utf-8 -*-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
___DESCRIPTION________________________________________________________________
- The module with class for output text information.
'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#      The package that provide classes for working with Qt library:
from   PyQt4        import QtGui, QtCore
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class console():
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __init__(self,Verb=1):
        '''
        ___DESCRIPTION________________________________________________________
        Init parameters.
        '''
        self.Verb  = Verb
        self.Msg   = dict.fromkeys(['Module','Function','Text','FullText','Type'],None)
        self.Tedt  = None
        self.Wgt   = None
        self.Color = "<font color=\"grey\">"
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def SetGuiTedt(self,Tedt):
        self.Tedt = Tedt
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def SetGuiWgt(self,Wgt):
        self.Wgt  = Wgt
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def msg(self,Obj,Text,Type):
        self.Msg['Module']   = Obj['Module']
        self.Msg['Function'] = Obj['Function']
        self.Msg['Type']     = Type
        self.Msg['Text']     = Text
        if self.Msg['Type']=='E':
            self.Msg['FullText'] = "<font color=\"red\">"
            self.Msg['FullText']+= 'Error______'
        if self.Msg['Type']=='W':
            self.Msg['FullText'] = "<font color=\"red\">"
            self.Msg['FullText']+= 'Warning____'
        if self.Msg['Type']=='R':
            self.Msg['FullText'] = "<font color=\"blue\">"
            self.Msg['FullText']+= '----->_____'
        if self.Msg['Type']=='P':
            self.Msg['FullText'] = "<font color=\"green\">"
            self.Msg['FullText']+= '......_____'
        self.Msg['FullText'] += '%80s'%self.Msg['Text']
        self.Msg['FullText'] += ' ___from:  '
        self.Msg['FullText'] += self.Msg['Module']
        self.Msg['FullText'] += '.'+self.Msg['Function']+'()'
        self.Msg['FullText'] += "</font><br>"
        self.send()
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def send(self):
        if self.Msg['Type']=='E' and self.Verb<0:
            return
        if self.Msg['Type']=='W' and self.Verb<1:
            return 
        if self.Msg['Type']=='R' and self.Verb<2:
            return
        if self.Msg['Type']=='P' and self.Verb<3:
            return
        #print self.Msg['FullText']
        if self.Tedt != None:
            self.Tedt.insertHtml(self.Msg['FullText'])
        if self.Wgt == None:
            return
        if self.Msg['Type']=='E':
            Prefix = 'Error in '
        elif self.Msg['Type']=='W':
            Prefix = 'Warning in '
        else:
            return
        Dialog = QtGui.QDialog(self.Wgt,QtCore.Qt.Window) 
        Dialog.setWindowTitle(Prefix+self.Msg['Module']+'.'+self.Msg['Function']+'()')
        Dialog.setMinimumWidth(300)
        Lbl_mess = QtGui.QLabel(self.Msg['Text'])
        Btn_hide = QtGui.QPushButton('OK')
        Btn_hide.clicked.connect(Dialog.close) 
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(Lbl_mess)
        vbox.addWidget(Btn_hide)
        Dialog.setLayout(vbox)
        Dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.MSWindowsFixedSizeDialogHint) 
        Dialog.exec_() # Показать окно
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        
        
        
        
        
        
        