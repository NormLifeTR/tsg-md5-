#-*- coding: utf-8 -*-
import hashlib
print("""
             TSG-TİM MD5 ŞİFRE KIRMA PROGRAMINA HOŞGELDİNİZ 
--------------------------------------------------------------------------------
                              NormLifeTR 
""")
md5 = raw_input("Kırılıcak şifreyi giriniz   : ")
wordlist = open("wordlist.txt" , "r").readlines()
for kelime in wordlist:
    kelime = kelime.strip()
    kir = hashlib.md5(kelime).hexdigest()
    if kir == md5:
        print("Md5 Şifresi başarıyla kırıldı : " + kelime) 
        break
    else:
        print("şifre kırma başarısız")
    
    
