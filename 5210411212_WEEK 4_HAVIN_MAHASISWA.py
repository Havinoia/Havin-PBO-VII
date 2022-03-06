#HAVIN NEO DIMAS NUGRAHA
#5210411212

class Mahasiswa :
    def __init__ (self, nama, nim, prodi, sks, semester) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.__sks = sks
        self.__semester = semester


    def Tampil(self) :\
        print(f"{self.nama} dengan nim {self.nim} prodi {self.prodi} sks {self.__sks} semester {self.__semester}")

mahasiswa1 = Mahasiswa("Nadia", "5210411245", "Informatika", "22", "2")
mahasiswa2 = Mahasiswa("Febriyan", "5210411203", "Informatika", "22", "2")
mahasiswa3 = Mahasiswa("Revy", "5210411227", "Informatika", "22", "2")
mahasiswa4 = Mahasiswa("Zidni", "5210411217", "Informatika", "22", "2")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("\n\tList Mahasiswa\n================================")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}. Saat ini sudah Semester {}, dengan mengambil mata kuliah {} SKS.'. format(mhs.nama, mhs.prodi, mhs.nim, mhs._Mahasiswa__semester, mhs._Mahasiswa__sks)
    print(teks)
print("\n")

