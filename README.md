# Watermark Remover

Alat penghapus watermark otomatis berbasis biner (terkompilasi).

## Persyaratan
- Python 3.x
- `requests`, `PyJWT`, `Pillow` (Pustaka Python yang diperlukan)

## Instalasi

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/piwwing23/remove_watermark.git
   cd remove_watermark
   ```

2. **Instal dependensi:**
   ```bash
   pip install requests PyJWT Pillow
   ```

## Cara Penggunaan

Pastikan file `src/main.py` dan `src/core.so` berada di dalam satu folder yang sama.

1. **Jalankan aplikasi:**
   Gunakan terminal untuk menjalankan skrip melalui Python:
   ```bash
   python3 src/main.py <path_ke_gambar>
   ```

2. **Contoh penggunaan:**
   ```bash
   python3 src/main.py gambar.jpg
   ```

3. **Hasil:**
   Gambar yang telah diproses akan disimpan secara otomatis dengan format nama `<nama_file>_cleaned.png` di folder yang sama.

## Struktur Repositori
- `src/main.py`: Loader utama untuk menjalankan modul biner.
- `src/core.so`: Modul biner terkompilasi yang berisi logika pemrosesan.
- `src/setup.py`: Script untuk kompilasi ulang (hanya jika diperlukan pada lingkungan baru).

## Catatan Penting
- Alat ini menggunakan biner terkompilasi untuk menjaga keamanan logika internal.
- Pastikan lingkungan Python Anda memiliki izin akses untuk memuat modul biner (`.so`).
- Jika Anda berpindah ke perangkat/OS lain dengan arsitektur berbeda, Anda perlu melakukan kompilasi ulang menggunakan `python3 src/setup.py build_ext --inplace`.
