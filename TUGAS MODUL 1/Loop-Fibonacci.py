# input jumlah deret 
n = 10

# inisialisasi dua angka pertama 
a = 1 
b =1

print("Deret Fibonacci dengan",n,"bilangan")
print(a, end='') # cetak angka pertama 
print(b, end='') #cetak angka kedua

#proses fibonacci
for i in range(2,n):
#range(2,10) karena 2 angka sudah dicetak c = a + b 
#angka selanjutnya adalah penjumlahan 2 angka sebelumnya 
   print(c,end='')
# Update nilai untuk iterasi selanjutnya 
a = b 
b = c 