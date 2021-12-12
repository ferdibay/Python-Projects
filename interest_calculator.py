# kullanıcıya merhaba diyoruz ve ad,tutar ve faiz oranını yazmasını istiyoruz..
print(".*.*.*.*.*Faiz Hesaplayıcıya Hoş Geldiniz*.*.*.*.*.")
ad = str(input("Lütfen Adınızı Giriniz:"))
tutar = float(input("Kredi Tutarı:"))
faiz_orani = float(input("Yıllık faiz oranı:"))

# parasının faizde kalacağı süreyi yıl ve ay olarak toplamda 2 yılı geçmeyecek şekilde ve yineleme süresini istiyoruz..
print("-> FAİZDE KALACAĞI SÜRE:")
yil = int(input("   Yıl olarak(Max 1 Yıl):"))
ay = int(input("   Ay olarak:"))
yinele = int(input("   Yineleme miktarı:"))
print("\n\n{} adlı kişinin raporu:\n".format(ad))

# toplam süreyi ve i sayacını sisteme tanıtıyoruz..
time = yil * 12 + ay
i = yinele

# faiz hesaplama fonksiyonumu yazıyor ve içine döngülerimizi atıyoruz
def print_full_report(ad, tutar, faiz_orani, yil, ay, i, time):

    # birinci döngümüzde kullanıcı 12 ay veya bir seneden az bir süre istiyorsa yineleme kadar total parasını ve aylık faiz getirisini yazdırıyoruz
    while i < 12:
        print("-------------------")
        print("Yıl:0, Ay:{}".format(i))

        # total ve aylık faizi hesaplıyoruz..
        faiz = (tutar / 100) * (faiz_orani / 12) * i
        aylik_faiz = faiz / 12

        # total ve aylık ödemeyi yazdırıyoruz
        print("toplam ödeme:", (tutar + faiz))
        print("aylık ödeme:", aylik_faiz)
        print("-------------------")

        # sayacı yinelemek istediğimiz miktar kadar arttırıyoruz..
        i = i + yinele

    # ikinci  döngümüzde kullanıcı 12 ay veya bir seneden az bir süre istiyorsa yineleme kadar total parasını ve aylık faiz getirisini yazdırıyoruz


    while 12 <= i <= time:
        print("-------------------")
        print("Yıl:{}, Ay:{}".format(1,i%12))

        # total ve aylık faizi hesaplıyoruz.
        faiz = (tutar / 100) * (faiz_orani / 12) * i
        aylik_faiz = faiz / 12

        # total ve aylık ödemeyi yazdırıyoruz
        print("toplam ödeme:", (tutar + faiz))
        print("aylık ödeme:", aylik_faiz)
        print("-------------------")

        # sayacı yinelemek istediğimiz miktar kadar arttırıyoruz..
        i = i + yinele

#fonksiyonumuzu bir değişkene atıyor ve onu print aracılığı ile bastırıyoruz..
print_full_report(ad, tutar, faiz_orani, yil, ay, i, time)


