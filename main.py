from Calculadora import CalculadoraDeArea, CalculadoraDeVolume

def menu():
    print("*********************************")
    print("*******Escolha a operação!*******")
    print("*********************************")

    print("""
    [1] Calcular Área de uma figura geométrica
    [2] Calcular Volume de uma figura geométrica
    [0] Sair
      """)
def menu_area():
    print("Deseja calcular a área de qual figura geométrica: ")
    print("""
    [1] Área do Quadrado
    [2] Área do Retângulo
    [3] Área do Círculo
    [4] Área do Triângulo
    [5] Área do Trápezio
    [0] Voltar ao menu principal
        """)
def menu_volume():
    print("Deseja calcular o volume de qual figura geométrica: ")
    print("""
    [1] Volume do Cubo
    [2] Volume do Paralelepipedo
    [3] Volume do Cilindro
    [4] Volume da Esfera
    [5] Volume do Cone
    [6] Volume da Pirâmide
    [0] Voltar ao menu principal
        """)
    
def eh_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))  # Converte a entrada para float
            if valor > 0:
                return valor  # Retorna o valor se for positivo
            else:
                print("Por favor, insira um número maior que zero.")
        except ValueError:
            print("Entrada inválida! Insira um número válido.")
def operacao_escolhida_area(resposta_area, calcArea):
    if resposta_area == 1:
       lado = eh_positivo("Informe quanto vale o lado do quadrado: ")
       return calcArea.area_quadrado(lado)
    elif resposta_area == 2:
        comprimento = eh_positivo("Informe o comprimento do retângulo: ")
        largura = eh_positivo("Informe a largura do retângulo: ")
        return calcArea.area_retangulo(comprimento, largura)
    elif resposta_area == 3:
        raio = eh_positivo("Informe quanto vale o raio  do círculo: ")
        return calcArea.area_circulo(raio)
    elif resposta_area == 4:
        base = eh_positivo("Informe o valor da base do triângulo: ")
        altura = eh_positivo("Informe a altura do triângulo: ")
        return calcArea.area_retangulo(base, altura)
    elif resposta_area == 5:
        base_menor = eh_positivo("Informe o valor da base MENOR do trapézio: ")
        base_maior = eh_positivo("Informe o valor da base MAIOR do trapézio: ")
        altura = eh_positivo("Informe a altura do trapézio: ")
        return calcArea.area_trapezio(base_menor, base_maior, altura)
    elif resposta_area == 0:
        return None
    else:
        print("OPÇÃO INVÁLIDA!")
def operacao_escolhida_volume(resposta_volume, calcVolume):
    if resposta_volume == 1:
        lado = eh_positivo("Informe quanto vale o lado do cubo: ")
        return calcVolume.volume_cubo(lado)
    elif resposta_volume == 2:
        comprimento = eh_positivo("Informe o comprimento do paralelepípedo: ")
        largura = eh_positivo("Informe a largura do paralelepípedo : ")
        altura = eh_positivo("Informe a altura do paralelepípedo : ")
        return calcVolume.volume_paralelepipedo(comprimento,largura,altura)
    elif resposta_volume == 3:
        raio = eh_positivo("Informe quanto vale o raio  do cilindro: ")
        altura = eh_positivo("Informe a altura do cilindro: ")
        return calcVolume.volume_cilindro(raio, altura)
    elif resposta_volume == 4:
        raio = eh_positivo("Informe o valor do raio da esfera: ")
        return calcVolume.volume_esfera(raio)
    elif resposta_volume == 5:
        raio = eh_positivo("Informe quanto vale o raio  do cone: ")
        altura = eh_positivo("Informe a altura do cone: ")
        return calcVolume.volume_cone(raio, altura)
    elif resposta_volume == 6:
        area_base = eh_positivo("Informe quanto vale a área da base da pirâmide: ")
        altura = eh_positivo("Informe quanto vale a altura da pirâmide: ")
        return calcVolume.volume_piramide(area_base, altura)
    elif resposta_volume == 0:
        return None
    else:
        print("OPÇÃO INVÁLIDA!")


while True:
    menu()
    resposta = int(input("Digite o número da operação desejada: "))


    if resposta == 1:
        calcArea = CalculadoraDeArea()
        while True:
            menu_area()
            resposta_area = int(input("Digite o número da operação desejada: "))
            if resposta_area == 0:
                break
            resultado = operacao_escolhida_area(resposta_area, calcArea)
            if resultado is not None:
                print(f"O resultado da área é: {resultado:.2f}")

    elif resposta == 2:
        calcVolume = CalculadoraDeVolume()
        while True:
            menu_volume()
            resposta_volume = int(input("Digite o número da operação desejada: "))
            if resposta_volume == 0:
                break
            resultado = operacao_escolhida_volume(resposta_volume, calcVolume)
            if resultado is not None:
                print(f"O resultado do volume é: {resultado:.2f}")
                
    elif resposta == 0:
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção Inválida")


