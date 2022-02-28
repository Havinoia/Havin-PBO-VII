#HAVIN NEO DIMAS NUGRAHA
#5210411212

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("Kamu terlalu banyak bercanda", "Marchella FP", 2019)
buku2 = Buku("Sang pemimpi", "Andrea Hirata", 2006)
buku3 = Buku("Sebuah seni untuk bersikap bodo amat", "Mark Manson", 2018)

bukus = [buku1, buku2, buku3]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")