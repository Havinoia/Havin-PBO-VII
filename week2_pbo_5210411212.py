#buat list
merk_hp = ('asus', 'samsung', 'huaweii', 'xiaomi', 'vivo')
print(merk_hp)

#ubah list menjadi set
merk_hp = set(['asus', 'samsung', 'huaweii', 'xiaomi', 'vivo'])
print(merk_hp)

#buat Set dengan berbagai tipe data
set_merkhp = {'samsung', 'galaxy', 24, True, ('A', 'B')}
print(set_merkhp)

print("")
himpunan_huruf = {'a', 'b', 'c'}
print(himpunan_huruf)

#Add
himpunan_huruf.add('d')
himpunan_huruf.add('e')
print(himpunan_huruf)

#Update
himpunan_huruf.update({ 'f', 'g' })
print(himpunan_huruf)

print("")
himpunan = {'havin', 'agus', 100, ('a', 'b'), False, True}
print(himpunan)

#Remove
himpunan.remove(100)
print(himpunan)

#Discard
himpunan.discard(('a', 'b'))
print(himpunan)

#Pop
nilaiYangDihapus = himpunan.pop()
print('nilaiYangDihapus =', nilaiYangDihapus)
print(himpunan)

#Clear
himpunan.clear()
print(himpunan)

laki = {
  'riko', 'tono', 'bagas', 'tino'
}
perempuan = {
  'rara', 'tini', 'vina', 'febi'
}
print("")

#Union (Gabungan)
print(laki.union(perempuan))

#Intersection (Irisan)
print(laki.intersection(perempuan))

#Difference (Selisih)
print('\nanggota grup laki yang bukan anggota grup perempuan')
print(laki - perempuan)
print(laki.difference(perempuan))

print('\ndibalik, anggota grup perempuan yang bukan anggota grup laki :')
print(perempuan - laki)
print(perempuan.difference(laki))

#Symmetric Difference
print('\nanggota yang hanya ikut satu grup saja :')
print(perempuan.symmetric_difference(laki))