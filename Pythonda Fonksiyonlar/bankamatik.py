SadıkHesap={
    'ad':'Hüseyin Tunç',
    'hesapNo':'12321313',
    'bakiye':3000,
    'ekHesap':2000
}
AliHesap={
    'ad':'Ali Tunç',
    'hesapNo':'12321313',
    'bakiye':3000,
    'ekHesap':1000
}
def ParaCek(hesap,cekilecektutar):
    if(hesap['bakiye']<cekilecektutar):
        ekHesapKullanılsınmı=input("Bakiye yetersiz ek Hesap Kullanılsın mı(evet,hayır) ?").lower()
        if(ekHesapKullanılsınmı=="evet"):
            if(hesap['bakiye']+hesap['ekHesap']<cekilecektutar):
                print("Üzgünüz limitiniz yetmiyor")
            else:
                hesap.update({'bakiye':0,'ekHesap':hesap['ekHesap']-(cekilecektutar-hesap['bakiye'])})
                print("Para Çekme İşlemi Başarılı")
                print(hesap)
        else:
            print("İşlem İptal Edildi")
    else:
        hesap.update({'bakiye':hesap['bakiye']-cekilecektutar})
        print(hesap)
ParaCek(SadıkHesap,2600)