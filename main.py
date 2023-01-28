import math

def ploRect(a, b):
    return (a * b)      #площадь четырехугольника

def perRect(a,b):
    return 2 * (a + b) # периметр прямоугольника

def ploTriangl(a, b, c):    # S треугольника по 3 сторонам
    p = (a + b + c) / 2
    plo = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    return plo

def perTriangle(a, b, c):
    return a + b + c       #периметр треугольника

def ploTriangl2(a, h):      # S треугольника по высоте и стороне
    return a*h * 0.5

def ploParall(a,h):
    return a * h    #площадь параллелограмма через сторону и высоту

def ploRomb(a,b):
    return a*b*0.5      #площадь ромба

def ploCircle(r):
    return round(math.pi * (r**2), 2)     #площадь круга

def perCircle(r):
    return round(2 * r * math.pi, 2)      #периметр круга

def ploTrap(a, b, h):
    return ((a + b) / 2) * h    #площадь трапеции

def ploCilinder(r,h):
    return round(math.pi * (r**2) * h, 2)     #объем циилиндра

def ploPara(a,b,c):
    return a*b*c    #Площадь параллелепипеда

def ploSphere(r):
    return round((4/3) * (r**3) * math.pi, 2)   #площадь Сферы

