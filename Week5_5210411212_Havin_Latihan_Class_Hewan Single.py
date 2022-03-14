#5210411212
#HAVIN NEO DIMAS NUGRAHA
#PBO 7 WEEK 5

#Single Inheritance

#Parent Class
class Hewan :   
    def bersuara(self) :
        print("Kucing Bersuara")

# Anak class mewarisi parent class
class Kucing(Hewan) :
    def suara(self) :
        print("miaw...miaw")


#Objek
cat = Kucing()
cat.suara()
cat.bersuara()

