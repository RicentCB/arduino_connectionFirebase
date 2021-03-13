
# def calcularAreaRectangulo(base, altura):
#     return base * altura

# def calcularPerimetroRectangulo(base, altura):
#     return (2 * base + 2 * altura)


# var1 = 5
# var2 = 10
# resultado = calcularAreaRectangulo(var1, var2)

# var3 = 15
# var4 = 3
base = 10
# resultado = calcularAreaRectangulo(var3, var4)
# resultado = calcularPerimetroRectangulo(var3, var1)
base = base / 5
# print(resultado)

class Rectangulo():
    # base    : float
    # altura  : float
    def __init__(self, base, altura, nombreUnico = "NOMBREDEFAULT"):
        self.base = base
        self.altura = altura
        self.nombreUnico = nombreUnico
        self.area = base * altura

    def calcularAreaRectangulo(self):
        print("El area del "+self.nombreUnico+" es: ")
        return self.base * self.altura

    def calcularPerimetroRectangulo(self):
        print("El perimetro del "+self.nombreUnico+" es: ")
        return (2 * self.base + 2 * self.altura)
    
    def nuevoValorBase(self, nuevaBase = 100):
        self.base = nuevaBase
    
    def nuevoValorAltura(self, nuevaAltura):
        self.altura = nuevaAltura


# Rectangulo1 = Rectangulo(10,5,"Rectangulo1")
# area1 = Rectangulo1.calcularAreaRectangulo()


Rectangulo2 = Rectangulo(100,2,"Rectangulo2")
Rectangulo1 = Rectangulo(10,5, "Rect1");
print(Rectangulo2.calcularAreaRectangulo())
print(Rectangulo1.calcularAreaRectangulo())

# print(Rectangulo2.calcularPerimetroRectangulo())

# Rectangulo2.nuevoValorBase(5)

# print(Rectangulo2.calcularPerimetroRectangulo())
# print(Rectangulo2.calcularAreaRectangulo())


# print(Rectangulo2.calcularPerimetroRectangulo())



