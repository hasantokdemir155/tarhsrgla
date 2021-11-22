import locale
from ssql import *
import pyodbc

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from syf2x import *



def ekle():
    print('mmmmmm')
    deg1=int(ui.comboBox.currentText())
    deg2=int(ui.comboBox_2.currentText())
    deg3=int(ui.comboBox_3.currentText())
    #kmt1=conn.cursor()
    kmtx=conn.cursor()
    #kmtx.execute('select * from Customers')
    print(deg1)
    deg=[deg1,deg2,deg3]
    print(deg)
    kmtx.execute('exec [tarin] @yl=?,@ayy=?,@gn=?' ,deg)
    print('ssssss')
    #print(kmtl)
    kaytlar=kmtx.fetchall()
    for i in kaytlar:
        print(i)

    

    #kaytlar=kmt1.fetchall()
    #kytx=kmtx.fetchall()

    for i in kaytlar:
        print(i[0])

    
    #print(ui.dateEdit.date().toString(QtCore.Qt.ISODate))

    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(('Tarih', 'Ad', 'Soyad', 'Şirket','Ödeme'))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  
   
    for i,strvr in enumerate(kaytlar):
                
            #print(locale.format_string("%.f", int(sutver),grouping=True))
          ui.tableWidget.setItem(i,0,QTableWidgetItem(str(strvr[2])+'-'+str(strvr[1])+'-'+str(strvr[0])))
          #ui.tableWidget.setItem(i,1,QTableWidgetItem(str(strvr[1])))                
          #ui.tableWidget.setItem(i,2,QTableWidgetItem(str(strvr[2])))
          ui.tableWidget.setItem(i,1,QTableWidgetItem(str(strvr[3])))
          ui.tableWidget.setItem(i,2,QTableWidgetItem(str(strvr[4])))
          ui.tableWidget.setItem(i,3,QTableWidgetItem(str(strvr[5])))
          ui.tableWidget.setItem(i,4,QTableWidgetItem(str(strvr[6])))
   
            
             
    

    
uyg=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show() 


conn = pyodbc.connect(
       "Driver={SQL Server Native Client 11.0};"
       "Server=HASAN\SQLEXPRESS1;"
       "Database=NORTHWND;"
       "Trusted_Connection=yes;"
    )

crs=conn.cursor()
locale.setlocale(locale.LC_ALL,"tr_TR.UTF-8")





kmt1=conn.cursor()
kmt1.execute('select year(OrderDate) From Orders  group by year(OrderDate)  order by year(OrderDate) asc')
kaytlar=kmt1.fetchall()

print(kaytlar)
m=0
for i in kaytlar:
    ui.comboBox.addItem(str(kaytlar[m][0]))
    m= m + 1

kmt1=conn.cursor()
kmt1.execute('select month(OrderDate) From Orders  group by month(OrderDate)  order by month(OrderDate) asc')  
#group by strftime('%m',bolum)")
kaytlar=kmt1.fetchall()

m=0
for i in kaytlar:
    ui.comboBox_2.addItem(str(kaytlar[m][0]))
    m= m + 1




kmt1=conn.cursor()
kmt1.execute('select day(OrderDate) From Orders  group by day(OrderDate)  order by day(OrderDate) asc')  
#group by strftime('%m',bolum)")
kaytlar=kmt1.fetchall()

m=0
for i in kaytlar:
    ui.comboBox_3.addItem(str(kaytlar[m][0]))
    m= m + 1







    
#for i in kaytlar:
#    print(i)
#    ui.comboBox.addItem(i)
  


ui.pushButton.clicked.connect(ekle)




sys.exit(uyg.exec_())
