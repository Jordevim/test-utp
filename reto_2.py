from calculadora import calculadoraRectangulo
from typing import Dict


def calcularSerie(nombre:str,peso:float,altura:float):
    imc = round(peso/(altura*altura),1)
    nombreb = nombre.upper()
    if imc < 18.5:
        valoracion = 'principiantes'
        valor = 150000
    if imc >= 30:
        valoracion = 'principiantes'
        valor = 150000
    if imc <=29.9 and imc >= 25:
        valoracion = 'intermedio'
        valor = 170000
    if imc <= 24.9 and imc >=18.5:
        valoracion = 'plus'
        valor = 200000
            
    usuario = {'nombre':nombreb,'peso':peso,'altura':altura,'imc':str(imc),'programa':valoracion,'valor':valor} 
    print(usuario)

print(calcularSerie('MIguel AnGel',53.6,1.78))


