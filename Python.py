import math

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


def Punto3(s,n):

    result=0
    try:
        n=int(n)
        for l in s:
            result+=ord(l)-96
        result=result*n
        print('Punto 3:',result)
        return True
    except:
        return False

def Punto4(s,n):

    result=1
    try:
        n=float(n)
        for l in s:
            result*=ord(l)-96
        result=math.ceil(result/n)
        print('Punto 4:',result)
        return True
    except:
        return False


def Punto5(s,n):

    try:
        n=int(n)
        if n%2==0:
            Punto3(s,n)
        else:
            Punto4(s,n)
        f=open('./c.txt')
        c=int(f.read())
        c+=1
        f.close()
        f=open('./c.txt','w')
        f.write(str(c))
        f.close()
        return True
    except ConnectionRefusedError:
        return False


def Punto6():
    # try:
    f=open('./c.txt')
    c=int(f.read())
    f.close()
    print(c)
    return True
    # except:
    return False


def ControlloEsistenzaFile():
    try:
        f=open('./c.txt')
        f.close()
        return True
    except:
        try:
            f=open('./c.txt','w')
            f.write('0')
            f.close()
            return True
        except:
            return False


ControlloEsistenzaFile()




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
            s = input('Inserisci s: ')
            n = input('Inserisci n: ')
            if not Punto2(s,n):
                print('Punto 2 rosso')
                exit()
        case 3:
            s = input('Inserisci s: ')
            n = input('Inserisci n: ')
            if not Punto3(s,n):
                print('Punto 3 rosso')
                exit()
        case 4:
            s = input('Inserisci s: ')
            n = input('Inserisci n: ')
            if not Punto4(s,n):
                print('Punto 4 rosso')
                exit()
        case 5:
            s = input('Inserisci s: ')
            n = input('Inserisci n: ')
            if not Punto5(s,n):
                print('Punto 5 rosso')
                exit()
        case 6:
            if not Punto6():
                print('Punto 6 rosso')
                exit()
        case other:
            print('Questo numero non e\' stato ancora implementato...')
except ConnectionRefusedError:
    print('Inserisci un numero consentito...')