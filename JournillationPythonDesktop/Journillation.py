#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gobject
import random
import os
import sys
import gtk
#EndImports

class iscApp1:
 iscVTrue = 1
 iscVQuitAfter = 0
 iscVmdH2end = " ##\n"
 iscVmdH2 = "\n\n## "
 iscVFinalState = ""
 iscVmdH1end = " #\n\n"
 iscVmdH1begin = "# "
 iscVDate = ""
 iscVJournalFile = "changeme.mkd"
 iscVJournalA1 = ""
 iscVJournalQ1 = "What did I have for breakfast today?"
 iscVJournalEntry = ""
 iscWindow1Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow1Window1Fixed = gtk.Fixed()
 iscWindow1DateBox0 = gtk.Entry()
 iscWindow1Label0 =gtk.Label("Date")
 iscWindow1Finish0 = gtk.Button("Finish")
 iscWindow1Save0 = gtk.Button("Save")
 iscWindow1Button20 = gtk.Button("Cancel")
 iscWindow1MainEntry0 = gtk.TextView(buffer=None)
 iscWindow1ATextField10 = gtk.TextView(buffer=None)
 iscWindow1QTextBox0 = gtk.Entry()
 iscWindow1Title0 =gtk.Label("Journillation 1.0")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()

#EndOfClass

def iscWindow1():
 thisiscApp1.iscWindow1DateBox0 = gtk.Entry()
 thisiscApp1.iscWindow1Label0 =gtk.Label("Date")
 thisiscApp1.iscWindow1Finish0 = gtk.Button("Finish")
 thisiscApp1.iscWindow1Save0 = gtk.Button("Save")
 thisiscApp1.iscWindow1Button20 = gtk.Button("Cancel")
 thisiscApp1.iscWindow1MainEntry0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow1ATextField10 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow1QTextBox0 = gtk.Entry()
 thisiscApp1.iscWindow1Title0 =gtk.Label("Journillation 1.0")
 thisiscApp1.iscWindow1Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow1Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow1Window1.set_title("Journillation")
 thisiscApp1.iscWindow1Window1.set_default_size(337, 416)
 thisiscApp1.iscWindow1Window1.add(thisiscApp1.iscWindow1Window1Fixed)
 thisiscApp1.iscWindow1Window1Fixed.width = 337
 thisiscApp1.iscWindow1Window1Fixed.height = 416
 thisiscApp1.iscWindow1Window1.connect("delete_event", iscWindow1Closed)
 thisiscApp1.iscWindow1Window1Fixed.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1DateBox0, 203, 22)
 thisiscApp1.iscWindow1DateBox0.set_text("")
 thisiscApp1.iscWindow1DateBox0.set_size_request(80, 22)
 thisiscApp1.iscWindow1DateBox0.connect("changed", iscWindow1DateBoxChanged)
 thisiscApp1.iscWindow1DateBox0.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1Label0, 156, 28)
 thisiscApp1.iscWindow1Label0.set_size_request(40, 12)
 thisiscApp1.iscWindow1Label0.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1Finish0, 34, 347)
 thisiscApp1.iscWindow1Finish0.set_size_request(80, 26)
 thisiscApp1.iscWindow1Finish0.connect("clicked", iscWindow1FinishClicked)
 thisiscApp1.iscWindow1Finish0.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1Save0, 129, 349)
 thisiscApp1.iscWindow1Save0.set_size_request(80, 26)
 thisiscApp1.iscWindow1Save0.connect("clicked", iscWindow1SaveClicked)
 thisiscApp1.iscWindow1Save0.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1Button20, 221, 348)
 thisiscApp1.iscWindow1Button20.set_size_request(80, 26)
 thisiscApp1.iscWindow1Button20.connect("clicked", iscWindow1Button2Clicked)
 thisiscApp1.iscWindow1Button20.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1MainEntry0, 40, 59)
 thisiscApp1.iscWindow1MainEntry0.set_size_request(270, 180)
 thisiscApp1.iscWindow1MainEntry0.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1ATextField10, 40, 282)
 thisiscApp1.iscWindow1ATextField10.set_size_request(270, 45)
 thisiscApp1.iscWindow1ATextField10.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1QTextBox0, 40, 250)
 thisiscApp1.iscWindow1QTextBox0.set_text("What did I have for breakfast today?")
 thisiscApp1.iscWindow1QTextBox0.set_size_request(270, 22)
 thisiscApp1.iscWindow1QTextBox0.connect("changed", iscWindow1QTextBoxChanged)
 thisiscApp1.iscWindow1QTextBox0.show()
 thisiscApp1.iscWindow1Window1Fixed.put(thisiscApp1.iscWindow1Title0, 40, 23)
 thisiscApp1.iscWindow1Title0.set_size_request(107, 19)
 thisiscApp1.iscWindow1Title0.show()
 thisiscApp1.iscWindow1Window1.show()
 #iscWindow1Opened
 #iscWindow1Done


