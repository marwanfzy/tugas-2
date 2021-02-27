def print_menu():
    print ("Selamat Datang!")
    print ("=" * 20)
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 3:
    menu_choice = int(input("Pilih Menu (1-3): "))
    if menu_choice == 1:
        print("Daftar Kontak:")
        for x in numbers.keys():
            print("Nama: ", x, "\nNo Telepon:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Tambahkan Nama dan Nomor")
        name = input("Nama : ")
        phone = input("No Telepon : ")
        numbers[name] = phone
        print ("Kontak berhasil ditambahkan!")
    elif menu_choice == 3:
        print ("Program Selesai, sampai Jumpa!")
    elif menu_choice >= 3:
        print ("Menu Tidak Tersedia")