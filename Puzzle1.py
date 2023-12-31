import i2clcd

class Puzzle1: 

  def __init__(self):
    self.lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=20)
    self.lcd.init()

  def Leer(self): #Devuelve un String que contiene entre 0 y 80 caracteres
    texto = input("Por favor ingrese un String: ")
    while(len(texto)>80):
      print("Has puesto más caracteres de los que se puede, ingrese otro String")
      texto = input("Por favor ingrese otro String: ")
    return texto

  def Imprimir(self, text):
    aux=0
    linea=1 #irá del 1 al 4, pero habrá que restarle 1 para usarlo (otherwise habría que sumarle 1)
    while(aux!=len(text)):
      if len(text)-aux>20:
        self.lcd.print_line(text[aux:(linea*20)], linea-1, 'CENTER')
        aux=aux+20
        linea=linea+1
      else:
        self.lcd.print_line(text[aux:len(text)], linea-1, 'CENTER')
        aux=len(text)
        linea=linea+1

  def Main(self):
    self.__init__()
    txt= self.Leer()
    self.Imprimir(txt)

mi_instancia = Puzzle1()
mi_instancia.Main()
