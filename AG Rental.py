

data = [
        {"Nama mobil":"INNOVA", "Tipe mobil" : "MPV", "Plat nomor" : "D 1283 AUG", "Price": 850000, "Tanggal": "02/05/25"},
        {"Nama mobil":"INNOVA", "Tipe mobil" : "MPV", "Plat nomor" : "D 417 ANG", "Price":  500000, "Tanggal": "02/05/25"},
        {"Nama mobil":"XPANDER", "Tipe mobil" : "MPV", "Plat nomor" : "D 1354 ADD", "Price": 475000, "Tanggal": "02/05/25"},
        {"Nama mobil":"FORTUNER", "Tipe mobil" : "SUV", "Plat nomor" : "D 2186 ABH", "Price": 475000, "Tanggal": "02/05/25"},
        {"Nama mobil":"PAJERO", "Tipe mobil" : "SUV", "Plat nomor" : "D 1342 PKM", "Price": 475000, "Tanggal": "02/05/25"},
        {"Nama mobil":"CRV", "Tipe mobil" : "SUV", "Plat nomor" : "D 1832 FTH", "Price": 475000, "Tanggal": "02/05/25"},
        {"Nama mobil":"CRV", "Tipe mobil" : "SUV", "Plat nomor" : "D 1982 KJI", "Price": 475000, "Tanggal": "02/05/25"},
        {"Nama mobil":"PALISADE", "Tipe mobil" : "SUV", "Plat nomor" : "D 1879 AJT", "Price": 475000, "Tanggal": "02/05/25"},
        {"Nama mobil":"STARGAZER", "Tipe mobil" : "MPV", "Plat nomor" : "D 182 AJR", "Price": 475000, "Tanggal": "02/10/25"},
        {"Nama mobil":"INNOVA", "Tipe mobil" : "MPV", "Plat nomor" : "D 44 YBA", "Price": 725000, "Tanggal": "02/08/25"}]


def input_angka(prompt,type):
    while True:
        if type == 'Menu':
            try:
                return int(input(prompt))
            except:
                print("Input harus berupa angka\n")
                break
        elif type == 'Angkaharus':
            try:
                return int(input(prompt))
            except:
                print("Input harus berupa angka\n")
        elif type == 'Angka':
            try:
                return int(input(prompt))
            except:
                print("Input harus berupa angka\n")
                return False


def input_huruf(prompt):
    while True:
        kata = input(prompt)
        if kata.isalpha():
            return kata
        else:
            print("Input harus berupa huruf\n")


def input_plat(prompt,type):
    while True:
        kata = input(prompt)
        kata = kata.upper()
        j = list(kata.split(' '))
        pelat = 0
        for i in type:
            if i["Plat nomor"] == kata:
                pelat = 1
        if pelat == 1:
            print("Plat mobil sudah terdaftar")
            return False
        else:
            if len(j) < 2 or len(j) > 3 or not kata:
                print("Input plat nomor tidak sesuai")
                return False
            else:
                if (len(j) == 2) and (1 <= int(len(j[0])) <= 2) and (1 <= int(len(j[1])) <= 4) :
                    if j[0].isalpha() and j[1].isnumeric() :
                        if int(j[1][0]) == 0:
                            print("Input plat nomor tidak sesuai")
                            return False
                        else :
                            return kata.upper()                              
                    else: 
                        print("Input plat nomor tidak sesuai")
                        return False
                elif (len(j) == 3) and (1 <= int(len(j[0])) <= 2) and (1 <= int(len(j[1])) <= 4) and (0 <= int(len(j[2])) <= 3) :
                    if j[0].isalpha() and j[1].isnumeric() and j[2].isalpha():
                        if int(j[1][0]) == 0:
                            print("Input plat nomor tidak sesuai")
                            return False
                        else:
                            return kata.upper()  
                    else: 
                        print("Input plat nomor tidak sesuai")
                        return False
                else :
                    print("Input plat nomor tidak sesuai")
                    return False


