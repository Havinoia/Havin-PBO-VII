#HAVIN NEO DIMAS NUGRAHA
#5210411212

class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswa1 = Mahasiswa("Nadia", "5210411245", "Informatika")
mahasiswa2 = Mahasiswa("Febriyan", "5210411203", "Informatika")
mahasiswa3 = Mahasiswa("Revy", "5210411227", "Informatika")
mahasiswa4 = Mahasiswa("Zidni", "5210411217", "Informatika")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("List Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")

