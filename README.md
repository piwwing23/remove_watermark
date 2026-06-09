# Watermark Remover

Alat penghapus watermark otomatis.

## 🚀 Persiapan Termux
1. Update: `pkg update && pkg upgrade -y`
2. Instal paket: `pkg install python git clang make build-essential -y`
3. Izin: `termux-setup-storage`

## 📥 Instalasi
1. Clone: `git clone https://github.com/piwwing23/remove_watermark.git`
2. Masuk folder: `cd remove_watermark`
3. Dependensi: `pip install requests PyJWT Pillow Cython`
4. Kompilasi: `cd src/ && python3 setup.py build_ext --inplace`

## 💻 Cara Penggunaan
Jalankan dari direktori utama:
```bash
python3 src/main.py <path_ke_gambar>
```
*Contoh: `python3 src/main.py src/gambar.jpg`*

## 🔐 Catatan Teknis
Kode inti aplikasi ini telah dikompilasi menjadi biner untuk **mencegah modifikasi dari luar** dan menjaga integritas serta keaslian algoritma. Jika Anda berpindah perangkat, lakukan kompilasi ulang (langkah Instalasi nomor 4) agar aplikasi tetap berjalan.

## ⚠️ Disclaimer
Pengguna bertanggung jawab penuh atas penggunaan alat ini.