def input_tanggal(prompt):
    while True:
        kata = input(prompt)
        if not kata:
            print('Tanggal tidak boleh kosong')
            return False
        else:
            j = list(kata.split('/'))
            if len(j) == 3 and j[0].isnumeric() and j[1].isnumeric() and j[2].isnumeric() and 0<len(j[0])<3 and 0<len(j[1])<3 and 0<len(j[2])<3 and 0<int(j[0])<13 and 0<int(j[1])<31 and 0<int(j[2])<100:
                if len(j[0])==1:
                    j[0] = '0'+j[0]
                if len(j[1])==1:
                    j[1] = '0'+j[1]
                if len(j[2])==1:
                    j[2] = '0'+j[2]
                ts = j[0]+'/'+j[1]+'/'+j[2]
                return ts
            else :
                print("Input Tanggal (M/D/Y) tidak sesuai")
                return False


def input_yakin(prompt):
    while True:
        kata = input(prompt).capitalize()
        if kata.isalpha() and (kata == "Ya" or kata == "Tidak"):
            return kata.capitalize()
        else:
            print("Input harus berupa Ya atau Tidak\n")


def Tanggal(d,m,y):
    
    y = y+(d//365)       
    if d %30 == 0:
        m = m
    else:
        m = m+(d//30)       
    if d %30 == 0:
        d = 30
    else:
        d = d%30            
    
    kata = f'{m}/{d}/{y}'
    j = list(kata.split('/'))
    
    if len(j[0])==1:
        j[0] = '0'+j[0]
    if len(j[1])==1:
        j[1] = '0'+j[1]
    if len(j[2])==1:
        j[2] = '0'+j[2]
    ts = f"{j[0]}/{j[1]}/{j[2]}"
    return ts


def cari_huruf(prompt,bagian,type):
    while True:
        kata = input(prompt).upper()
        if not kata:
            print(f"input {bagian} tidak boleh kosong")
            return False
        else:
            if kata.isalpha():
                ada_nama = False  
                for i in type:
                    if kata == i[bagian]:
                        ada_nama = True
                        break  
                if ada_nama:
                    return kata  
                else:
                    print(f"{bagian} tidak ditemukan")
                    return False
            else:
                print("Input harus berupa huruf\n")
                return False


def cari_plat(prompt, type):
    while True:
        kata = input(prompt).upper()
        if not kata :
            print("Input Plat tidak boleh kosong")
            return False
        else:
            j = list(kata.split(' '))
            if len(j) <2 or len(j) >3 or not kata:
                print("Input plat nomor tidak sesuai")
                return False
            else:
                if (len(j) == 2) and (1 <= int(len(j[0])) <= 2) and (1 <= int(len(j[1])) <= 4) :
                    if j[0].isalpha() and j[1].isnumeric() :
                        if int(j[1][0]) == 0:
                            print("Input plat nomor tidak sesuai")
                            return False
                        else:
                            ada_plat = False
                            for i in type: 
                                if kata == i["Plat nomor"]:
                                    ada_plat = True
                                    break  
                            if ada_plat:
                                return kata  
                            else:
                                print("Plat nomor kendaraan tidak ditemukan")
                                return False
                    else: 
                        print("Input plat nomor tidak sesuai")
                        return False
                        
                elif (len(j) == 3) and (1 <= int(len(j[0])) <= 2) and (1 <= int(len(j[1])) <= 4) and (0 <= int(len(j[2])) <= 3) :
                    if j[0].isalpha() and j[1].isnumeric() and j[2].isalpha():
                        if int(j[1][0]) == 0:
                            print("Input plat nomor tidak sesuai")
                            return False
                        else:
                            ada_plat = False
                            for i in type:
                                if kata == i["Plat nomor"]:
                                    ada_plat = True
                                    break  
                            if ada_plat:
                                return kata  
                            else:
                                print("Plat nomor kendaraan tidak ditemukan")
                                return False
                    else: 
                        print("Input plat nomor tidak sesuai")
                        return False
                else :
                    print("Input plat nomor tidak sesuai")
                    return False
            

def cari_tanggal_sewa(prompt,plat,type):
    while True:
        kata = input(prompt)
        if not kata:
            print('Tanggal tidak boleh kosong')
            return False

        elif '/' in kata:
            j = list(kata.split('/'))
            

            if len(j) == 3 and j[0].isnumeric() and j[1].isnumeric() and j[2].isnumeric()  and 0<len(j[0])<3 and 0<len(j[1])<3 and 0<len(j[2])<3 and 0<int(j[0])<13 and 0<int(j[1])<31 and 0<int(j[2])<100 :
                k = list(map(int, kata.split('/')))
                if len(j[0])==1:
                    j[0] = '0'+j[0]
                if len(j[1])==1:
                    j[1] = '0'+j[1]
                if len(j[2])==1:
                    j[2] = '0'+j[2]
                ts = f"{j[0]}/{j[1]}/{j[2]}"
                
                for i in type:
                    if i["Plat nomor"] == plat:
                        t = list(map(int, i["Tanggal"].split('/')))
                        if (k[2] < t[2]) or (k[0] < t[0] and k[2] == t[2]) or (k[1]<t[1] and k[0] == t[0] and k[2] == t[2]):
                            print(f"Tanggal {ts} tidak valid, kendaraan tersedia pada {i['Tanggal']}.")
                            return False
                return ts  

            else :
                print("Input Tanggal (M/D/Y) tidak sesuai")
                return False
        else :
            print("Input Tanggal (M/D/Y) tidak sesuai")
            return False


def Mainmenu():
    print("""\n\t\t=========================================================================\n\t\t|*|\t\t\t\t\t\t\t\t      |*|
        \t|*|\t\t\tSelamat Datang di RENTALS\t\t      |*|
        \t|*|\t\t\t\t\t\t\t\t      |*|
        \t|*|\t\t List Menu :\t\t\t\t\t      |*|
        \t|*|\t\t 1. Daftar Kendaraan\t\t\t\t      |*|
        \t|*|\t\t 2. Tambah Kendaraan\t\t\t\t      |*|
        \t|*|\t\t 3. Hapus Kendaraan\t\t\t\t      |*|
        \t|*|\t\t 4. Update Kendaraan\t\t\t\t      |*|
        \t|*|\t\t 5. Sewa Kendaraan\t\t\t\t      |*|
        \t|*|\t\t 6. Exit Program\t\t\t\t      |*|
        \t|*|\t\t\t\t\t\t\t\t      |*|\n\t\t=========================================================================
        """)


def daftar_data():
    from tabulate import tabulate  
    print(tabulate(data, headers="keys", tablefmt= 'grid'))
    print()


def daftar():
    menu_daftar = 0
    while menu_daftar != 7:
        print("""\n\t\t\t\t
        \t\t\t    List Menu pada Daftar :
              
        \t\t\t    1. Daftar Kendaraan Seluruhnya
        \t\t\t    2. Cari Nama Kendaraan
        \t\t\t    3. Cari Tipe Kendaraan
        \t\t\t    4. Cari Plat Kendaraan
        \t\t\t    5. Cari Harga Kendaraan
        \t\t\t    6. Cari Tanggal Kendaraan
        \t\t\t    7. Kembali ke Menu Utama
    
        """)
        
        menu_daftar = input_angka("Masukkan angka Menu yang ingin dijalankan : ","Menu")
        print()

        if menu_daftar == 1:
            if data != []:
                daftar_data()
            else:
                print("Daftar data kosong")
            
        
        elif menu_daftar == 2:
            while True:
                if data != []:
                    list_nama = []
                    nama_sort = cari_huruf("Masukkan nama mobil : ","Nama mobil",data)
                    if nama_sort == False:
                        break
                    else:
                        for i in data:
                            if i["Nama mobil"] == nama_sort :
                                list_nama.append(i)
                        if list_nama==[]:
                            print("Tidak ada mobil dengan nama tersebut")
                        
                        from tabulate import tabulate 
                        print(tabulate(list_nama, headers="keys", tablefmt= 'grid'))
                        print()
                        break
                else:
                    print("Daftar data kosong")

        elif menu_daftar == 3:
            while True:    
                if data != []:
                    list_tipe = []
                    tipe_sort = cari_huruf("Masukkan tipe mobil : ","Tipe mobil",data)
                    if tipe_sort == False:
                        break
                    else:
                        for i in data:
                            if i["Tipe mobil"] == tipe_sort :
                                list_tipe.append(i)
                        if list_tipe==[]:
                            print("Tidak ada mobil dengan tipe tersebut")
                        
                        from tabulate import tabulate 
                        print(tabulate(list_tipe, headers="keys", tablefmt= 'grid'))
                        print()
                        break
                else:
                    print("Daftar data kosong")

        elif menu_daftar == 4:
            while True:    
                if data != []:
                    list_plat = []
                    plat_sort = cari_plat("Masukkan plat nomor mobil (XX #### XXX) : ",data)
                    if plat_sort == False:
                        break
                    else: 
                        for i in data:
                            if i["Plat nomor"] == plat_sort :
                                list_plat.append(i)
                        if list_plat==[]:
                            print("Tidak ada mobil dengan plat tersebut")
                        
                        from tabulate import tabulate 
                        print(tabulate(list_plat, headers="keys", tablefmt= 'grid'))
                        print()
                        break
                else:
                    print("Daftar data kosong")

        elif menu_daftar == 5:
            while True:
                if data != []:
                    list_harga = []
                    harga_sort = input_angka("Masukkan budget sewa mobil anda : ","Angka")
                    if harga_sort == False:
                        break
                    else:
                        for i in data:
                            if i["Price"] <= harga_sort :
                                list_harga.append(i)
                        if list_harga==[]:
                            print("Tidak ada mobil dibawah harga tersebut")
                        
                        from tabulate import tabulate 
                        print(tabulate(list_harga, headers="keys", tablefmt= 'grid'))
                        print()
                        break
                else:
                    print("Daftar data kosong")

        elif menu_daftar == 6:
            while True:
                if data != []:
                    list_tanggal = []
                    tanggal_sort = input_tanggal("Masukkan tanggal sewa (M/D/Y) : ")
                    if tanggal_sort == False:
                        break
                    else:
                        k = list(map(int, tanggal_sort.split('/')))
                        for i in data:
                            t = list(map(int, i["Tanggal"].split('/')))
                            if (k[2] > t[2]) or (k[0] > t[0] and k[2] == t[2]) or (k[1]>=t[1] and k[0] == t[0] and k[2] == t[2]) :
                                list_tanggal.append(i)
                        if list_tanggal == []:
                            print("Tidak ada mobil dibawah tanggal tersebut")
                        
                        from tabulate import tabulate 
                        print(tabulate(list_tanggal, headers="keys", tablefmt= 'grid'))
                        print()
                        break

                else:
                    print("Daftar data kosong")

        elif menu_daftar == 7:
            break
        else :
            print("Value tidak valid, coba lagi")
            
    
def nambah():
    menu_nambah = 0
    while menu_nambah != 2:
        print("""\n\t\t\t\t
        \t\t\t    List Menu Tambah :
              
        \t\t\t    1. Tambah kendaraan
        \t\t\t    2. Kembali ke Menu Utama 

              """)
        menu_nambah = input_angka("Masukkan angka Menu Tambah yang ingin dijalankan : ","Menu")
        if menu_nambah == 1:
            while True:        
                ds = []
                dict_tambah = {"Nama mobil":"Elgrand", "Tipe mobil" : "MPV", "Plat nomor" : "D 44 YBA", "Price": 725000, "Tanggal": "hehe"}
                plat_mobil = input_plat("Masukkan Plat Nomor (XX #### XXX) : ", data)
                if plat_mobil == False:
                    break
                else:
                    nama_mobil = input_huruf("Masukkan Nama Mobil : ")
                    tipe_mobil = input_huruf("Masukkan Tipe Mobil : ")
                    harga = input_angka("Masukkan Harga sewa : ","Angkaharus")
                    tanggal_mobil = input_tanggal("Masukkan tanggal ketersediaan mobil (M/D/Y) :")
                    if tanggal_mobil == False:
                        break
                    else:
                        dict_tambah["Nama mobil"] = nama_mobil.upper()
                        dict_tambah["Tipe mobil"] = tipe_mobil.upper()
                        dict_tambah["Plat nomor"] = plat_mobil
                        dict_tambah["Price"] = harga
                        dict_tambah["Tanggal"] = tanggal_mobil
                ds.append(dict_tambah)
                from tabulate import tabulate  
                print(tabulate(ds, headers="keys", tablefmt= 'grid'))
                print()
                
                yakin = input_yakin("Apakah ingin lanjut untuk menyimpan data? (Ya/Tidak)\n")
                if yakin.capitalize() == "Ya":
                    data.append(dict_tambah)
                    print("\nData berhasil disimpan\n") 
                    break         
                elif yakin.capitalize() == "Tidak":
                    print("\nPenembahan data dibatalkan\n")
                    break
        elif menu_nambah==2:
            break
        else :
            print("Value tidak valid, coba lagi")

        
        
def Hapus():
    menu_hapus = 0
    while menu_hapus!=4:
        print("""\n\t\t\t\t
        \t\t\t    List Menu Hapus :
              
        \t\t\t    1. Hapus kendaraan berdasarkan Plat nomor (primary Key)
        \t\t\t    2. Hapus berdasarkan nama kendaraan
        \t\t\t    3. Hapus berdasarkan Tipe kendaraan
        \t\t\t    4. Kembali ke Menu Utama

              """)
        menu_hapus = input_angka("Masukkan angka Menu Hapus yang ingin dijalankan : ","Menu")

        if menu_hapus == 1:
            while True:
                daftar_data()
                hapus_platmobil = cari_plat("Masukkan Plat nomor yang ingin dihapus (XX #### XXX) : ", data)
                if hapus_platmobil == False:
                    break
                else:
                    for item in data:
                        if item["Plat nomor"] == hapus_platmobil:
                            print(item)
                            yakin = input_yakin("Apakah ingin lanjut untuk menghapus data? (Ya/Tidak)\n")
                            if yakin.capitalize() == "Ya":
                                data.remove(item)
                                print("\nData berhasil dihapus\n")
                                break          
                            elif yakin.capitalize() == "Tidak":
                                print("Penghapusan data dibatalkan")
                                break
                    break
        elif menu_hapus == 2:
            list_nama = []
            while True:
                daftar_data()
                hapus_namamobil = cari_huruf("Masukkan nama kendaraan yang ingin dihapus : ","Nama mobil",data)
                if hapus_namamobil == False:
                    break
                else:
                    for item in data:
                        if item["Nama mobil"] == hapus_namamobil:
                            list_nama.append(item)
                    from tabulate import tabulate 
                    print(tabulate(list_nama, headers="keys", tablefmt= 'grid'))
                    print()
                    yakin = input_yakin("Apakah ingin lanjut untuk menghapus data? (Ya/Tidak)\n")
                    if yakin.capitalize() == "Ya":
                        for i in range(len(list_nama)):
                            data.remove(list_nama[i])
                        print("\nData berhasil dihapus\n") 
                        break         
                    elif yakin.capitalize() == "Tidak":
                        print("Penghapusan data dibatalkan")
                        break
        elif menu_hapus == 3:
            list_tipe = []
            while True:
                daftar_data()
                hapus_tipemobil = cari_huruf("Masukkan tipe kendaraan yang ingin dihapus : ",'Tipe mobil',data)
                if hapus_tipemobil == False:
                    break
                else :
                    for item in data:
                        if item["Tipe mobil"] == hapus_tipemobil:
                            list_tipe.append(item)
                    from tabulate import tabulate 
                    print(tabulate(list_tipe, headers="keys", tablefmt= 'grid'))
                    print()
                    yakin = input_yakin("Apakah ingin lanjut untuk menghapus data? (Ya/Tidak)\n")
                    if yakin.capitalize() == "Ya":
                        for i in range(len(list_tipe)):
                            data.remove(list_tipe[i])
                        print("\nData berhasil dihapus\n")
                        break          
                    elif yakin.capitalize() == "Tidak":
                        print("Penghapusan data dibatalkan")
                        break
        elif menu_hapus == 4:
            break
        else:print("Value tidak valid, coba lagi")


def Update():
    menu_update = 0
    while menu_update != 2:
        print("""\n\t\t\t\t
        \t\t\t    List Menu Update :
              
        \t\t\t    1. Ubah data kendaraan
        \t\t\t    2. Kembali ke Menu Utama 

              """)
        menu_update = input_angka("Masukkan angka Menu Update yang ingin dijalankan : ","Menu")
        update = 0
        if menu_update == 1:
            while True:
                if update==1:
                    break
                daftar_data()
                up_plat = cari_plat("Masukkan Plat nomor kendaraan yang ingin diedit (XX #### XXX) : ",data)
                if up_plat == False:
                    break
                else:
                    menu_ubah = 0
                    while menu_ubah != 5:
                            if update==1:
                                break
                            print("""\n\t\t\t\t
                        \t\t\t    Pilihan data apa yang akan diubah :
                            
                        \t\t\t    1. Ubah Nama kendaraan
                        \t\t\t    2. Ubah Tipe kendaraan
                        \t\t\t    3. Ubah Harga kendaraan
                        \t\t\t    4. Ubah Tanggal kendaraan 
                        \t\t\t    5. Tidak jadi mengubah data
                                  

                            """)
                            menu_ubah = input_angka("Masukkan angka Menu Ubah yang ingin dijalankan : ","Menu")
                            
                            if menu_ubah == 1:
                                nama_mobil = input_huruf("Masukkan Nama pengganti : ").upper()
                                yakin = input_yakin("Lanjut untuk mengganti nama? (Ya/Tidak)\n")
                                if yakin.capitalize() == "Ya":
                                    for i in data:
                                        if i["Plat nomor"] == up_plat:
                                            i["Nama mobil"] = nama_mobil
                                            print("\nData berhasil diubah\n")
                                            update=1
                                            break
                                elif yakin.capitalize() == "Tidak":
                                    print("Penggantian data dibatalkan")
                                    update=1
                                    break

                            elif menu_ubah == 2:
                                tipe_mobil = input_huruf("Masukkan Tipe pengganti : ").upper()
                                yakin = input_yakin("Lanjut untuk mengganti tipe mobil? (Ya/Tidak)\n")
                                if yakin.capitalize() == "Ya":
                                    for i in data:
                                        if i["Plat nomor"] == up_plat:
                                            i["Tipe mobil"] = tipe_mobil
                                            print("\nData berhasil diubah\n")
                                            update=1
                                            break
                                elif yakin.capitalize() == "Tidak":
                                    print("Penggantian data dibatalkan")
                                    update=1
                                    break

                            elif menu_ubah == 3:
                                harga_mobil = input_angka("Masukkan Harga pengganti : ","Angkaharus")
                                yakin = input_yakin("Lanjut untuk mengganti harga? (Ya/Tidak)\n")
                                if yakin.capitalize() == "Ya":
                                    for i in data:
                                        if i["Plat nomor"] == up_plat:
                                            i["Price"] = harga_mobil
                                            print("\nData berhasil diubah\n")
                                            update=1
                                            break
                                elif yakin.capitalize() == "Tidak":
                                    print("Penggantian data dibatalkan")
                                    update=1
                                    break

                            elif menu_ubah == 4:
                                tanggal_mobil = input_tanggal("Masukkan Tanggal pengganti (M/D/Y) : ")
                                if tanggal_mobil == False:
                                    update=1
                                    break
                                else:
                                    yakin = input_yakin("Lanjut untuk mengganti tanggal? (Ya/Tidak)\n")
                                    if yakin.capitalize() == "Ya":
                                        for i in data:
                                            if i["Plat nomor"] == up_plat:
                                                i["Tanggal"] = tanggal_mobil
                                                print("\nData berhasil diubah\n")
                                                update=1
                                                break
                                    elif yakin.capitalize() == "Tidak":
                                        print("Penggantian data dibatalkan")
                                        update=1
                                        break

                            elif menu_ubah == 5:
                                update=1
                                break

                            else:
                                print("Value tidak valid, coba lagi")
        elif menu_update== 2:
            break
        else:
            print("Value tidak valid, coba lagi")

                                

def Penyewaan() :
    cart = []
    menu_sewa = 0
    while menu_sewa != 4:
        print("""\n\t\t\t\t
              
        \t\t\t    List Menu Sewa :
              
        \t\t\t    1. Pesan sewa kendaraan
        \t\t\t    2. Daftar keranjang
        \t\t\t    3. Pembayaran
        \t\t\t    4. keluar
        """) 
        menu_sewa = input_angka("Masukkan angka Menu sewa yang ingin dijalankan : ","Menu")
        if menu_sewa == 1:
            while True :     
                sewa = {"Nama mobil":"Elgrand", "Plat nomor" : "D 44 YBA", "Price": "72500", "Jangka waktu sewa": "hehe", "Tanggal": "hehe", "Tanggal berakhir sewa": "hehe"}
                from tabulate import tabulate  
                print(tabulate(data, headers="keys", tablefmt= 'grid'))

                sewa_plat = cari_plat("Masukkan plat nomor : ", data)
                if sewa_plat == False:
                    break
                sewa_waktu = input_angka("Jangka waktu sewa : ", "Angka")
                if sewa_waktu == False:
                    break
                else:
                    sewa_tanggal = cari_tanggal_sewa("Masukkan tanggal (M/D/Y) mulai sewa : ",sewa_plat,data)
                    if sewa_tanggal==False:
                        break
                    for i in data :
                        if i["Plat nomor"] == sewa_plat :
                            sewa["Nama mobil"] = i["Nama mobil"]
                            sewa["Plat nomor"] = i["Plat nomor"]
                            sewa["Price"] = i["Price"]*sewa_waktu
                            sewa["Tanggal"] = sewa_tanggal
                            sewa["Jangka waktu sewa"] = sewa_waktu   
                            sewa["Tanggal berakhir sewa"] = Tanggal(list(map(int, sewa_tanggal.split('/')))[1] + sewa_waktu,list(map(int, sewa_tanggal.split('/')))[0],list(map(int, sewa_tanggal.split('/')))[2])
                            
                    yakin = input_yakin("Apakah ingin lanjut untuk menyewa? (Ya/Tidak)\n")
                    if yakin.capitalize() == "Ya":
                        cart.append(sewa)
                        for i in data :
                            if i["Plat nomor"] == sewa_plat :
                                i["Tanggal"] = sewa["Tanggal berakhir sewa"]
                        print("\nKendaraan telah dimasukkan kedalam keranjang\n")    
                        break     
                    elif yakin.capitalize() == "Tidak":
                        print("\nSewa kendaraan dibatalkan\n")
                        break

        elif menu_sewa == 2:
            if cart != []:
                from tabulate import tabulate 
                print(tabulate(cart, headers="keys"))
            else :
                print("Keranjang sewa kosong")
                print()

        elif menu_sewa == 3:
            if cart != []:
                while True:
                    beli = 0
                    if beli == 1:
                        break
                    yakin = input_yakin("Apakah ingin melanjutkan pembayaran? (Ya/Tidak)\n")
                    if yakin.capitalize() == "Ya":
                        total= 0
                        for i in cart:
                            total = total + i["Price"]
                        
                        print(f"Total yang harus dibayar = {total}")
                        while True :
                            uang = input_angka("Masukkan Jumlah uang : ",'Angkaharus')
                            Kurang = total - uang
                            Kembali = uang - total

                            if uang < total:
                                print(f"Uang anda kurang sebesar : {Kurang}")
                                break
                            elif uang > total:
                                print(f"\nTerima kasih \nUang kembali anda : {Kembali}")
                                cart = []
                                beli = 1
                                break
                            else : 
                                print("\nTerima kasih uang anda pas")
                                cart = []
                                beli = 1
                                break  
                    elif yakin.capitalize() == "Tidak":
                        break
            else:
                print("Keranjang sewa kosong")
                print()
        elif menu_sewa == 4:
            break
        else:
            print("Value tidak valid, coba lagi")

def MenuUtama():
    program = 0
    while program !=6 :
        Mainmenu()
        program = input_angka("Masukkan angka Menu yang ingin dijalankan : ","Menu")

        if program == 1:
            daftar()

        elif program == 2 :
            nambah()
            
        elif program == 3 :
            Hapus()

        elif program == 4 :
            Update()

        elif program == 5 :
            Penyewaan()

        elif program == 6 :
            break
        else:
            print("Value tidak valid, coba lagi")


# Jalankan menu utama
MenuUtama()











