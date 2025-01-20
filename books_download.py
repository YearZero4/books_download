
#-----------------------------------------------------------#
#- SCRIPT PARA DESCARGAR LIBROS O MANUALES DE PROGRAMACION -#
#-           [PGX] - NINGUN SISTEMA ES SEGURO              -#
#-----------------------------------------------------------#

import requests, re, os, sys
from colorama import init, Style, Fore
from bs4 import BeautifulSoup
init(autoreset=True)


so=os.name
if so == 'nt':
 os.system("cls")
else:
 os.system("clear")

lenguajes_dict = {
    1: "C#",
    2: "C++",
    3: "PHP",
    4: "Bash",
    5: "Rush",
    6: "Perl",
    7: "HTML",
    8: "Dart",
    9: "Java",
    10: "Ruby",
    11: "Matlab",
    12: "Scratch",
    13: "Haskell",
    14: "Batch",
    15: "Cobol",
    16: "Pascal",
    17: "Fortran",
    18: "Golang",
    19: "Python",
    20: "Kotlin",
    21: "Scheme",
    22: "Javascript",
    23: "Typescript",
    24: "Objective-C",
    25: "Visual Basic"
}
e='    '
print(f"""\n{e}SCRIPT PARA DESCARGAR LIBROS (PDF) \n{e}{e}[MANUALES DE PROGRAMACION]\n
{Style.BRIGHT}{Fore.GREEN}    [1]{Fore.WHITE} C#           {Fore.GREEN}[14]{Fore.WHITE} Batch
{Fore.GREEN}    [2]{Fore.WHITE} C++          {Fore.GREEN}[15]{Fore.WHITE} Cobol
{Fore.GREEN}    [3]{Fore.WHITE} PHP          {Fore.GREEN}[16]{Fore.WHITE} Pascal
{Fore.GREEN}    [4]{Fore.WHITE} Bash         {Fore.GREEN}[17]{Fore.WHITE} Fortran
{Fore.GREEN}    [5]{Fore.WHITE} Rush         {Fore.GREEN}[18]{Fore.WHITE} Golang
{Fore.GREEN}    [6]{Fore.WHITE} Perl         {Fore.GREEN}[19]{Fore.WHITE} Python
{Fore.GREEN}    [7]{Fore.WHITE} HTML         {Fore.GREEN}[20]{Fore.WHITE} Kotlin
{Fore.GREEN}    [8]{Fore.WHITE} Dart         {Fore.GREEN}[21]{Fore.WHITE} Scheme
{Fore.GREEN}    [9]{Fore.WHITE} Java         {Fore.GREEN}[22]{Fore.WHITE} Javascript
{Fore.GREEN}    [10]{Fore.WHITE} Ruby        {Fore.GREEN}[23]{Fore.WHITE} Typescript
{Fore.GREEN}    [11]{Fore.WHITE} Matlab      {Fore.GREEN}[24]{Fore.WHITE} Objective-C
{Fore.GREEN}    [12]{Fore.WHITE} Scratch     {Fore.GREEN}[25]{Fore.WHITE} Visual Basic
{Fore.GREEN}    [13]{Fore.WHITE} Haskell     {Fore.GREEN}[00]{Fore.WHITE} Otro
""")
opcion = int(input(f"{e}Seleccione una opcion (1-25): "))
if 1 <= opcion <= 25:
 lenguaje = lenguajes_dict[opcion]
elif 0 == opcion:
  lenguaje=input(f"\n{e}LENGUAJE DE PROGRAMACION -> ")
else:
 print("Opción no válida. Por favor, selecciona un número entre 1 y 25.")

