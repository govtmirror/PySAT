from PyQt4 import QtCore, QtGui
from pysat.utils.gui_utils import make_combobox
from PYSAT_UI_MODULES.Error_ import error_print

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class strat_folds_:
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.stratified_folds()

    def stratified_folds(self):
        self.pysat_fun.fun_list.append(self.pysat_fun.do_strat_folds)
        self.strat_folds = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.strat_folds.setFont(font)
        self.strat_folds.setObjectName(_fromUtf8("Stratified Folds"))
        self.strat_folds_vlayout = QtGui.QVBoxLayout(self.strat_folds)
        self.strat_folds_vlayout.setObjectName(_fromUtf8("strat_folds_vlayout"))
        self.strat_folds_choose_data_label = QtGui.QLabel(self.strat_folds)
        self.strat_folds_choose_data_label.setObjectName(_fromUtf8("strat_folds_choose_data_label"))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data_label)
        datachoices=self.pysat_fun.datakeys
        if datachoices==[]:
            error_print('No data has been loaded!')
            datachoices=['No data has been loaded!']
        self.strat_folds_choose_data=make_combobox(datachoices)
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data)
        self.strat_folds_choose_var_label = QtGui.QLabel(self.strat_folds)
        self.strat_folds_choose_var_label.setObjectName(_fromUtf8("strat_folds_choose_var_label"))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_var_label)
        varchoices=self.pysat_fun.data[self.strat_folds_choose_data.currentText()].df['meta'].columns.values
        self.strat_folds_choose_var=make_combobox(varchoices)
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_var)
        self.strat_folds_choose_data.activated[int].connect(self.strat_fold_change_vars)
        self.strat_folds_hlayout = QtGui.QHBoxLayout()
        self.strat_folds_hlayout.setObjectName(_fromUtf8("strat_folds_hlayout"))
        self.nfolds_label = QtGui.QLabel(self.strat_folds)
        self.nfolds_label.setObjectName(_fromUtf8("nfolds_label"))
        self.strat_folds_hlayout.addWidget(self.nfolds_label)
        self.nfolds_spin = QtGui.QSpinBox(self.strat_folds)
        self.nfolds_spin.setObjectName(_fromUtf8("nfolds_spin"))
        self.nfolds_spin.setMinimum(1)
        self.strat_folds_hlayout.addWidget(self.nfolds_spin)
        self.test_fold_label = QtGui.QLabel(self.strat_folds)
        self.test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        self.test_fold_label = QtGui.QLabel(self.strat_folds_gbox)
        self.test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        foldchoices=['1']
        self.choose_test_fold = make_combobox(foldchoices)
        self.choose_test_fold.setObjectName(_fromUtf8("choose_test_fold"))
        self.nfolds_spin.valueChanged.connect(self.strat_fold_change_testfolds)
        self.strat_folds_hlayout.addWidget(self.choose_test_fold)
        self.spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.strat_folds_hlayout.addItem(self.spacerItem)
        self.create_folds = QtGui.QPushButton(self.strat_folds)
        self.create_folds.setObjectName(_fromUtf8("create_folds"))
        self.create_folds.setText(_translate("strat_folds", "Create Folds", None))
        self.strat_folds_hlayout.addWidget(self.create_folds)
        self.strat_folds_vlayout.addLayout(self.strat_folds_hlayout)
        self.verticalLayout_8.addWidget(self.strat_folds)
        self.strat_folds.raise_()
        self.strat_folds.setTitle(_translate("MainWindow", "Stratified Folds", None))
        self.nfolds_label.setText(_translate("strat_folds", "N folds", None))
        self.test_fold_label.setText(_translate("strat_folds", "Test Fold", None))
        self.create_folds.setText(_translate("strat_folds", "Create Folds", None))
        self.strat_folds_choose_data_label.setText(_translate("strat_folds", "Choose data to stratify:", None))
        self.strat_folds_choose_var_label.setText(_translate("strat_folds", "Choose variable on which to sort:", None))
        try:
            # arg_list.append(['known data', 5, 2, ('meta', 'SiO2')])
            self.create_folds.clicked.connect(lambda: self.pysat_fun.arg_list.append([known_data, 5, 2, ('meta', 'SiO2')]))
        except:
            print('There was a problem with creating stratified folds...')

    def strat_fold_change_vars(self):
        self.strat_folds_choose_var.clear()
        choices = self.pysat_fun.data[self.strat_folds_choose_data.currentText()].df['meta'].columns.values
        print(choices)
        self.strat_folds_choose_var.addItems(choices)

    def strat_fold_change_testfolds(self):
        self.choose_test_fold.clear()
        choices = list(map(str, list(range(1, self.nfolds_spin.value() + 1))))
        print(choices)
        self.choose_test_fold.addItems(choices)

