number_1 = 10
number_2 = 20
number_3 = 30
number_4 = 40
c = number_1 + number_2 + number_3 + number_4
print("la suma de los cuatro numeros es:", c)

number_4 = 40
number_5 = 50
d = number_4 + number_5
print("la suma de los dos numeros es:", d)

lado_1 = int(input("ingrese un numero: "))
lado_2 = int(input("ingrese el segundo numero: "))
lado_3 = int(input("ingrese el tercer numero: "))

if lado_1 == lado_2 == lado_3:
    print("los tres lados son iguales")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("dos lados son iguales y uno no")
else:
    print("los tres lados son diferentes")
