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

**Contoh penggunaan (Gambar di dalam folder src):**
```bash
python3 src/main.py src/gambar.jpg
```

### 📂 Menangani Gambar di Direktori Berbeda
Jika gambar yang ingin diproses berada di lokasi lain, Anda **wajib** menggunakan *full path* (lokasi lengkap) gambar tersebut agar tidak terjadi error `FileNotFoundError`:

**Contoh jika gambar ada di folder Downloads (Penyimpanan Internal):**
```bash
python3 src/main.py /sdcard/Download/gambar_saya.jpg
```

*Hasil pemrosesan akan otomatis tersimpan di lokasi yang sama dengan lokasi file gambar asli.*

## 🔐 Catatan Teknis & Hak Kekayaan Intelektual
- **Perlindungan Kode**: Proyek ini menggunakan metode kompilasi biner untuk melindungi kekayaan intelektual (IP) dan mencegah pencurian, modifikasi, atau penyalahgunaan logika aplikasi oleh pihak yang tidak berwenang.
- **Integritas Proyek**: Dengan menggunakan format biner, kode inti aplikasi dijamin tetap tertutup dan terlindungi dari upaya *reverse engineering* yang mudah, memastikan keunikan algoritma tetap terjaga.
- **Portabilitas**: Modul biner yang dihasilkan bersifat *platform-specific* (spesifik untuk arsitektur CPU dan versi Python perangkat Anda). Jika Anda memindahkan proyek ke perangkat lain, **wajib** melakukan kompilasi ulang (langkah Instalasi nomor 3) agar kompatibel dengan lingkungan baru.

## ⚠️ Disclaimer
Alat ini ditujukan untuk tujuan edukasi dan penggunaan pribadi. Pengguna bertanggung jawab sepenuhnya atas penggunaan perangkat lunak ini sesuai dengan hukum dan kebijakan hak cipta yang berlaku.
