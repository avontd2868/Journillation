#!/usr/bin/env python2
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
 iscVJournalEntry = ""
 iscVJournalQ1 = "What did I have for breakfast today?"
 iscVJournalA1 = ""
 iscVJournalFile = "changeme.mkd"
 iscVDate = ""
 iscVmdH1begin = "# "
 iscVmdH1end = " #\n\n"
 iscVFinalState = ""
 iscVmdH2 = "\n\n## "
 iscVmdH2end = " ##\n"
 iscVQuitAfter = 0
 iscVTrue = 1
 iscWindow2Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow2Window1Fixed = gtk.Fixed()
 iscWindow2DateBox0 = gtk.Entry()
 iscWindow2Label0 =gtk.Label("Date")
 iscWindow2Finish0 = gtk.Button("Finish")
 iscWindow2Save0 = gtk.Button("Save")
 iscWindow2Button20 = gtk.Button("Cancel")
 iscWindow2MainEntry0 = gtk.TextView(buffer=None)
 iscWindow2ATextField10 = gtk.TextView(buffer=None)
 iscWindow2QTextBox0 = gtk.Entry()
 iscWindow2Title0 =gtk.Label("Journillation 1.0")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()

#EndOfClass

def iscConfirmationDialog1():
 message = "Are you sure you want to quit?\n\n(you will loose any unsaved work)"
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, message)
 response = dialog.run()
 dialog.destroy()
 if response == gtk.RESPONSE_YES:
  iscAppQuit4()
  #iscConfirmationDialog1Yes
  return False
 else:
  #iscConfirmationDialog1No
  return True

def iscWindow2():
 thisiscApp1.iscWindow2DateBox0 = gtk.Entry()
 thisiscApp1.iscWindow2Label0 =gtk.Label("Date")
 thisiscApp1.iscWindow2Finish0 = gtk.Button("Finish")
 thisiscApp1.iscWindow2Save0 = gtk.Button("Save")
 thisiscApp1.iscWindow2Button20 = gtk.Button("Cancel")
 thisiscApp1.iscWindow2MainEntry0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow2MainEntry0.set_wrap_mode(gtk.WRAP_WORD) # I put this line in
 thisiscApp1.iscWindow2ATextField10 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow2QTextBox0 = gtk.Entry()
 thisiscApp1.iscWindow2Title0 =gtk.Label("Journillation 1.0")
 thisiscApp1.iscWindow2Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow2Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow2Window1.set_title("Journillation")
 thisiscApp1.iscWindow2Window1.set_default_size(337, 416)
 thisiscApp1.iscWindow2Window1.add(thisiscApp1.iscWindow2Window1Fixed)
 thisiscApp1.iscWindow2Window1Fixed.width = 337
 thisiscApp1.iscWindow2Window1Fixed.height = 416
 thisiscApp1.iscWindow2Window1.connect("delete_event", iscWindow2Closed)
 thisiscApp1.iscWindow2Window1Fixed.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2DateBox0, 203, 22)
 thisiscApp1.iscWindow2DateBox0.set_text("")
 thisiscApp1.iscWindow2DateBox0.set_size_request(80, 22)
 thisiscApp1.iscWindow2DateBox0.connect("changed", iscWindow2DateBoxChanged)
 thisiscApp1.iscWindow2DateBox0.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2Label0, 156, 28)
 thisiscApp1.iscWindow2Label0.set_size_request(40, 12)
 thisiscApp1.iscWindow2Label0.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2Finish0, 34, 347)
 thisiscApp1.iscWindow2Finish0.set_size_request(80, 26)
 thisiscApp1.iscWindow2Finish0.connect("clicked", iscWindow2FinishClicked)
 thisiscApp1.iscWindow2Finish0.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2Save0, 129, 349)
 thisiscApp1.iscWindow2Save0.set_size_request(80, 26)
 thisiscApp1.iscWindow2Save0.connect("clicked", iscWindow2SaveClicked)
 thisiscApp1.iscWindow2Save0.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2Button20, 221, 348)
 thisiscApp1.iscWindow2Button20.set_size_request(80, 26)
 thisiscApp1.iscWindow2Button20.connect("clicked", iscWindow2Button2Clicked)
 thisiscApp1.iscWindow2Button20.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2MainEntry0, 39, 59)
 thisiscApp1.iscWindow2MainEntry0.set_size_request(270, 180)
 thisiscApp1.iscWindow2MainEntry0.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2ATextField10, 40, 282)
 thisiscApp1.iscWindow2ATextField10.set_size_request(270, 45)
 thisiscApp1.iscWindow2ATextField10.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2QTextBox0, 40, 250)
 thisiscApp1.iscWindow2QTextBox0.set_text("What did I have for breakfast today?")
 thisiscApp1.iscWindow2QTextBox0.set_size_request(270, 22)
 thisiscApp1.iscWindow2QTextBox0.connect("changed", iscWindow2QTextBoxChanged)
 thisiscApp1.iscWindow2QTextBox0.show()
 thisiscApp1.iscWindow2Window1Fixed.put(thisiscApp1.iscWindow2Title0, 40, 23)
 thisiscApp1.iscWindow2Title0.set_size_request(107, 19)
 thisiscApp1.iscWindow2Title0.show()
 thisiscApp1.iscWindow2Window1.show()
 #iscWindow2Opened
 #iscWindow2Done


