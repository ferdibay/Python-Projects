# gerekli time modüllerini indiriyoruz
import time
from datetime import datetime
an=datetime.now()

# hoşgeldin ekranı ile kullanıcımızı selamlıyoruz

print("***** İstinye Online Market'e Hoşgeldiniz ****")
print("Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:")
envanter = {'kuşkonmaz': 3, 'brokoli': 7, 'havuç': 5, 'elmalar': 15, 'muz':18, 'meyve': 5, 'yumurta': 4,
            'karışık meyve suyu': 19, 'balık çubukları': 10, 'dondurma': 4,
            'elma suyu': 8, 'portakal suyu': 4, 'üzüm suyu':16}
sepet=[]

# sisteme giriş için gerekli fonksiyonu yazıyoruz. kullanıcı merve adını ve 4444 şifresini girene dek sistem ondan bu bilgileri istemeye devam edecek
def sistemGiris():
    name = input("Kullanıcı adı:")
    password = int(input("Şifreniz:"))

    if name == "merve" and password == 4444:
        print("Başarıyla giriş yapıldı!")
        print(f"Hoşgeldin {name}.İlgili menü numarasını girerek aşağıdaki seçeneklerden birini seçebilirsin!")

    elif name!="merve" or password!=4444:
        print("Kullanıcı adınız ve/veya şifreniz doğru değil. Lütfen tekrar deneyin!")
        return sistemGiris()

sistemGiris()

# ürün seçimi için gerekli fonksiyonu yazıyoruz

def urunSecme():
    print("\nLütfen aşağıdaki hizmetlerden birini seçin:")
    print("1.Ürün ara")
    print("2.Sepete git ve satın al")
    print("3.Çıkış yap")
    secim=int(input("Seçiminiz:"))

# seçimin 1 olması durumunda envanter sözlüğünde belirtilen seçeneklerden biri seçilecek ve oluşturduğumuz boş listeye ürünün fiyatı adet miktarıyla çarpılarak girilecek

    # burada içecek türümüzü ve sayımızı seçiyoruz
    if secim==1:
        urun=input("\nNe arıyorsunuz(içecek/meyve): ")
        if urun=="içecek":
            print("1.üzüm suyu\n2.portakal suyu\n3.elma suyu")
            icecek=int(input("içeçek seçiminizi girin:"))
            adet=int(input("adet giriniz:"))
            if icecek==1 :
                sepet.append(envanter["üzüm suyu"]*adet)
                return urunSecme()
            elif icecek==2 :
                sepet.append(envanter["portakal suyu"]*adet)
                return urunSecme()
            elif icecek==3 :
                sepet.append(envanter["elma suyu"]*adet)
                return urunSecme()

        # burada meyve türümüzü ve sayımızı seçiyoruz
        elif urun=="meyve":

                print("1.kuşkonmaz\n2.havuç\n3.elmalar")
                meyve = int(input("meyve seçiminizi girin:"))
                adet_2=int(input("adet giriniz:"))
                if meyve == 1:
                    sepet.append(envanter["kuşkonmaz"]*adet_2)
                    return urunSecme()
                elif meyve == 2:
                    sepet.append(envanter["havuç"]*adet_2)
                    return urunSecme()
                elif meyve == 3:
                    sepet.append(envanter["elmalar"]*adet_2)
                    return urunSecme()

    # fonksiyonumuzu return ile geri çağırdık. seçimin 2 olması durumunda sepete gidiyoruz ve onaylayıp onaylamadığımızı soruyoruz
    elif secim==2:
        print("\nSepetinizdeki ürünlerin toplam fiyatı: "+str(sum(sepet))+"$")
        soru=input("sepet tutarını onaylıyor musunuz?(evet/hayır)")
        if soru=="evet":
            print("Makbuzunuz işleniyor...\n")
            time.sleep(3)
            print("Satın alma işlemi tamamlandı!\n")
            print("*"*10,"İstinye Online Market","*"*10)
            print("*"*43)
            print("\t\t0850 283 6000\n\t\tistinye.edu.tr\n")
            print("-"*10)
            print(f"Toplam alışveriş: {sum(sepet)}$")
            print("-" * 10)
            print("Tarih:"+str(an.date())+" "+str(an.hour)+":"+str(an.minute))
            print("Online Market'imizi kullandığınız için teşekkür ederiz!\n")

            return urunSecme()
        if soru=="hayır":
            return urunSecme()

    # fonksiyonumuzu return ile tekrar geri çağırdık. seçimin 3 olması durumunda programımızı sonlandırıyoruz
    elif secim==3 :
        print("\nSistemden çıkışınız yapılıyor.Lütfen bekleyiniz!\n")
        time.sleep(3)
        print("Tekrar bekleriz...")
        return 0

urunSecme()










