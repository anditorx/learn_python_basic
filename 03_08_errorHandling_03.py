class ValueToSmallError(Exception):
    pass

class ValueToLargeError(Exception):
    pass

number = 10

while True:
    try:
        i_num = int(input("Masukkan angka: "))
        
        if i_num < number:
            raise ValueToSmallError
        elif i_num > number:
            raise ValueToLargeError
        break
    
    except ValueToSmallError:
        print("error: angka yang kamu input terlalu kecil, coba lagi!")
        print()
    except ValueToLargeError:
        print("error: angka yang kamu input terlalu besar, coba lagi!")
        print()
    
    print("Benar! Kamu berhasi menebak angka dengan tepat.")
        