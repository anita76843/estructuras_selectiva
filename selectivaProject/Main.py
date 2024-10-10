#simple
a= 33
b= 200

if b>a:
    print(b,"es mayor que ",a)

#doble
y= 200
z= 333

if y > z:
    print(y,"es mayor que",z)
else:
    print(y,"no es mayor que ",z)

#multiple

c= 200
d= 207

if c>d:
    print(c,"es mayor que",d)
elif c<d:
    print(c,"es menor que",d)
else:
    print(c,"es igual que",d)


#enlazadas

e=28

if e > 10:
    print("por encima de diez,")
if e > 20:
    print("y tambien por encima de 20!")
else:
    print("pero no por encima de 20.")

#end y sep
print("estudiar los sabados", end =' ')
print(" es genial")


print("daniela","luis", "carlos","camila")#agrega espacios por defecto
print("daniela","luis", "carlos","camila", sep="")#quita espacios
print("daniela","luis", "carlos","camila",sep= ",")# agrega comas
print("daniela","luis", "carlos","camila",sep = "_",end ="_curso_python")#implemetacion end y sep





















