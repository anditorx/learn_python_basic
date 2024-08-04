try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except Exception as e:
    print ("error: ", e.__class__,".")
    
print("")
print("---")
print("")

try:
    nilai = "10"
    pembagi = 0
    hasil = nilai/pembagi
except ZeroDivisionError:
    print("error: Terjadi ZeroDivisionError")
except ValueError:
    print("error: Terjadi ValueError")
except Exception:
    print("error: Terjadi error yang tidak dikenali")
    

    
print("")
print("---")
print("")