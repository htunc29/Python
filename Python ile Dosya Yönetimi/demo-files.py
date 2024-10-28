#dosya kopyalama fonksiyonu yazınız
# def copyFile(oldFileName,newFileName):
#     with open(oldFileName,"r",encoding="utf-8") as file:
#         content=file.read()
#     with open(newFileName,"w",encoding="utf-8") as file:
#         file.write(content)
# oldFileName=input("Eski Dosya İsmi:")
# newFileName=input("Yeni Dosya İsmi:")
# copyFile(oldFileName,newFileName)



#eski dosyadaki tüm içerikleri yeni dosyaya tersten yazdırınız
# def copyFile(oldFileName,newFileName):
#     with open(oldFileName,"r",encoding="utf-8") as file:
#         content=file.read()
#     with open(newFileName,"w",encoding="utf-8") as file:
#         file.write(content[::-1])

# oldFileName=input("Eski Dosya İsmi:")
# newFileName=input("Yeni Dosya İsmi:")
# copyFile(oldFileName,newFileName)




#fonksiyona gönderilen dosya içindeki verilerin özet bilgisini hazırlayınız

def intro(fileName):
    kelimesayisi=0
    with open(fileName,"r",encoding="utf-8") as file:
        satirlar=file.readlines()
    sonuc={
        "satir_sayisi":len(satirlar),
        "kelime_sayisi":sum(len(satir.split(' ')) for satir in satirlar),
        "karakter_sayisi":sum(len(satir) for satir in satirlar)
    }
    print(f"{sonuc['satir_sayisi']} {sonuc['kelime_sayisi']} {sonuc['karakter_sayisi']}")
        
intro("msg.txt")