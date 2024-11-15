import math

def areaTriangulo(base: float, altura: float) -> float:
    area = base*altura/2
    return area

def areaRectangulo(base: float, altura: float) -> float:
    area = base * altura
    return area

def areaCirculo(radio: float) -> float:
    area = math.pi * radio * radio
    return area

'''
    Y así hasta tener todas las figuras geométrica que queramos
'''
