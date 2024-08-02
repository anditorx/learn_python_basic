# Fungsi dengan Jumlah Parameter yang Tidak Diketahui
# Jika Anda tidak tahu berapa banyak argumen yang akan diterima, 
# Anda bisa menggunakan *args untuk parameter positional dan **kwargs untuk parameter keyword.

def print_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_info(1, 2, 3, a=4, b=5)
