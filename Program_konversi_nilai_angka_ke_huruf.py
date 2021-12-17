# Program konversi nilai angka ke huruf

angka=float(input("Masukkan angka: "))
if (angka >=0 and angka <=20):
    print ("E")
elif (angka >20 and angka <= 40):
    print ("D")
elif (angka >41 and angka <=60):
    print ("C")
elif (angka >61 and angka <=70):
    print ("CD")
elif (angka >71 and angka <=80):
    print ("B")
elif (angka >81 and angka <=90):
    print ("AB")
else :
    print ("A")
