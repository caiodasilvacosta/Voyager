import math

# Activity 01: Faça um programa que leia um número inteiro e imprima.
integer = int(input("Give me an integer number: "))
print("The number you've just written is " + str(integer))
print(format("O tipo de variável de 'integer' é " + str(type(integer))))  #essa linha ficou uma zona. Só um teste porque não consegui com o "format"

#Activity 02: Faça um programa que leia um número real e o imprima.
real = float(input("Agora, por favor, digite um número real: "))
print("O número real que você digitou é " + str(real))

#Activity 03: Peça ao usuário para digitar três valores inteiros e digite a soma deles.
numero_1 = int(input("Type a first number: "))
numero_2 = int(input("Now, you type a second number: "))
numero_3 = int(input("A third number: "))
soma_1 = numero_1 + numero_2 + numero_3
print("The summation of the numbers you've just typed is " + str(soma_1))
print("The summation of the numbers you've just typed is", numero_1 + numero_2 + numero_3)

# Practice on Interpolation:
print("The summation of the numbers {}, {} and {} you've just typed is {}".format(numero_1, numero_2, numero_3, soma_1))
print(f"A soma entre {numero_1}, {numero_2} e {numero_3} é {soma_1}")
print("Os valores somados são: ", numero_1 + numero_2 + numero_3)

# Activity 04: Peça ao usuário para digitar um número real e imprima o quadrado desse número:
real_2 = float(input("Please, type a real number of your choosing: "))
square_real = real_2 ** 2
print("The square of your number is {}".format(square_real))

# Activity 05: Peça ao usuário para digitar um número real e imprima a quinta parte deste número:
real_3 = float(input("Please, type another real number: "))
fifth_part = real_3 / 5
print(f"The fifth part of your number is {fifth_part}")

#Activity 06: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é F = C * (9.0/5.0) + 32.0.
temp_celsius = float(input("Please, provide the temperature in Celsius: "))
temp_fah = temp_celsius * (9.0 / 5.0) + 32.0
print("The temperature of {} degrees Celsius corresponds to {} degrees Fahrenheit!".format(temp_celsius, temp_fah))

#Activity 07: Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é C = K -273.15.
temp_kelvin = float(input("Please, provide the temperature in Kelvin: "))
temp_celsius_2 = temp_kelvin - 273.15
print("The temperature of {} Kelvin corresponds to {} degrees Celsius!".format(temp_kelvin, temp_celsius_2))

#Activity 08: Leia um ângulo em graus e apresente-o em radianos. A fórmula de conversão é R = G * Pi/180
angle_degrees = float(input("Please, provide the value of your angle in degrees: "))
angle_rad = angle_degrees * math.pi / 180
print("The value of the angle {} in degrees corresponds to {} in radianos!".format(angle_degrees, angle_rad))

#Activity 09: Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. A fórmula de conversão é C = P * 2.54.
valor_pol = float(input("Please, provide the length in inches: "))
valor_comp = valor_pol * 2.54
print("The lenght of {} inches corresponds to {} centimeters".format(valor_pol, valor_comp))

#Activity 10: Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três fatores lidos.
value_one = float(input("Please, provide the first value: "))
value_two = float(input("Please, provide the second value: "))
value_three = float(input("Please, provide the third and last value: "))
result_square = value_one ** 2 + value_two ** 2 + value_three ** 2
print("The sum of the squares of your values is {}".format(result_square))
