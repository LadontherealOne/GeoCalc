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
def add_point():
    #get all entrys
    pkt_nr = w.koordinaten_tabelle1_pktnr_entry.text()
    pkt_rechts = w.koordinaten_tabelle1_rewert_entry.text()
    pkt_hoch = w.koordinaten_tabelle1_hwert_entry.text()
    pkt_hoehe = w.koordinaten_tabelle1_hoehe_entry.text()
    #test if all entrys are valid
    if pkt_nr == "":
        w.koordinaten_tabelle1_return_label.setText("Punktnummer eingeben!")
    elif pkt_rechts == "":
        w.koordinaten_tabelle1_return_label.setText("Rechtswert eingeben!")
    elif pkt_hoch == "":
        w.koordinaten_tabelle1_return_label.setText("Hochwert eingeben!")
    else: #mindestanzahl an feldern ausgefüllt
        try: #test if entrys are valid types
            float(pkt_rechts)
            float(pkt_hoch)
            print(pkt_hoehe)
            if pkt_hoehe != "":
                float(pkt_hoehe)
        except: #eingabe fehlerhaft
            w.koordinaten_tabelle1_return_label.setText("Eingabe überprüfen!")
            return
        # eingabe korrekt
        # add a new row
        row_count = w.koordinaten_tabelle1_pktliste_table.rowCount()
        w.koordinaten_tabelle1_pktliste_table.insertRow(row_count)
        #set all items of the row
        w.koordinaten_tabelle1_pktliste_table.setItem(row_count, 0, QTableWidgetItem(pkt_nr))
        w.koordinaten_tabelle1_pktliste_table.setItem(row_count, 1, QTableWidgetItem(pkt_rechts))
        w.koordinaten_tabelle1_pktliste_table.setItem(row_count, 2, QTableWidgetItem(pkt_hoch))
        w.koordinaten_tabelle1_pktliste_table.setItem(row_count, 3, QTableWidgetItem(pkt_hoehe))



w.koordinaten_tabelle1_pkthinzufuegen_button.clicked.connect(add_point)

w.show()
sys.exit(app.exec_())