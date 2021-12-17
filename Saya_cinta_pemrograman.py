a=int(input("masukkan angka pertama: "))
b=int(input("masukkan angka kedua: "))
maks=0

if a>b:
    maks=a
elif a==b:
    print ('2 angka sama besar')
else:
    maks=b
print ('angka terbesar adalah: ',maks)