def iscWindow2Closed(self, other):
 pass
 iscAppQuit4()
 #iscWindow2Closed


def iscWindow2DateBoxChanged(self):
 pass
 iscGetTextBox14()
 #iscWindow2DateBoxChanged


def iscWindow2FinishClicked(self):
 pass
 iscSetNumber15()
 #iscWindow2FinishClicked


def iscWindow2SaveClicked(self):
 pass
 iscGetTextField16()
 #iscWindow2SaveClicked


def iscWindow2Button2Clicked(self):
 pass
 iscConfirmationDialog1()
 #iscWindow2Button2Clicked


def iscWindow2QTextBoxChanged(self):
 pass
 iscGetTextBox13()
 #iscWindow2QTextBoxChanged


def iscAppQuit4():
 thisiscApp1.destroy(None,None)
 #iscAppQuit4Done


def iscCombineText5():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVmdH1begin + thisiscApp1.iscVDate
 iscCombineText6()
 #iscCombineText5Done


def iscCombineText6():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVmdH1end
 iscCombineText7()
 #iscCombineText6Done


def iscCombineText7():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVJournalEntry
 iscCombineText8()
 #iscCombineText7Done


def iscCombineText8():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVmdH2
 iscCombineText9()
 #iscCombineText8Done


def iscCombineText9():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVJournalQ1
 iscCombineText10()
 #iscCombineText9Done


def iscCombineText10():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVmdH2end
 iscCombineText11()
 #iscCombineText10Done


def iscCombineText11():
 thisiscApp1.iscVFinalState = thisiscApp1.iscVFinalState + thisiscApp1.iscVJournalA1
 iscSaveTextFileDialog18()
 #iscCombineText11Done


def iscIfThen12():
 if thisiscApp1.iscVQuitAfter == thisiscApp1.iscVTrue:
  iscAppQuit4()
  #iscIfThen12True

  pass
 else:
  #iscIfThen12False

  pass

def iscGetTextBox13():
 thisiscApp1.iscVJournalQ1 = thisiscApp1.iscWindow2QTextBox0.get_text()
 #iscGetTextBox13Done


def iscGetTextBox14():
 thisiscApp1.iscVDate = thisiscApp1.iscWindow2DateBox0.get_text()
 #iscGetTextBox14Done


def iscSetNumber15():
 thisiscApp1.iscVQuitAfter = thisiscApp1.iscVTrue
 iscGetTextField16()
 #iscSetNumber15Done


def iscGetTextField16():
 thisiscApp1.iscVJournalEntry = thisiscApp1.iscWindow2MainEntry0.get_buffer().get_text(thisiscApp1.iscWindow2MainEntry0.get_buffer().get_start_iter(), thisiscApp1.iscWindow2MainEntry0.get_buffer().get_end_iter())
 iscGetTextField17()
 #iscGetTextField16Done


def iscGetTextField17():
 thisiscApp1.iscVJournalA1 = thisiscApp1.iscWindow2ATextField10.get_buffer().get_text(thisiscApp1.iscWindow2ATextField10.get_buffer().get_start_iter(), thisiscApp1.iscWindow2ATextField10.get_buffer().get_end_iter())
 iscCombineText5()
 #iscGetTextField17Done


def iscSaveTextFileDialog18():
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
  iscSaveAllTextToFile19()
  #iscSaveTextFileDialog18Done
  pass
 elif response == gtk.RESPONSE_CANCEL:
  #iscSaveTextFileDialog18Cancelled
  pass

 dialog.destroy()

def iscSaveAllTextToFile19():
 f = open(thisiscApp1.iscVJournalFile, 'w')
 f.write(thisiscApp1.iscVFinalState)
 f.close()
 iscIfThen12()
 #iscSaveAllTextToFile19Done


#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow2()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()
