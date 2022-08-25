import json

archivo = open("tarea1.txt", "w")
archivo.write("Alexia,Putellas ,28 \n")
archivo.write("Michel, Romero,20 \n")
archivo.write("Cristobal, Colon, 80 \n")
archivo.write("Edwin, Cevallos, 61 \n")
archivo.write("Diana, Spencer,63 \n")
archivo.write("Daniel, Radcliffe,33 \n")
archivo.write("Justin, Bieber,29 \n")
archivo.write("Freddie, Highmore,30 \n")
archivo.write("Jonny, Deep,53 \n")
archivo.write("Camila,  Vasquez,38 \n")

archivo = open("tarea1.txt", "r")
d={}
archivo2 = open("tarea.txt", "w")
for line in archivo:
    name,lname,age=line.strip().split(",")
    d = {"nombre": name, "apellido": lname, "edad": age,}
    archivo2.write(json.dumps(d))
    archivo2.write("\n")
    
#{{nombre:Michel,apellido:Romero,edad:20}}


archivo2 = open("tarea.txt", "r")
Lines = archivo2.readlines()
