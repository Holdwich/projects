import mysql.connector
import os

class SQL:
   def __init__(self, esquema):
       self.cnx = mysql.connector.connect(user=os.getenv(usuario), password=os.getenv(senha), host='127.0.0.1', database=esquema)

   def executar(self, comando, parametros):
       cs = self.cnx.cursor()
       cs.execute(comando, parametros)
       self.cnx.commit()
       cs.close()
       return True

   def consultar(self, comando, parametros):
       cs = self.cnx.cursor()
       cs.execute(comando, parametros)
       return cs

   def imprimir(self, comando, parametros, titulos):
       tab = PrettyTable(titulos)
       cs = self.cnx.cursor()
       cs.execute(comando, parametros)
       for reg in cs:
           tab.add_row(reg)
       print(tab)
       return cs

   def __del__(self):
       self.cnx.close()
