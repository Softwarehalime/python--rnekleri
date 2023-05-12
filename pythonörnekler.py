


if __name__=='__main__':
   print("hello")
    #print("MERHABA HALİMENUR ......")
'''sayi=input("bir sayı girin: ")
toplam=0 
carpım=1
for rakam in sayi:
    toplam+=int(rakam)
    carpım*=int(rakam)
print("sayının rakamları toplamı: ",toplam)
print("sayının rakamları carpımı: ",carpım)'''

    #metin=input("bir isim girin: " )
    #print((metin+"\n")*10) #girilen metni 10 kere tekrar eden satır sadece pythonda var bu * özelliği 

sayılar=[10,11,12,13,14,15,16,17,18,19,20]
#for sayi in sayılar:
    #if sayi % 2==0:
        #print(sayi) #listedek çift sayıları yazdırır
sayılar2=[21,22,23,24,25]
birlestir=sayılar + sayılar2 #iki listeyi bitleştirir
print(birlestir)
for sayi in birlestir:
     if sayi % 2==0:
        print(sayi)
     
            


'''hafta_ici=["pazartesi","salı","carsamba","persembe","cuma"]
    print=("cuma" in hafta_ici) #cuma elamanının hafta ici listesinde olup olmadıgnı kontrol eder
    print=("cumartesi" in hafta_ici)'''

    

'''print("ekrana liste halinde meyve adlarını yazan program")
     meyveler=["elma","armut","mandalina"]
     print(" meyveler listesi:{}".format(meyveler))
     liste=[3.14,7,89,"pırasa","3 elma",6]
     print(liste)
     print(meyveler)
     print(liste[3]) #listenin 3.indeksini ekrana yazdırır
     liste[3]='armut' #listenin 3.indeksimdeki elemanı degistirir yani pırasa yerine armut gelecek
     liste[2]=54 #2.indeksteki elemanı degistrir
     print(liste)'''

    


'''def dikdortgenalan(genislik,yukseklık):
        alan =float(genislik)*float(yukseklık)
        print("alan: ",alan)
        return alan
    gen= input('genişlik :')
    yuk= input('yukseklık. ')
    dikdortgenalan(gen,yuk)'''

''' print("sinema tiyatro bileti alan ögrenciye %50 indirim yapan program")
    secim=input(' sinema ise 1 ,tiyatro için 2 tusaynız: ')
    ogrenci=input('örencimsiniz evet ise E,degiiseniz H seciniz: ')
    ucret=0
    #indirimsiz ücret
    if secim=='1':
        ucret=20
    else :
        ucret=30
    #indirimli fyat
    if ogrenci=='E':
        ucret=ucret/2
    else:
        ucret=ucret
    print("odemeniz gereken tutar= {0}".format(ucret))'''

''' print("kenarları girilen dikdorgenin alanı ve caevresi")
    kıkenar=input('kısa kenarı giriniz: ')
    uzkenar=input('uzun kenarı giriniz: ')
    cevre= 2*(int(kıkenar)+int(uzkenar))
    alan= int(kıkenar)*int(uzkenar)
    print("dikdörtgenin alanı= {0}".format(alan))
    print("dkdortgenin cevresi= {0}".format(cevre))'''


'''    print("1 ile 20 arasındaki cift sayıları yazan program")
    for i in range(1,21):
        if(i % 2== 0):
            print(i) '''


''' isim =input("adınızı yazınız:")
    sayac =0
    while sayac < len(isim):
        print (isim[sayac])
        sayac+=1
    else:
        print ("adlarınız harfleri listelendi")'''


    
''' print("VÜCUT ENDEKSİ HESPLAMA PRGRAMINA HOSGEDNİZ")
    kilo=int(input("kilonuzu giriniz: "))
    boy=float(input("boyunuzu irinz: "))

    endeks=kilo/boy*boy
    if endeks <= 18:
        print("\n zayıf {}".format(endeks))
    elif endeks>18 and endeks <=25:
        print("\n kilolu{}".format(endeks))
    elif endeks>25 and endeks<=30:
       print("\n obez{}".format(endeks))
    elif endeks>30:
         print("\n aşırı aşırı obez{}".format(endeks))'''
'''
    yas=int(input("suanki yasınızı giriniz:"))
    print(yas)
    yil=100-yas
    yeniyas=2022+yil
    print("yuz yasınıza bu yılda gireceksiniz:)",yeniyas)'''

'''print("dairenin alanını hesaplama")
    r=int(input("dairenin yaricapini giriniz:"))
    alan =3*r*r
    print("dairenin alani.",alan)'''

'''print("basamak sayısını bulma.")
    sayi=int(input("bir sayi giriniz:"))
    if(sayi < 0):
        print("girdiginiz sayi negatiftir")
    elif(sayi > 0):
        print("girdiginiz sayi pozitiftir")
    ysayi=str(sayi)
    for index,i ,in enumerate(ysayi):
        print(index,i)'''

'''print("liste ortalaması:")
    liste=[]
    for i in range(10):
        sayi=int(input("eklemek istediginiz elemanı giriniz:"))
        liste.append(sayi)
    print(liste)
    ntane=0
    ptane=0
    tane=0
    ptop=0
    ntop=0
    for i in liste:

        if(i < 0):
            ntop=ntop+i
            ntane=ntane+1
        elif(i > 0):
            ptop=ptop+i
            ptane=ptane+1
        
    print("listedeki negatif sayilarin ortalamasi:",ntop/ntane)
    print("listedeki pozitif sayilarin ortalamasi:",ptop/ptane)
'''
'''
    liste=[2,4,8,5,1,4]
    yeni=[]
    yeni=liste
    print(liste)
    print("kopya",yeni)
'''