print("")
download = 'libros_descargados/' ; n = 0 ; nf = int(input(f"{e}Cantidad de libros a descargar -> ")) ; pages=[]
url = 'https://www.google.com/search'
headers = {
    "Host": "www.google.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Cookie": "AEC=AZ6Zc-X-xDglBKUMpTHPc2HV4CtIKBu8gbOmog1VLrlTnp0C8pPX14-OTg; NID=520=ccKtMOxOSk6ODORUTRlRutLu7Qnu0XIdtyfCFv5PyvIjWc13DoSVuoUJS-feqAuyvWfKRhvyRiFgpjXMUIBZ0Jh3NDonj8ZnFhIgLBHmlo4g0iWchJKqc8Zx2C5EAUfHkB2NfmBV3iH1qciCJIvudUTEXebo_e0Oqbrjdp0_08Uy7jifFkI9Kfn2KT4fvqo28AoQpRr_3b7zMDtE9ZfogfIEkJACv_NfLEPh3yMmwNziPpr1aHe3Gj5lxf9b3yFaQ8ji39dvYuw; SG_SS=*HyOaI3vyAAaHFuaVpxZ965C58I0Szi4EADQBEArZ1NMx_u4m22rkcEoRlBz6HyNEqH_VJqHiDVxIzeQP2231y5By03pXOy9Es-IOjinvPQAAATxtAAAAQVcBB0EANbaGnzQKGj8qhaK41BCp7ZBrmLkEM2ubgeKVYMrfjJvotLQqTD-LhjbvN-yl-Og_SII3-KQwpgI1g1xQUeo1P0lXHNIo4_AQ64nPluVpAhv-cQOatC_NEFC8e2uTiLWWaY31Oge1mzpjiaQZ0bxuwWIS8nvy_ZF3yan0BYJXiKHsIJQPYoIYbgpiyPCTUsAHuikW09--um-jUZc3md5wGFkbux-pLkK1QqZHW7Cuuj1JV0d2wtCefHAgJeFJV0u0hIsFeIBUyNJEIgPWCgCqzPB9t9bYh4N8MhI-webWdAPol9la-g-Upcc0A7Gyb2EY0raEusZGS_kbLG1m_s8MWqGyst-DRacfOdpXl1-0pMrBOESO58SIt8Xe68NQG7sfwQbs02QvGiFuF2RwHokpD0D45aXcxvlh_rmG8o_54X2gi7uhEMqtYLbO-IaZ-XV_HZ7SNrdNA3v-Cg1ottZ2nwGWZxuFm2IJM5JsYTAMzK7AtKZe393pdQdo1OQHzDzo6XEycDkg2Yu8BQIsIInAGmHt3yxVPnAB5QzGnNWaHUIliwRXkeOksr_7Mt2D3lI_5-7H-CyrWfoqwbg-F4_uWDbjtUexiHph_EzUU_-xzLtH3_lzketbYMrSRAgIqd5-ubrv4HYtDGmB9LfKaz65_K0EY_P69JP1vGub8ocvKSQeWI9ipKj0T9EChNvlypDlPh5ChaV90bas4_vPTdzL-ZkAnty96Mp7oLXcSD7ioReC_JWmYRCPS9g9XoxUn_lsQ2Z6ual0Y8k4oBu9FTwi0S5xAqS6QJAtX_w3OhuKaYpyz4ZhcKHI7uH9_WOhsg",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Priority": "u=0, i",
    "Pragma": "no-cache"
}

params = {'q': f'filetype:pdf manual de programacion {lenguaje}'}
r = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
pag = soup.find_all('a', class_='fl')
for i in pag:
 paginas = f"https://www.google.com/{i.get('href')}"
 pages.append(paginas)
descargados = set(os.listdir(download)) if os.path.exists(download) else set()

for i in pages:
 r = requests.get(i, headers=headers)
 soup = BeautifulSoup(r.content, 'html.parser')
 links = soup.find_all('a', href=re.compile('.*\\.pdf'))
 for d in links:
  if n >= nf:
   input(f'\n{e}HA FINALIZADO EL SCRIPT')
   sys.exit()
  try:
   find=d['href'].find('.pdf')
   pdf=d['href']
   nx = os.path.basename(pdf).replace('%25', '_')
   nombre = f"{download}{os.path.basename(pdf).replace('%25', '_')}"
   if os.path.basename(nombre) not in descargados:
    r = requests.get(pdf, headers=headers)
    if not os.path.exists(download):
      os.makedirs(download)
    with open(nombre, 'wb') as f:
     f.write(r.content)
    descargados.add(os.path.basename(nombre))
    print(f" {e}{Fore.WHITE}{Style.BRIGHT} [{n+1}] ---> {Fore.GREEN}[DESCARGADO]")
    n += 1
  except Exception as e:
   pass
