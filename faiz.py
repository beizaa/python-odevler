f= open("faizHesaplama.txt", "w+")
anaPara= int(input("Ana para miktari nedir?"))
faizSuresi= int(input("Ne kadar sure ile(yil) parayi alacaksiniz?"))
faizOrani= int(input("Faiz orani nedir(yillik)?"))
print("Toplam faiz tutari:", anaPara*faizSuresi*faizOrani/100, "dir.")
print("Aylik ortalama faiz tutari:", anaPara*faizOrani/(100*12), "dir.")
print("Gunluk ortalama fazi tutari:", anaPara*faizOrani/(100*365), "tir.")
print("Toplam para miktari:", anaPara+(anaPara*faizSuresi*faizOrani/100), "dir.")

print(anaPara, file=f)
print(faizSuresi, file=f)
print(faizOrani, file=f)

print("Toplam faiz tutari:", anaPara*faizSuresi*faizOrani/100, "dir.", file=f)
print("Aylik ortalama faiz tutari:", anaPara*faizOrani/(100*12), "dir.", file=f)
print("Gunluk ortalama fazi tutari:", anaPara*faizOrani/(100*365), "tir.", file=f)
print("Toplam para miktari:", anaPara+(anaPara*faizSuresi*faizOrani/100),"dir.", file=f)
f.close()


