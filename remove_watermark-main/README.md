# remove_watermark

Hapus watermark dari gambar otomatis pakai AI. Support Linux, Arch Linux, dan Termux.

## Installation

### Termux (Android)
```bash
git clone https://github.com/piwwing23/remove_watermark.git
cd remove_watermark
bash setup-termux.sh
```

### Linux (Debian/Ubuntu/Arch)
```bash
git clone https://github.com/piwwing23/remove_watermark.git
cd remove_watermark
bash setup.sh
```

## Usage

```bash
# Satu gambar
./dist/main gambar.jpg

# Banyak gambar sekaligus
./dist/main foto1.jpg foto2.png foto3.webp

# Pake wildcard
./dist/main *.jpg

# Campur format beda
./dist/main selfie.png liburan.jpg screenshot.webp

# Dari folder berbeda
./dist/main ~/Downloads/gambar.jpg ./foto/lama.png

# Pake path absolut
./dist/main /storage/emulated/0/DCIM/Camera/foto.jpg

# Semua file gambar dalam folder
./dist/main *.jpg *.png *.jpeg *.webp
```

## Output

| Input | Output |
|-------|--------|
| `foto.jpg` | `foto_cleaned.jpg` |
| `dir/gambar.png` | `dir/gambar_cleaned.png` |
| `~/Pictures/selfie.webp` | `~/Pictures/selfie_cleaned.webp` |
| `a.jpg b.jpg c.jpg` | `a_cleaned.jpg`, `b_cleaned.jpg`, `c_cleaned.jpg` |

## Supported Formats

- `.jpg` / `.jpeg`
- `.png`
- `.webp`
