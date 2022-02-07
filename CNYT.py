import math

def Suma(a,b):
    real=a[0]+b[0]
    imag=a[1]+b[1]
    return(real,imag)

def Producto(a,b):
    producent=(a[0]*b[0]+(a[1]*b[1])*-1)
    producima=(a[0]*b[1]+a[1]*b[0])
    return (producent,producima)
def Resta(a,b):
    realr=a[0]-b[0]
    imagr=a[1]-b[1]
    return(realr,imagr)

def Division(a,b):
    nb=Conjugado(b)
    numerador=Producto(a,nb)
    denominador=Producto(b,nb)
    return((numerador[0]/denominador[0]),(numerador[1]/denominador[0]))
def Modulo(a):
    mod=math.sqrt((a[0]*a[0])+(a[1]*a[1]))
    return mod
def Conjugado(a):
    na=a[1]*-1
    return(a[0],na)
if __name__ == '__main__':
    print(Suma((3, 5), (-2.6, 6.8)))