def iscWindow1Closed(self, other):
 pass
 iscAppQuit19()
 #iscWindow1Closed


def iscWindow1DateBoxChanged(self):
 pass
 iscGetTextBox9()
 #iscWindow1DateBoxChanged


def iscWindow1FinishClicked(self):
 pass
 iscSetNumber8()
 #iscWindow1FinishClicked


def iscWindow1SaveClicked(self):
 pass
 iscGetTextField7()
 #iscWindow1SaveClicked


def iscWindow1Button2Clicked(self):
 pass
 iscAppQuit19()
 #iscWindow1Button2Clicked


def iscWindow1QTextBoxChanged(self):
 pass
 iscGetTextBox10()
 #iscWindow1QTextBoxChanged


def iscSaveAllTextToFile4():
 f = open(thisiscApp1.iscVJournalFile, 'w')
 f.write(thisiscApp1.iscVFinalState)
 f.close()
 iscIfThen11()
 #iscSaveAllTextToFile4Done


def iscSaveTextFileDialog5():
 dialog = gtk.FileChooserDialog("Save..", None, gtk.FILE_CHOOSER_ACTION_SAVE,  (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE, gtk.RESPONSE_OK))
 dialog.set_default_response(gtk.RESPONSE_OK)
 dialog.set_current_name("untitled.txt")
 filter = gtk.FileFilter()
 filter.set_name("Text Files")
 filter.add_mime_type("text/plain")
 filter.add_pattern("*.txt")
 dialog.add_filter(filter)
 filter2 = gtk.FileFilter()
 filter2.set_name("All Files")
 filter2.add_mime_type("All Files")
 filter2.add_pattern("*.*")
 dialog.add_filter(filter2)
 response = dialog.run()
 if response == gtk.RESPONSE_OK:
  thisiscApp1.iscVJournalFile = dialog.get_filename()
  iscSaveAllTextToFile4()
  #iscSaveTextFileDialog5Done
  pass
 elif response == gtk.RESPONSE_CANCEL:
  #iscSaveTextFileDialog5Cancelled
  pass

 dialog.destroy()

def iscGetTextField6():
 thisiscApp1.iscVJournalA1 = thisiscApp1.iscWindow1ATextField10.get_buffer().get_text(thisiscApp1.iscWindow1ATextField10.get_buffer().get_start_iter(), thisiscApp1.iscWindow1ATextField10.get_buffer().get_end_iter())
 iscCombineText18()
 #iscGetTextField6Done


def iscGetTextField7():
 thisiscApp1.iscVJournalEntry = thisiscApp1.iscWindow1MainEntry0.get_buffer().get_text(thisiscApp1.iscWindow1MainEntry0.get_buffer().get_start_iter(), thisiscApp1.iscWindow1MainEntry0.get_buffer().get_end_iter())
 iscGetTextField6()
 #iscGetTextField7Done


def iscSetNumber8():
 thisiscApp1.iscVQuitAfter = thisiscApp1.iscVTrue
 iscGetTextField7()
 #iscSetNumber8Done


def iscGetTextBox9():
 thisiscApp1.iscVDate = thisiscApp1.iscWindow1DateBox0.get_text()
 #iscGetTextBox9Done


def iscGetTextBox10():
 thisiscApp1.iscVJournalQ1 = thisiscApp1.iscWindow1QTextBox0.get_text()
 #iscGetTextBox10Done


def iscIfThen11():
 if thisiscApp1.iscVQuitAfter == thisiscApp1.iscVTrue:
  iscAppQuit19()
  #iscIfThen11True

  pass
 else:
  #iscIfThen11False

  pass

def iscCombineText12():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVJournalA1
 iscSaveTextFileDialog5()
 #iscCombineText12Done


def iscCombineText13():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVmdH2end
 iscCombineText12()
 #iscCombineText13Done


def iscCombineText14():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVJournalQ1
 iscCombineText13()
 #iscCombineText14Done


def iscCombineText15():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVmdH2
 iscCombineText14()
 #iscCombineText15Done


def iscCombineText16():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVJournalEntry
 iscCombineText15()
 #iscCombineText16Done


def iscCombineText17():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVmdH1end
 iscCombineText16()
 #iscCombineText17Done


def iscCombineText18():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVmdH1begin + thisiscApp1.iscVDate
 iscCombineText17()
 #iscCombineText18Done


def iscAppQuit19():
 thisiscApp1.destroy(None,None)
 #iscAppQuit19Done


#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow1()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()