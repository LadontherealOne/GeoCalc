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

import numpy as np

pkt_list = []

app = QApplication(sys.argv)
w = loadUi("Test2.ui")


def add_point():
    # get all entrys
    pkt_nr = w.koordinaten_tabelle1_pktnr_entry.text()
    pkt_rechts = w.koordinaten_tabelle1_rewert_entry.text()
    pkt_hoch = w.koordinaten_tabelle1_hwert_entry.text()
    pkt_hoehe = w.koordinaten_tabelle1_hoehe_entry.text()
    # test if all entrys are valid
    if pkt_nr == "":
        w.koordinaten_tabelle1_return_label.setText("Punktnummer eingeben!")
    elif pkt_rechts == "":
        w.koordinaten_tabelle1_return_label.setText("Rechtswert eingeben!")
    elif pkt_hoch == "":
        w.koordinaten_tabelle1_return_label.setText("Hochwert eingeben!")
    else:  # mindestanzahl an feldern ausgefüllt
        try:  # test if entrys are valid types
            float(pkt_rechts)
            float(pkt_hoch)
            print(pkt_hoehe)
            if pkt_hoehe != "":
                float(pkt_hoehe)
        except type:  # eingabe fehlerhaft
            w.koordinaten_tabelle1_return_label.setText("Eingabe überprüfen!")
            return
        # eingabe korrekt
        # add a new row
        row_count = w.koordinaten_tabelle1_pktliste_table.rowCount()
        w.koordinaten_tabelle1_pktliste_table.insertRow(row_count)
        # set all items of the row
        w.koordinaten_tabelle1_pktliste_table.setItem(row_count, 0, QTableWidgetItem(pkt_nr))
        w.koordinaten_tabelle1_pktliste_table.setItem(row_count, 1, QTableWidgetItem(pkt_rechts))
        w.koordinaten_tabelle1_pktliste_table.setItem(row_count, 2, QTableWidgetItem(pkt_hoch))
        w.koordinaten_tabelle1_pktliste_table.setItem(row_count, 3, QTableWidgetItem(pkt_hoehe))


def add_tab():  # adds a new (empty :/) tab with incrementet name
    index = w.koordinaten_tabWidget.currentIndex()  # gets index of current selected tab
    count = w.koordinaten_tabWidget.count()  # counts all existing tabs
    if index == count-1:  # checks if current selected tab is the "add_tab"
        w.koordinaten_tabWidget.insertTab(count-1, QWidget(), "KT "+str(count))  # insert a new tab in the last-1 slot
        w.koordinaten_tabWidget.setCurrentIndex(count-1)  # swap to the new added tab
        

def show_point():   #shows the coordinates from table1
    if w.grafik_grafik_graphicsview.scene() is None: # sets the scene in which the coordinates are displayed
        scene = QGraphicsScene()
        w.grafik_grafik_graphicsview.setScene(scene)
    else:
        scene = w.grafik_grafik_graphicsview.scene()
        scene.clear()
    # getting the screen height to scale the points to 1% of it
    screen_height = QApplication.desktop().screenGeometry().height()
    pkt_size = screen_height/100
    for row in range(w.koordinaten_tabelle1_pktliste_table.rowCount()): # collects all values for x and y; displays them as an ellipse 
        hoch_i = w.koordinaten_tabelle1_pktliste_table.item(row,1)
        rechts_i = w.koordinaten_tabelle1_pktliste_table.item(row,2)
        if hoch_i is not None and rechts_i is not None:
            hoch = float(hoch_i.text())
            rechts = float(rechts_i.text())
            pkt = scene.addEllipse(-hoch,rechts,pkt_size,pkt_size, brush=Qt.black)
            pkt_list.append(pkt)


def clear_graph(): # clears the graph
    scene = w.grafik_grafik_graphicsview.scene()
    scene.clear()
   
    
def zoom_in():  # zooms in in the graph
    zoom_faktor = 2
    w.grafik_grafik_graphicsview.scale(zoom_faktor,zoom_faktor)
    
    for pkt in pkt_list:
        pkt_size= pkt.rect()
        radius = pkt_size.width()
        new_radius = radius*0.5
        add_radius = -(radius-new_radius)
        pkt_size.adjust(0,0,add_radius,add_radius)
        pkt.setRect(pkt_size)


    
def zoom_out():  # zooms out of the graph
    zoom_faktor = 0.5
    w.grafik_grafik_graphicsview.scale(zoom_faktor,zoom_faktor)
    
    for i,pkt in enumerate(pkt_list):
        pkt_size= pkt.rect()
        radius = pkt_size.width()
        new_radius = radius*2
        add_radius = -(radius-new_radius)
        pkt_size.adjust(0,0,add_radius,add_radius)
        pkt.setRect(pkt_size)


def export_csv(): # exports the coordinates from kt1 as comma seperated values into the text field
    pkt = []
    for row in range(w.koordinaten_tabelle1_pktliste_table.rowCount()): # collects all values for pktnr, x, y an z
        pktnr = w.koordinaten_tabelle1_pktliste_table.item(row,0).text()
        hoch = w.koordinaten_tabelle1_pktliste_table.item(row,1).text()
        rechts = w.koordinaten_tabelle1_pktliste_table.item(row,2).text()
        höhe = w.koordinaten_tabelle1_pktliste_table.item(row,3).text()
        if hoch is not None and rechts is not None:                     # appends the text field 
            w.export_export_plaintxtedit.appendPlainText(f'{pktnr},{hoch},{rechts},{höhe}')


w.koordinaten_tabelle1_pkthinzufuegen_button.clicked.connect(add_point)
w.koordinaten_tabWidget.currentChanged.connect(add_tab)
w.grafik_anzeigen_button.clicked.connect(show_point)
w.grafik_clear_button.clicked.connect(clear_graph)
w.grafik_grafik_graphicsview.setDragMode(QGraphicsView.ScrollHandDrag)
w.export_csv_button.clicked.connect(export_csv)
w.grafik_plus_button.clicked.connect(zoom_in)
w.grafik_minus_button.clicked.connect(zoom_out)

w.show()
sys.exit(app.exec_())
