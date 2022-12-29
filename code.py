from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import datetime




import sys

from PySide6.QtUiTools import loadUiType

MainUI, _ = loadUiType("./main.ui")


class MainApp(QMainWindow, MainUI):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon('age.ico'))
        self.handel_buttons()
    
    
    
    def handel_buttons(self):
       self.pushButton.clicked.connect(self.find_age)
       
    
    
    def first_action(self):
        date = self.second.date()
        
        self.first.setMaximumDate(date)
        
    
    def second_action (self):
        
        date = self.first.date()
        
        self.second.setMaximumDate(date)
        
        
       
        
        
    def find_age(self):
      
        # get the first age
        get_Qdate1 = self.first.date()
        birth_year = get_Qdate1.year()
        birth_month = get_Qdate1.month()
        birth_day = get_Qdate1.day()
  
        # get the second age
        get_Qdate2 = self.second.date()
        given_year = get_Qdate2.year()
        given_month = get_Qdate2.month()
        given_day = get_Qdate2.day()
        
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        
        
        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

        # if birth month exceeds given month, then
        # donot count this year and add 12 to the
        # month so that we can subtract and find out
        # the difference
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12
  
        # calculate day, month, year
        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year
  
        # setting text to the result
        self.result.setText(str(calculated_day) + " Day(s), " + str(calculated_month)
                            + " Month(s), " + str(calculated_year) + " Year(s)")
        
       
        
    
    
    
def main():
    app = QApplication()
    window = MainApp()
    window.show()
    app.exec()


if "__main__" == __name__:
    main()        






