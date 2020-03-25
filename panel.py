from data import flask_server
import flask,os,platform,sys
sistem = platform.system()
isim = os.getlogin()
if sistem == "Windows" and int(platform.uname().release) < 10:
    print("\n\tRenk kodlarını desteklemeyen sistem kullanıyorsunuz . Renkler devre dışı bırakıldı !")
    kirmizi = yesil = sari = mavi = pembe = camgoz = normal = ""
else:
    kirmizi , yesil , sari , mavi , pembe , camgoz , normal = "\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m","\033[0m"
def slogan():
    print("""
    ▄▄▄▄·  ▄· ▄▌▄▄▄▄▄▄▄▄ .·▄▄▄▄   ▄▄▄· ▄▄▄▄▄ ▄▄▄· 
    ▐█ ▀█▪▐█▪██▌•██  ▀▄.▀·██▪ ██ ▐█ ▀█ •██  ▐█ ▀█ 
    ▐█▀▀█▄▐█▌▐█▪ ▐█.▪▐▀▀▪▄▐█· ▐█▌▄█▀▀█  ▐█.▪▄█▀▀█ 
    ██▄▪▐█ ▐█▀·. ▐█▌·▐█▄▄▌██. ██ ▐█ ▪▐▌ ▐█▌·▐█ ▪▐▌
    ·▀▀▀▀   ▀ •  ▀▀▀  ▀▀▀ ▀▀▀▀▀•  ▀  ▀  ▀▀▀  ▀  ▀ 
                            ByteData  P A N E L ~ 
    """)
def ts():
    temizle()
    slogan()
if sistem == "Windows":
    def temizle():
        os.system("cls")
else:
    def temizle():
        os.system("clear")
ts()
try:flask_server.flask_start(os,flask,kirmizi,yesil,normal)
except KeyboardInterrupt:
    if input(kirmizi+"\tÇıkmak Istermisin ?"+normal+f"\n\tÇıkış yaptığın takdirde ngrok çalışmaya devam edecek lakin flask çalışmayı durduracaktır !\n\n\t[{isim}] [ {yesil}E{normal} | {kirmizi}H{normal} ] : ").strip().lower() == "h":
        sys.exit()
