# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:54:57 2023

@author: Hauke
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *

app = QApplication(sys.argv)
w = loadUi("Test2.ui")

w.show()
sys.exit(app.exec_())