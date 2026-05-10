# ✅ JANGAN HAPUS BAGIAN DI BAWAH INI
from flask import Flask
app = Flask(__name__)

# ==============================================
# HALAMAN UTAMA
# ==============================================
@app.route('/')
def beranda():
    return """
 # Program Pemesanan Makanan & Minuman
print("="*40)
print("          DAFTAR MENU KEDAI MAKAN")
print("="*40)

# Daftar Makanan
print("\n📌 MAKANAN")
print("1. Nasi Goreng       : Rp 15.000")
print("2. Bakso             : Rp 10.000")
print("3. Gorengan (1 buah) : Rp 2.000")

# Daftar Minuman
print("\n📌 MINUMAN")
print("4. Es Teh            : Rp 5.000")
print("5. Kopi              : Rp 5.000")
print("6. Nutrisari Dingin  : Rp 5.000")
print("="*40)

# Inisialisasi variabel
total_harga = 0
pesanan = []

# Proses pemesanan
while True:
    pilih = int(input("\nMasukkan nomor pesanan (0 untuk selesai): "))

    if pilih == 0:
        break

    elif pilih == 1:
        pesanan.append("Nasi Goreng")
        total_harga += 15000
        print("✅ Nasi Goreng ditambahkan")

    elif pilih == 2:
        pesanan.append("Bakso")
        total_harga += 10000
        print("✅ Bakso ditambahkan")

    elif pilih == 3:
        jumlah = int(input("Masukkan jumlah gorengan: "))
        pesanan.append(f"Gorengan x{jumlah}")
        total_harga += (2000 * jumlah)
        print(f"✅ Gorengan sebanyak {jumlah} buah ditambahkan")

    elif pilih == 4:
        pesanan.append("Es Teh")
        total_harga += 5000
        print("✅ Es Teh ditambahkan")

    elif pilih == 5:
        pesanan.append("Kopi")
        total_harga += 5000
        print("✅ Kopi ditambahkan")

    elif pilih == 6:
        pesanan.append("Nutrisari Dingin")
        total_harga += 5000
        print("✅ Nutrisari Dingin ditambahkan")

    else:
        print("❌ Nomor menu tidak tersedia!")

# Tampilkan Ringkasan Pesanan
print("\n" + "="*40)
print("           RINGKASAN PESANAN")
print("="*40)
for item in pesanan:
    print(f"- {item}")
print(f"\nTOTAL YANG HARUS DIBAYAR: Rp {total_harga:,}")
print("="*40)

# Metode Pembayaran
print("\n💳 METODE PEMBAYARAN")
print("1. DANA     : 087872273979")
print("2. GoPay    : 087872273979")
print("3. Bayar di Kasir")

bayar = input("\nPilih cara pembayaran (1/2/3): ")

if bayar == "1" or bayar == "2":
    print("\n✅ Silakan transfer ke nomor di atas. Terima kasih sudah memesan!")
elif bayar == "3":
    print("\n✅ Silakan bayar langsung di kasir. Terima kasih sudah memesan!")
else:
    print("\n✅ Pesanan dicatat. Silakan menunggu pesanan Anda.")

print("="*40)
    """

# ✅ JANGAN HAPUS BAGIAN DI BAWAH INI
if __name__ == '__main__':
    app.run(debug=True)
