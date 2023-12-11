import math
def tambah(bil1, bil2):
    hasil = bil1+bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)
def kurang(bil1, bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)
def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)
def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)
def log(bil1):
    hasil = math.log10(bil1)
    print("hasil dari log",bil1,'=', hasil)
def akar(bil1):
    hasil = math.sqrt(bil1)
    print("hasil akar dari",bil1,"=",hasil)
def sin(nilai):
    hasil = math.sin(nilai)
    print("hasil sin dari", nilai, "=", hasil)

def cos(nilai):
    hasil = math.cos(nilai)
    print("hasil cos dari", nilai, "=", hasil)

def tan(nilai):
    hasil = math.tan(nilai)
    print("hasil tan dari", nilai, "=", hasil)