#HAVIN NEO DIMAS NUGRAHA
#5210411212

class Menu :
    def __init__(self, nama, deskripsi, harga, stok) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__stok = stok

    def Tampil(self) :
        print(f"{self.nama} harga Rp {self.harga} \n---> {self.deskripsi} sisa stok {self.__stok}\n")

minuman1 = Menu("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000, 6)
minuman2 = Menu("Jus Jambu", "Jus jambu merah tanpa gula", 8500,9)
minuman3 = Menu("Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500, 6)
minuman4 = Menu("Jus Alpukat", "Jus alpukat dengan gula merah", 15000, 4)

makanan1 = Menu("Kerang Dara", "Kerang asam manis", 25000, 4)
makanan2 = Menu("Magelangan", "Magelangan dengan telur", 12000, 3)
makanan3 = Menu("Ayam Geprek", "Ayam geprek dengan Es Teh", 10000, 6)
makanan4 = Menu("Nasi Goreng", "Nasi Goreng dengan telur setengah matang", 8000, 8)

pilihan_makanan = [makanan1, makanan2, makanan3, makanan4]
pilihan_minuman = [minuman1, minuman2, minuman3, minuman4]  

print("\nDaftar Menu Makanan\n==========================")
for mkn in pilihan_makanan :
    mkn.Tampil()
print("\nDaftar Menu Minuman\n==========================")
for mn in pilihan_minuman :         
    mn.Tampil()
print("\n")