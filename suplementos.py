
class Cliente1070:
    id_peoduct = 0
    Nombre = ""
    tipo = ""
    Sabor = ""
    peso = 0
    precio_uni = 0
    def MostrarDatos(self, id_product, Nombre, tipo, sabor, peso, precio_uni):SSSSSSSSSSSSSSSS
        print(f"Id de producto {id_product}")
        print(f"Nombre del producto {Nombre}")
        print(f"tipo de producto {tipo}")
        print(f"sabor del producto {sabor}")
        print(f"peso del producto {peso}")
        print(f"Curp del Cliente {precio_uni}")
    def lista_Clientes(self):
        print("Lista de alumnos")
        ListaC = ["Emiliano","cesar","justin","melany","paola"]
        for x in ListaC:
            print(x)
    def Tupla_Provedores(self):
        TuplaP = ("emvape","Juan","Jose","martinez","molinar")
        print("Tupla provedores")
        for x in TuplaP:
            print(x)
    def Dic_Sabores(self):
        print("Diccionario de Sabores")
        suple = {"proteina" : "creamoreo",
                    "vitamina" : "naranja",
                    "creatina" : "uva" , 
                    "chochos" : "frambuesa",
                    "barrasP" : "chocolate"}
        for x,y in suple.items():
            print(x,y)
Objet=Cliente1070()
prod2=Cliente1070()
Objet.id_peoduct=168332
Objet.Nombre="superProtein"
Objet.tipo="polvo"
Objet.Sabor="creamoreo"
Objet.peso=1
Objet.precio_uni=1600
print("informacion sobre nuestro producto")
Objet.MostrarDatos(Objet.id_peoduct,Objet.Nombre,Objet.tipo,Objet.Sabor,Objet.peso,Objet.precio_uni)
print("-nuestros clientes mas fieles-")
prod2. lista_Clientes()
print("-Nuestros provedores <3-")
prod2.Tupla_Provedores()
print("-Nuestros sabores-")
prod2.Dic_Sabores()