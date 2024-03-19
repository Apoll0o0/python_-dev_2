# modul_odev.py

def harf_kontrol(char):
   
    if char.isalpha():
        return True
    else:
        return False

def kücük_harf(char):
   
    return char.lower()

def harf_kullanim_sikligi(text):
   
    letter_count = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
            total_letters += 1
    
    frequency_percentage = {char: (count / total_letters) * 100 for char, count in letter_count.items()}
    return frequency_percentage
def sesli_harf(text):
    print("sesli harf sayısı: ")
    vowels = "aeiou"
    vowel_count = 0
    
    for char in text:
        if char.lower() in vowels:
            vowel_count += 1
            
    return vowel_count

def sessiz_harf(text):
    print("sessiz harf sayısı: ")
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonant_count = 0
    
    for char in text:
        if char.lower() in consonants:
            consonant_count += 1
            
    return consonant_count

def bilgi():
 
    print("Ad Soyad: [Alperen Beyhan]")
    print("Öğrenci Numarası: [211213073]")
    print("Not: [Hayatta asla arkana bakma]")
