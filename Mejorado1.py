import i2clcd

class Mejorado1: 

  def __init__(self):
    self.lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=20)
    self.lcd.init()

  def Leer(self): #Devuelve un String que contiene entre 0 y 80 caracteres
    texto = input("Por favor ingrese un String: ") 
    newtxt = self.MaxCar(texto)    
    return newtxt

  def Imprimir(self, text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
      self.lcd.print_line(line, i, 'CENTER')

  def MaxCar(self, text):
    while len(text) > 80:
      print("Has puesto más caracteres de los que se puede, ingrese otro String")
      text = input("Por favor ingrese otro String: ")
    return text
        
  def Main(self):
    self.__init__()
    txt= self.Leer()
    self.Imprimir(txt)

mi_instancia = Mejorado1()  #Cuando esté en el Puzzle2, estás 2 lineas van comentadas para que no se ejecuten automaticamente 
mi_instancia.Main()
