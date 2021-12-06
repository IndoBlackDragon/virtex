# @IndoBlacDragon team

"""
[•] Ahmad Adptr
[•] Rifal 
[•] Aga
[•] Kuhaku

"""

from os import system,chdir
from time import sleep
from sys import stdout,exit

try:
    from tabulate import tabulate as tb
except:
    print ("\ninstall bahan dulu..")
    print ("tunggu sampai selesai\n")
    system("pip3 install tabulate")
    system("pkg install toilet")
    system("pkg install toilet")
    system("pkg install mpv")
    
    
def logos():
    from random import choice
    ch = ["pagga","future","script","slant","lean","shadow","smshadow","ivrit",'bubble',"digital"]
    w = ["\033[31;1m","\033[32;1m","\033[33;1m","\x1b[34;1m","\x1b[35;1m","\x1b[36;1m","\x1b[37;1m"]
    wr = choice(w)
    wrs = choice(w)
    choc = choice(ch)
    print (wr)
    system(f"figlet -f {choc} -tc Virtex 1.1")
    print (wrs)

def kenalan():
    system("mpv indoblackdragon.mp3")
    system("clear")

def anon(teks):
    for x in teks:
        stdout.write(x);stdout.flush()
        from random import uniform
        sleep(round(uniform(0.003,0.1),1))

        
class method(object):
    def __init__(self,file,txt,jmlh):
        self.file = file
        self.txt = txt
        self.jmlh = jmlh

# IBD (IndoBlacDragon)
def IBD_AHMAD(file,jumlah,teks):
    open_file = open(file,"w")
    try:
        lam = (lambda jmlh,teks:open_file.write(jmlh*f"{teks}"))
        lam(jumlah,teks)
    except OverflowError:
        print ("\n[!] Teks melebihi keganasan virtex\n[!] gagal\n");exit()
class functional(method):
    def main(self):
        IBD_AHMAD(self.file,self.jmlh,self.txt)

def _mulai():

    logos()
    print ("ＩｎｄｏＢｌａｃｋＤｒａｇｏｎ  Ｔｅａｍ\n")
    print ("[i] github: https://github.com/IndoBlackDragon")
    print ("[i] team : Indoblackdragon\n")
    print ("\033[37;3minput nama file (txt) untuk mengisi virtex\033[0m")    
    x = input("\033[32;1mfile: ")
    y = input("teks: ")
    z = int(input('limit: '))

    anon ("\n\033[37;1mTerdeteksi!\x1b[36;1m\n")

    mylist = {

        "file":[f"{x}","..."],
        "limit":[f'{z}',"..."],
        "teks":[f"{y[0:6]}..","..."]
    }

    print (tb(mylist,headers="keys",tablefmt="fancy_grid",showindex=range(1,3)))
    inp=input ("\n\033[37;1m[[ press enter ]] ")

    import re
    if re.findall(r'',inp):
        anon("\nmemulai proses..");sleep(2)
        progammer = functional(x,y,z)
        progammer.main()
        print (f"\n[\x1b[33;1m√\x1b[37;1m] berhasil membuat file {x}")
        anon("\n\nmemindahkan file ke penyimpanan internal ");sleep(1)
        system(f"mv {x} $HOME");chdir("..");system(f"mv {x} /sdcard");chdir("virtex")
        print("\n\x1b[32;1m[!] Successfully")
        print(f"\nNama virtex = {x}")

        Ahmad = open(x,"w").write(z*f"{y}")
        if Ahmad<130000:
            print (f"Tingkat bahaya = lemah")
        elif (Ahmad>130.000 and Ahmad<390000):
            print (f"Tingkat bahaya = sedang")
        elif Ahmad>390000:
            print (f"Tingkar bahaya = ganas")
        print ("\033[0m")


if __name__=="__main__":
    kenalan()
    _mulai()
    anon ("\nuntuk menggunakan virtex tersebut silahkan simak gambar berikur ini. ingat! virtex ini hanya khusus target wa");sleep(2)
    from __Indo__ import views
    views("2.jpg")
    views("3.jpg")
    views("1.jpg")    
    views("tutorial.mp4")
    print ("\n\n[[ program finished ]]\033[0m\n")
