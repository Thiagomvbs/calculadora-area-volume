import math

class CalculadoraDeArea():

    def area_quadrado(self, lado):
        return  math.pow(lado, 2)
        
    def area_retangulo(self, comprimento, largura):
        return  comprimento * largura

    def area_circulo(self, raio):
        return  math.pi * (math.pow(raio, 2))

    def area_triangulo(self, base, altura):
        return  (base * altura) / 2

    def area_trapezio(self, base_menor, base_maior, altura):
        return  ((base_menor + base_maior) * altura) / 2


class CalculadoraDeVolume():

    def volume_cubo(self,lado):
        return math.pow(lado, 3)
    
    def volume_paralelepipedo(self, comprimento, largura, altura):
        return comprimento * largura * altura
    
    def volume_cilindro(self, raio, altura):
        return math.pi * (math.pow(raio, 2) * altura)
    
    def volume_esfera(self, raio):
        return (4 / 3) * math.pi * (math.pow(raio, 3))
    
    def volume_cone(self, raio, altura):
        return (1 / 3) * math.pi * (math.pow(raio, 2) * altura)
    
    def volume_piramide(self, area_base, altura):
        return ( 1 / 3) * area_base * altura