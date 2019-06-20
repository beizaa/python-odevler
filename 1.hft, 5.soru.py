f=open("aylikmasraf.txt", "w+")
gelir= int(input("Aylik geliriniz ne kadardir?"))
mutfak= int(input("Aylik mutfak masrafiniz ne kadardir?"))
egitim= int(input("Aylik egitim masrafiniz ne kadardir?"))
giyim= int(input("Aylik giyim masrafiniz ne kadardir?"))
ulasim= int(input("Aylik ulasim masrafiniz ne kadardir?"))
aylik_toplam_masraf =int(mutfak+egitim+giyim+ulasim)
print("Aylik toplam masrafiniz", aylik_toplam_masraf, "eurodur.")
print("Aylik gider miktarinizin aylik gelirinize orani:", (aylik_toplam_masraf)/gelir, "dir.")

print(gelir, file=f)
print(mutfak, file=f)
print(egitim, file=f)
print(giyim, file=f)
print(ulasim, file=f)
print("Aylik toplam masrafiniz", mutfak+egitim+giyim+ulasim, "euro kadardir.", file=f)
print("Aylik gider miktarinizin aylik gelirinze orani:", (mutfak+egitim+giyim+ulasim)/gelir, "dir.", file=f)
f.close()





