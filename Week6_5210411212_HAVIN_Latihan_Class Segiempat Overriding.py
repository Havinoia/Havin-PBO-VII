#5210411212
#HAVIN NEO DIMAS NUGRAHA

class Segiempat():
    def __init__(self, panjang, lebar) -> None:
        self.panjang = panjang
        self.lebar = lebar
        
    def hitungLuas(self): #method overriding
        print("Luas Segiempat =", self.panjang * self.lebar, "m^2")
       
class Bujursangkar(Segiempat):
    def __init__(self, sisi):
        self.side = sisi
        Segiempat.__init__(self,sisi,sisi)
        
    def hitungLuas(self): #method overriding
        print("Luas Bujur sangkar =", self.side*self.side, "m^2")
      
b=Bujursangkar(4)
s=Segiempat(2,4)
b.hitungLuas()
s.hitungLuas()
