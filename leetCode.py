nums = int(input("Masukkan angka: "))
num = nums 
hasil = 0

temp = nums
while temp > 0:
    hasil += temp % 10
    temp //= 10 

i = 2
faktor = []
while i * i <= num:
    while num % i == 0:
        faktor.append(i)  
        num //= i 
    i += 1

if num > 1:
    faktor.append(num)

hasil2 = 0
hasil2 = 0
for i in faktor:
    while i > 0:
        hasil2 += i % 10
        i //= 10

if hasil == hasil2:
    print(True)
else:
    print(False)