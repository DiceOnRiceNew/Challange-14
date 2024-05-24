import fisika
import time
def batas():
    print("-"*15)
    
waktu_awal = time.time()
    
print(f"Massa Jenis = {fisika.MassaJenis.MassaJenis(10,2)}")
print(f"Massa Jenis = {fisika.MassaJenis.Massa(10,2)}")
print(f"Massa Jenis = {fisika.MassaJenis.Volume(10,2)}")

waktu_akhir = time.time()
print(f"Waktu yang dibutuhkan : {waktu_akhir - waktu_awal}")

batas()
print(f"Usaha = {fisika.U(12,3)}")
print(f"Gaya = {fisika.G(6,2)}")
print(f"Gaya = {fisika.J(9,3)}")

batas()

print(f"Hasil Energi Potensial : {fisika.Ep(4,7,4)}")
print(f"Hasil Energi Kinetik : {fisika.Ek(4,10)}")

batas()

print(f"Total harga setelah diskon : {fisika.Ds(40000,60)}")