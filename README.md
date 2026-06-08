# Watermark Remover

Alat penghapus watermark otomatis berbasis biner (terkompilasi).

## Instalasi
1. Clone repositori ini.
2. Pastikan file `core.so` dan `main.py` berada dalam satu folder.

## Cara Penggunaan
Jalankan file `main.py` menggunakan Python 3 dengan menyertakan path gambar yang ingin diproses:

```bash
python3 main.py <nama_gambar.jpg>
```

Contoh:
```bash
python3 main.py tes.png
```

Hasil gambar yang sudah bersih akan tersimpan dengan akhiran `_cleaned.png` di folder yang sama.
