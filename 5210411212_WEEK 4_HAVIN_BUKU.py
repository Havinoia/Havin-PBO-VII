#HAVIN NEO DIMAS NUGRAHA
#5210411212

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit, jmlh_halaman) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__jmlh_halaman = jmlh_halaman

    def Tampil(self) :
        print(f"Buku {self.judul} karangan {self.pengarang} pertama kali diterbitkan tahun {self.tahun_terbit}")
        print(f"Buku {self.judul} jumlah halamannya adalah {self.__jmlh_halaman}\n")

buku1 = Buku("Kamu terlalu banyak bercanda", "Marchella FP", 2019, 234)
buku2 = Buku("Sang pemimpi", "Andrea Hirata", 2006, 214)
buku3 = Buku("Sebuah seni untuk bersikap bodo amat", "Mark Manson", 2018, 211)

kumpulan_buku = [buku1, buku2, buku3]
print("\n\tList Buku\n================================")
for buku in kumpulan_buku :     
     buku.Tampil()
print("\n")