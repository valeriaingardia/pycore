import math 

print ("RISOLUZIONE EQUAZIONI DI SECONDO GRADO")
print ("Sia data l'equazione di secondo grado nella forma ax^2 + bx + c = 0")

a = 0 
while a == 0:
    a = float(input("Inserire a: "))
b= float(input("Inserire b: "))
c= float(input("Inserire c: "))

delta = b**2 - 4*a*c
if delta < 0:
    print ("L'equazione non ha soluzioni reali")
elif delta == 0:
    print ("L'equazione ha una soluzione reale doppia")
    x= -b / (2*a)
else :
    print ("L'equazione ha due soluzioni reali distinte")
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print ("Le soluzioni dell'equazione sono: x1 =", x1, "e x2 =", x2)

