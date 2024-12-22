import random
import string

từ = string.ascii_letters
số = string.digits
dấu = string.punctuation


def taomatkhaungaunhien(dài=10):
    printable = f'{từ}{số}{dấu}'
    
    printable = list(printable)
    random.shuffle(printable)
    
    matkhaungaunhien = random.choices(printable, k=dài)
    matkhaungaunhien = ''.join(matkhaungaunhien)
    return matkhaungaunhien

def nhapdodaimatkhau():
    dodaimatkhau = input("bạn muốn mật khẩu dài bao nhiêu ?")
    return int(dodaimatkhau)

def main():
    dodaimatkhau = nhapdodaimatkhau()
    matkhau = taomatkhaungaunhien(dodaimatkhau)
    print(matkhau)



if __name__ == '__main__':
    main()