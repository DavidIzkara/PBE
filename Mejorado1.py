import i2clcd

class Mejorado1: 

  def __init__(self):
    self.lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=20)
    self.lcd.init()

  def Leer(self): 
    texto = input("Por favor ingrese un String: ")   
    return texto

def imprimir_lcd(texto, max_caracteres_por_linea):
    palabras = texto.split()
    lineas = ['']
    for palabra in palabras:
        if '\n' in palabra:
            partes = palabra.split('\n')
            for parte in partes:
                if len(lineas[-1] + parte) <= max_caracteres_por_linea:
                    lineas[-1] += parte + ' '
                else:
                    lineas.append(parte + ' ')
        elif len(lineas[-1] + palabra) <= max_caracteres_por_linea:
            lineas[-1] += palabra + ' '
        else:
            lineas.append(palabra + ' ')

    for i, line in enumerate(lineas):
       self.lcd.print_line(line.rstrip(), i, 'CENTER')

        
  def Main(self):
    self.__init__()
    txt= self.Leer()
    self.Imprimir(txt)

mi_instancia = Mejorado1()  #Cuando esté en el Puzzle2, estás 2 lineas van comentadas para que no se ejecuten automaticamente 
mi_instancia.Main()
