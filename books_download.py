
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
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:109.0) Gecko/20100101 Firefox/115.0'}
params = {'q': f'filetype:pdf manual de programacion {lenguaje}'}
r = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
pag = soup.find_all('a', class_='fl')
for i in pag:
 paginas = f"https://www.google.com/{i.get('href')}"
 pages.append(paginas)
descargados = set(os.listdir(download)) if os.path.exists(download) else set()

for i in pages:
 r = requests.get(i)
 soup = BeautifulSoup(r.text, 'html.parser')
 links = soup.find_all('a', href=re.compile('.*\.pdf'))
 for d in links:
  if n >= nf:
   input(f'\n{e}HA FINALIZADO EL SCRIPT')
   sys.exit()
  try:
   pdf = d.get('href').split('&sa=')[0].split('?q=')[1].split('.pdf')[0] + '.pdf'
   nx = os.path.basename(pdf).replace('%25', '_')
   nombre = f"{download}{os.path.basename(pdf).replace('%25', '_')}"
   if os.path.basename(nombre) not in descargados:
    r = requests.get(pdf)
    if not os.path.exists(download):
      os.makedirs(download)
    with open(nombre, 'wb') as f:
     f.write(r.content)
    descargados.add(os.path.basename(nombre))
    print(f" {e}{Fore.WHITE}{Style.BRIGHT} [{n+1}] ---> {Fore.GREEN}[DESCARGADO]")
    n += 1
  except Exception as e:
   pass
