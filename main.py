import rsa

publicKey, privateKey = rsa.newkeys(512)

def rsaEncript(frase):
     frase = rsa.encrypt(frase.encode(), publicKey)
     return frase

def rsaDecript(frase):
     frase = rsa.decrypt(frase, privateKey).decode()
     return frase


def morse(a):
    a = str(a)
    a = a.lower()
    caractere = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": " "
    }
    new_a = ''
    for letra in a:
        if letra in caractere:
            new_a += caractere[letra] + ' '
        else:
            new_a += letra + ' '
    a = new_a
    return a

def noMorse (a):
    a = str(a).lower()
    caractere = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", " ": ' ' 
    }
    morse_text = a.split(' ')
    new_a = ''
    for letra in morse_text:
        if letra in caractere:
            new_a += caractere[letra]
        else:
            pass
    a = new_a
    return a

frase = rsaEncript(input('Digita ai mermao = '))
print(frase)
print(morse(frase))
print(noMorse(frase))
print(rsaDecript(frase))



