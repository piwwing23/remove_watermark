import requests, json, time, uuid, os, sys

BASE = "https://image-generation.perchance.org/api"

def buat_gambar(user_key, prompt, negatif=", ugly, amputee, deformed", 
                res="512x768", guidance=7, seed=-1, channel="pretty-ai",
                cf_clearance=None):
    
    s = requests.Session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/149.0.0.0 Safari/537.36",
        "Origin": "https://image-generation.perchance.org",
        "Referer": "https://image-generation.perchance.org/embed",
    })
    if cf_clearance:
        s.cookies.set("cf_clearance", cf_clearance, domain=".image-generation.perchance.org")
    
    rid = str(uuid.uuid4())
    cb = str(time.time()).replace(".", "")
    
    # Kirim generate
    params = {"userKey": user_key, "requestId": rid, "adAccessCode": "", "__cacheBust": cb}
    data = {
        "adAccessCode": "",
        "channel": channel,
        "guidanceScale": guidance,
        "negativePrompt": negatif,
        "prompt": prompt,
        "requestId": rid,
        "resolution": res,
        "seed": seed,
        "subChannel": "public",
        "userKey": user_key
    }
    r = s.post(f"{BASE}/generate", params=params, json=data, timeout=30)
    if r.status_code != 200:
        return False, f"Gagal: {r.status_code} {r.text[:200]}"
    
    # Polling queue
    for _ in range(60):
        q = s.get(f"{BASE}/getUserQueuePosition", 
                   params={"userKey": user_key, "requestId": rid}, timeout=10)
        if q.status_code == 200:
            try:
                pos = q.json()
                if pos == -1 or (isinstance(pos, dict) and pos.get("position") == -1):
                    break
            except: pass
        time.sleep(1)
    else:
        return False, "Timeout queue"
    
    # Ambil hasil
    for _ in range(30):
        a = s.get(f"{BASE}/awaitExistingGenerationRequest",
                   params={"userKey": user_key, "__cacheBust": str(time.time()).replace(".", "")},
                   timeout=10)
        if a.status_code == 200 and len(a.text) > 30:
            break
        time.sleep(1)
    else:
        return False, "Timeout hasil"
    
    try:
        hasil = a.json()
    except:
        return False, f"Parse gagal: {a.text[:200]}"
    
    if "t" in hasil or "token" in hasil:
        token = hasil.get("t") or hasil.get("token")
        dl = s.get(f"{BASE}/downloadTemporaryImageViaProxy", params={"t": token}, timeout=30)
        if dl.status_code == 200 and "image" in dl.headers.get("content-type", ""):
            nama = f"output_{uuid.uuid4().hex[:8]}.jpg"
            with open(nama, "wb") as f:
                f.write(dl.content)
            return True, nama
        return False, "Download gagal"
    
    elif "edited_image" in hasil:
        import base64
        img_data = hasil["edited_image"]["image"]
        nama = f"output_{uuid.uuid4().hex[:8]}.jpg"
        with open(nama, "wb") as f:
            f.write(base64.b64decode(img_data))
        return True, nama
    
    return True, str(hasil)[:200]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pemakaian: python3 perchance.py 'prompt'")
        print("Atur USER_KEY dan CF_CLEARANCE di file atau env")
        sys.exit(1)
    
    prompt = sys.argv[1]
    user_key = os.environ.get("USER_KEY") or input("userKey: ")
    cf = os.environ.get("CF_CLEARANCE") or input("cf_clearance cookie: ")
    
    ok, msg = buat_gambar(user_key, prompt, cf_clearance=cf)
    print(f"{'OK' if ok else 'ERROR'}: {msg}")
