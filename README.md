# Watermark Remover

Remove watermark dari gambar otomatis pakai AI. **No limit**, bypass rate limit 3x/hari.

## Fitur

- 🚀 Hapus watermark otomatis
- 🔄 Bypass rate limit (3 request/akun, auto rotate akun)
- 🔒 Code terenkripsi (compiled binary, bukan Python source)
- 💻 Support Linux, Arch Linux, Termux

## Instalasi

```bash
# Clone repo
git clone https://github.com/piwwing23/remove_watermark.git
cd remove_watermark

# Install (detek OS otomatis)
bash setup.sh
```

Proses instalasi:
- Detek OS (Arch/Debian/Termux)
- Install Python + dependencies
- Compile ke binary (20MB, butuh ~2 menit)
- Hapus file source (hanya binary tersisa)

## Pemakaian

```bash
# Langsung pake binary (setelah install)
./dist/main gambar.jpg

# Banyak gambar sekaligus
./dist/main gambar1.jpg gambar2.jpg gambar3.jpg
```

Hasil: `gambar_cleaned.jpg` (di folder yang sama)

## Cara Kerja

| Komponen | Keterangan |
|----------|-----------|
| JWT | Generate sendiri, gak perlu login |
| Firebase | Auto bikin akun baru tiap 3 request |
| Rate limit | Bypass pakai rotate Firebase account |
| Code | Encrypted + compiled binary, gak bisa dibaca |

## Struktur File

```
remove_watermark/
├── setup.sh        # Installer (Linux/Arch/Termux)
├── dist/main       # Compiled binary (setelah install)
├── venv/           # Virtual environment (auto generated)
└── README.md
```

## Catatan

- JWT secret & Firebase key udah di-encrypt di dalam binary
- Source code asli **tidak bisa dilihat** (compiled + encrypted)
- Rate limit API: 3 req/akun → auto rotate akun Firebase
- API endpoint: `api.watermark.phd` (reverse engineered)
