# -*- coding: utf-8 -*-
''' 
This module is a header-like file for pyqtconfig. Handles compatiblity
with both PyQt5 and PySide2.
'''
import sys

if "PyQt5" in sys.modules:
    from PyQt5.QtCore import (QVariant, Qt, QMutex, QMutexLocker, QSettings,
                              QObject, pyqtSignal)
    from PyQt5.QtWidgets import (QComboBox, QCheckBox, QAction,
                                 QActionGroup, QPushButton, QSpinBox,
                                 QDoubleSpinBox, QPlainTextEdit, QLineEdit,
                                 QListWidget, QSlider, QButtonGroup,
                                 QTabWidget, QApplication, QGridLayout,
                                 QTextEdit, QWidget, QMainWindow)
    from PyQt5 import QtWidgets

    Signal = pyqtSignal

elif "PySide2" in sys.modules:
    from PySide2.QtWidgets import (QComboBox, QCheckBox, QAction, QMainWindow,
                              QActionGroup, QPushButton, QSpinBox,
                              QDoubleSpinBox, QPlainTextEdit, QLineEdit,
                              QListWidget, QSlider, QButtonGroup, QWidget,
                              QTabWidget, QApplication, QGridLayout, QTextEdit)
    from PySide2.QtCore import (Signal, Qt, QMutex, QMutexLocker, QSettings,
                               QObject)

    from PySide2 import QtWidgets
    
    QVariant = None



