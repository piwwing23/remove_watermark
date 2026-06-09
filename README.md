# Watermark Remover

Alat penghapus watermark otomatis berbasis biner (terkompilasi).

## 🚀 Persiapan Pengguna Termux Baru (PENTING)
Jika Anda baru saja menginstal Termux, Anda **wajib** melakukan langkah-langkah di bawah ini agar perangkat siap untuk kompilasi biner:

1. **Update dan Upgrade Repositori:**
   ```bash
   pkg update && pkg upgrade -y
   ```

2. **Instal Paket yang Dibutuhkan:**
   ```bash
   pkg install python git clang make build-essential -y
   ```

3. **Berikan Izin Penyimpanan:**
   ```bash
   termux-setup-storage
   ```
   *(Klik "Allow" saat muncul pop-up di layar).*

---

## 🛠 Persyaratan Sistem
- Python 3.x
- `requests`, `PyJWT`, `Pillow` (Pustaka Python yang diperlukan)
- `Cython` (Untuk kompilasi biner)

## 📥 Instalasi

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/piwwing23/remove_watermark.git
   cd remove_watermark
   ```

2. **Instal dependensi:**
   ```bash
   pip install requests PyJWT Pillow Cython
   ```

3. **Kompilasi Modul (Wajib Dilakukan di Perangkat Anda):**
   ```bash
   cd src/
   python3 setup.py build_ext --inplace
   ```

## 💻 Cara Penggunaan

Pastikan file `src/main.py` dan `src/core.so` berada di folder `src/`. Jalankan aplikasi dari direktori utama proyek:

**Contoh penggunaan:**
```bash
python3 src/main.py gambar.jpg
```

*Hasil pemrosesan akan otomatis tersimpan dengan format `<nama_file>_cleaned.png` di folder yang sama.*

## 🔐 Catatan Teknis
- **Keamanan**: Alat ini menggunakan modul terkompilasi (`.so`) untuk melindungi algoritma dari modifikasi/pencurian.
- **Portabilitas**: Jika Anda memindahkan proyek ini ke perangkat lain, **wajib** melakukan kompilasi ulang (langkah Instalasi nomor 3) karena biner `.so` spesifik untuk arsitektur CPU perangkat Anda.

## ⚠️ Disclaimer
Alat ini ditujukan untuk tujuan edukasi dan penggunaan pribadi. Pengguna bertanggung jawab sepenuhnya atas penggunaan perangkat lunak ini sesuai dengan hukum dan kebijakan hak cipta yang berlaku.
