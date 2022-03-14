#5210411212
#HAVIN NEO DIMAS NUGRAHA
#PBO 7 WEEK 5

#Multilevel Inheritance
#Parent Class
class Hewan :
    def bersuara(self) :
        print("Kucing Bersuara")
    
#Anak class mewarisi class hewan
class Kucing(Hewan) :
    def suara(self) :   
        print("miaw...miaw")

#Anak class Anakkucing mewarisi dari class hewan
class AnakKucing(Kucing) :
    def minum(self) :   
        print("Minum air")
    
#Objek
cat = AnakKucing()
cat.bersuara()
cat.suara()
cat.minum()

