def Punto1(s,n):
    
    word = ""
    try:
        n=int(n)
        for l in s:
            word += chr(ord(l)+n)

        print('Punto 1:',s,word)
        return True
    except:
        return False

def Punto2(s,n):

    word = ""
    try:
        n=int(n)
        for l in s:
            word += chr(ord(l)-n)

        print('Punto 1:',s,word)
        return True
    except:
        return False

try:
    punto=int(input('Quale punto vuoi eseguire: '))

    match punto:
        case 1:
            s = input('Inserisci s: ')
            n = input('Inserisci n: ')
            if not Punto1(s,n):
                print('Punto 1 rosso')
                exit()
        case 2:
            if not Punto2(s,n):
                s = input('Inserisci s: ')
                n = input('Inserisci n: ')
                print('Punto 2 rosso')
                exit()
except:
    print('Inserisci un numero consentito...')