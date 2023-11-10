#Start input Admin name 
admin_name = str(input("Input Nama Admin :"))
while not admin_name:
    print("Nama Admin tidak boleh kosong.")
    admin_name = input("Input Nama Admin: ")
    

#Start fitur
while True :
    #Start Output Pilihan
    print("[]======================[]")
    print("Pilih Fitur Program ini :")
    print("1. Absen Karyawan")
    print("2. Manajemen Supply")
    print("3. keluar")
    print("[]======================[]")
    #End Output Pilihan
    
    #Start Input Pilihan
    select_input = int(input("Input Pilihan (1/2/3) :"))
    #End Input Pilihan
    
    #Start Absen Karyawan
    if select_input == 1 :
        #Tuple Karyawan
        karyawan = ("Dani", "dani", "Maul", "maul", 'Budi', "budi", "Siti", "siti" )
        
        #Pilih Karyawan
        print("[]======================[]")
        print("List karyawan :")
        print("1. Dani \n2. Maul \n3. Budi \n4. Siti")
        selectKar1 = str(input("Pilih Karyawan (Dani/Maul/Budi/Siti) :"))
        
        #Penyocokan data karyawan dari input
        if selectKar1 in karyawan :
            
            #Start Code Waktu
            #Waktu datang Karyawan (input)
            print("[]======================[]")    
            timeArrive = input("Masukkan waktu kedatangan karyawan (format: HH:MM): ")
    
            #Memisahkan jam dan menit dari input pengguna (Waktu Datang)
            try:
                jam_datang, menit_datang = map(int, timeArrive.split(':'))
                #jika User menginput menit yang salah
                if menit_datang >= 60 :
                    print("Format Waktu Salah!")
                    print("Program Mengulang...")
                    continue
                #jika karyawan datang setelah restoran tutup
                elif jam_datang >= 17 :
                    print("Restoran Tutup")
                    print("Program Mengulang...")
                    continue
                elif jam_datang > 24 :
                    print("Format Waktu Salah!")
                    print("Program Mengulang...")
                    continue
            except ValueError:
                print("[]======================[]")
                print("Format waktu salah. Gunakan format HH:MM.")
                print("Program Mengulang...")
                continue
                
            #Waktu Pulang input
            print("[]======================[]")
            timeLeave = input("Masukkan waktu pulang karyawan (format: HH:MM): ")  
             
            #Memisahkan jam dan menit dari input pengguna (Waktu Pulang)
            try:
                jam_pulang, menit_pulang = map(int, timeLeave.split(':'))
                #jika User menginput menit yang salah
                if menit_datang >= 60 :
                    print("Format Waktu Salah!")
                    print("Program Mengulang...")
                    continue
                elif jam_pulang > 24 :
                    print("Format Waktu Salah!")
                    print("Program Mengulang...")
                    continue
            except ValueError:
                print("[]======================[]")
                print("Format waktu salah. Gunakan format HH:MM.")
                print("Program Mengulang...")
                continue
            
            #Waktu Telat    
            jam_telat = 7
            menit_telat = 0
            #Total menit Jam kerjanya
            total_menit_kerja = (jam_pulang - jam_datang)*60 + (menit_pulang - menit_datang)
            
            #End Code Waktu
            #Start Penghitungan Gaji
            #gaji Perjam
            tarif_per_jam = 15000
            potongan_gaji = 0
            gaji_akhir = 0
            gaji_awal = 0
        
            #karyawan pulang sebelum kerja dimulai
            if total_menit_kerja <= 0 and jam_pulang < jam_telat :
                print("Karyawan pulang lebih awal.")
            

            #karyawan datang lebih dahulu
            elif total_menit_kerja > 0 and jam_telat > jam_datang :
                
                #datang dulu, pulang dulu
                if  total_menit_kerja >= 600 and 7 > jam_datang and jam_pulang < 17 :
                    selisihwaktu = ((7 - jam_datang)*60) - menit_datang
                    menitFinal = total_menit_kerja - selisihwaktu
                    gaji = (menitFinal / 60) * tarif_per_jam 
                    gaji_awal = gaji
                    gaji_akhir = gaji
                    print("1")
                
                #datang dulu, pulang dulu
                elif total_menit_kerja <= 600 and 7 > jam_datang and jam_pulang < 17 :
                    selisihwaktu = ((7 - jam_datang)*60) - menit_datang
                    menitFinal = total_menit_kerja - selisihwaktu
                    gaji = (menitFinal / 60) * tarif_per_jam 
                    gaji_awal = gaji
                    gaji_akhir = gaji
                    print("2")
                
                elif total_menit_kerja <= 600 and 7 > jam_datang :
                    rumus =  ((17 - jam_telat)*60 + (0 - menit_telat))
                    rumus2 = rumus / 60
                    gaji = rumus2 * tarif_per_jam
                    gaji_awal = gaji
                    gaji_akhir = gaji
                    print("3")
                 
                elif jam_datang < jam_telat and jam_pulang > 17 :
                    gaji = 150000
                    gaji_awal = gaji
                    gaji_akhir = gaji
                    print("4")
                    
            elif jam_datang == 7 and jam_pulang == 17 and menit_datang < 5 :
                gaji = 150000
                gaji_awal = gaji
                gaji_akhir = gaji
                print("5")
                
            elif jam_datang == 7 and jam_pulang == 17 and menit_datang > 5 :
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                keterlambatan_menit = (jam_datang - 7)* 60 + menit_datang
                potongan_gaji = (keterlambatan_menit / 5) * 1200
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                gaji1 = rumus3
                gaji = rumus3 - potongan_gaji
                gaji_awal = gaji1
                gaji_akhir = gaji
                print("6") 
            
            elif total_menit_kerja >= 600 and 7 <= jam_datang and jam_pulang > 17 and menit_datang > 5 :
                selisihwaktu = ((jam_pulang - 17)*60) - menit_pulang
                menitFinal = total_menit_kerja - selisihwaktu
                upah = (menitFinal / 60) * tarif_per_jam 
                gaji_awal = upah
                keterlambatan_menit = (jam_datang - 7)* 60 + menit_datang
                potongan_gaji = (keterlambatan_menit / 5) * 1200
                gaji = upah - potongan_gaji
                gaji_akhir = gaji
                print("tambahan1") 
                    
            elif jam_datang == 7 and jam_pulang > 17 :
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                gaji = rumus3
                gaji_awal = gaji
                gaji_akhir = gaji
                print("7")
                
            elif jam_datang == 7 and jam_pulang < 17 and menit_datang < 5:
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                gaji = rumus3
                gaji_awal = gaji
                gaji_akhir = gaji
                print("8")
                    
            elif jam_datang > 7 and jam_pulang < 17  :
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                keterlambatan_menit = (jam_datang - 7)* 60 + menit_datang
                potongan_gaji = (keterlambatan_menit / 5) * 1200
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                gaji1 = rumus3
                gaji = rumus3 - potongan_gaji
                gaji_awal = gaji1
                gaji_akhir = gaji
                print("9")
                
            elif total_menit_kerja >= 600 and 7 < jam_datang and jam_pulang > 17 :
                selisihwaktu = ((jam_pulang - 17)*60) - menit_pulang
                menitFinal = total_menit_kerja - selisihwaktu
                upah = (menitFinal / 60) * tarif_per_jam 
                gaji_awal = upah
                keterlambatan_menit = (jam_datang - 7)* 60 + menit_datang
                potongan_gaji = (keterlambatan_menit / 5) * 1200
                gaji = upah - potongan_gaji
                gaji_akhir = gaji
                print("tambahan")
                
            elif jam_datang > 7 and jam_pulang >= 17  :
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                keterlambatan_menit = (jam_datang - 7)* 60 + menit_datang
                potongan_gaji = (keterlambatan_menit / 5) * 1200
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                gaji = rumus3 - potongan_gaji
                gaji1 = rumus3
                gaji_awal = gaji1
                gaji_akhir = gaji
                print("10")
                
            elif jam_datang == 7 and jam_pulang < 17 and menit_datang > 0 :
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                keterlambatan_menit = (jam_datang - 7)* 60 + menit_datang
                potongan_gaji = (keterlambatan_menit / 5) * 1200
                rumus3 = (total_menit_kerja / 60) * tarif_per_jam
                gaji1 = rumus3
                gaji = rumus3 - potongan_gaji
                gaji_awal = gaji1
                gaji_akhir = gaji
                print("11")
                
            
            
            """
            #karyawan telat    
            elif jam_datang > jam_telat :
            #menghitung keterlambatan dalam menit
                keterlambatan_menit = (jam_datang - jam_telat)* 60 + menit_datang
                gaji_awal = 150000
                
                #Menghitung potongam gaji karena keterlambatan(denda)
                potongan_gaji = (keterlambatan_menit / 5) * 1200
                gaji = gaji_awal - potongan_gaji
                gaji_akhir = gaji
                print("8")
                
                if jam_datang >= 16 and menit_datang >= 45 :
                    print("karyawan tidak layak digaji") 
                    continue
                """
                
            
            #End Penghitungan Gaji
            
            #Start Outputing Rincian
            print("[]===[Rincian]===[]")
            print("Admin Bertugas :", admin_name)
            print("Nama karyawan :", selectKar1)
            print("Pukul waktu datang :", timeArrive)
            print("Pukul waktu pulang :", timeLeave)
            print("Gaji awal : Rp.", gaji_awal)
            print("Denda : Rp.", potongan_gaji)
            print('Total gaji : Rp.', gaji_akhir)
            print("[]===[Rincian Selesai]===[]")
            print("1. Menu Awal")
            print("2. Keluar")
            pilihan_menu_done_absen = int(input("pilih (1/2) :"))
            print("[]======================[]")
            if pilihan_menu_done_absen == 1 :
                print("Program kembali ke menu awal")
                continue
            elif pilihan_menu_done_absen == 2 :
                print("Program keluar...")
                print("Terima Kasih Telah Menggunakan Program Ini!")
                break
            else :
                print("Input tidak benar \nProgram keluar...")
                print("Terima Kasih Telah Menggunakan Program Ini!")
                break
            #End Outputing Rincian
            
        elif selectKar1 not in karyawan :
            print("[]======================[]")
            print("Bukan Karyawan!")
            print("Program Mengulang...")
            continue
    #End Absen Karyawan
        
    #Start Manajemen Supply
    elif select_input == 2 :
        #Tuple bahan
        bahan = ("Beras", "beras", "Daging", "daging", "Tepung", "tepung" )
        
        #Pilihan bahan
        print("[]======================[]")
        print("1. Beras \n2. Daging \n3. Tepung")
        
        #input pilih bahan
        print("[]======================[]")
        nama_bahan = str(input("Pilih nama bahan (Beras/Daging/Tepung) :"))
        
        if nama_bahan in bahan :
            #input stok lama dan baru
            try :
                print("[]======================[]")
                bahan_baru = float(input("Masukan Stok bahan baru (kg) :"))
                bahan_lama = float(input("Masukan Stok bahan lama (kg) :"))
            except ValueError :
                print("[]======================[]")
                print("Input tidak valid. Masukkan hanya bilangan bulat atau desimal.")
                print("Program Mengulang...")
                continue
          
            #proses apakah kurang
            gabung = (bahan_baru + bahan_lama) 
        
            #kondisi barang kurang
            if gabung < 10 :
                print("[]======================[]")
                print("Stok tidak memenuhi syarat minimum (10kg)!")
                kurang = 10 - gabung
                print("Stok bahan lama :", bahan_lama, "Kg")
                print("Stok bahan baru :", bahan_baru, "Kg")
                print("Jumlah stok bahan lama dan baru :", gabung, "Kg")
                print("Bahan kurang :", kurang)
                #input harga brang kurang
                print("[]======================[]")
                try :
                    harga_barang = int(input("Masukan harga barang perkilonya dipasaran (Rupiah) :"))
                except ValueError :
                    print("[]======================[]")
                    print("Input tidak valid. Masukkan hanya bilangan bulat.")
                    print("Program Mengulang...")
                    continue
                #harga bahan x stok kurang
                harga_stokKurang = kurang * harga_barang
                #harga bahan x barang baru
                harga_stokBaru = bahan_baru * harga_barang
                #Jumlah harga bahan stok baru + kurangnya
                baru_kurang = harga_stokKurang + harga_stokBaru
                
                #Start Outputing kondisi bahan kurang
                print("[]===[Rincian]===[]")
                print("Admin Bertugas :", admin_name)
                print("Nama bahan :", nama_bahan)
                print("Stok bahan lama :", bahan_lama, "Kg")
                print("Stok bahan baru :", bahan_baru, "Kg")
                print("Bahan kurang :", kurang, "Kg")
                print("harga bahan perkilo : Rp.", harga_barang)
                print("Harga bahan baru : Rp.", harga_stokBaru)
                print("Harga bahan yang masih kurang : Rp.", harga_stokKurang)
                print("Total jumlah harga stok bahan baru dan stok kurang : Rp.", baru_kurang)
                print("[]===[Rincian Selesai]===[]")
                print("1. Menu Awal")
                print("2. Keluar")
                print("[]======================[]")
                pilihan_menu_done_absen = int(input("pilih (1/2) :"))
                if pilihan_menu_done_absen == 1 :
                    print("Program kembali ke menu awal")
                    continue
                elif pilihan_menu_done_absen == 2 :
                    print("Program keluar...")
                    print("Terima Kasih Telah Menggunakan Program Ini!")
                    break
                else :
                    print("Input tidak benar \nProgram keluar...")
                    print("Terima Kasih Telah Menggunakan Program Ini!")
                    break
                #End Outputing kondisi bahan kurang
            
            #Kondisi bahan sudah cukup
            elif gabung >= 10 :
                #karena barang tidak kurang
                kurang = 0
                harga_stokKurang = 0
                print("[]======================[]")
                print("Stok memenuhi syarat minimum (10kg)!")
                print("Stok bahan lama :", bahan_lama, "Kg")
                print("Stok bahan baru :", bahan_baru, "Kg")
                print("Jumlah stok bahan lama dan baru :", gabung, "Kg")
                #input harga stok baru
                print("[]======================[]")
                try :
                    harga_barang = float(input("Masukan harga barang perkilonya dipasaran (Rupiah) :"))
                except ValueError :
                    print("[]======================[]")
                    print("Input tidak valid. Masukkan hanya bilangan bulat atau desimal.")
                    print("Program Mengulang...")
                    continue
                #barang baru x harganya
                harga_stokBaru = bahan_baru * harga_barang
                harga_stokKurang = 0
                #Jumlah harga bahan stok baru + kurangnya
                baru_kurang = harga_stokKurang + harga_stokBaru
                
                #Start Outputing kondisi bahan pas
                print("[]===[Rincian]===[]")
                print("Admin Bertugas :", admin_name)
                print("Nama bahan :", nama_bahan)
                print("Stok bahan lama :", bahan_lama, "Kg")
                print("Stok bahan baru :", bahan_baru, "Kg")
                print("Bahan kurang :", kurang, "Kg")
                print("harga bahan perkilo : Rp.", harga_barang)
                print("Harga bahan baru : Rp.", harga_stokBaru)
                print("Harga bahan yang masih kurang : Rp.", harga_stokKurang)
                print("Total jumlah harga stok bahan baru dan stok kurang : Rp.", baru_kurang)
                print("[]===[Rincian Selesai]===[]")
                print("1. Menu Awal")
                print("2. Keluar")
                print("[]======================[]")
                pilihan_menu_done_absen = int(input("pilih (1/2) :"))
                if pilihan_menu_done_absen == 1 :
                    print("Program kembali ke menu awal")
                    continue
                elif pilihan_menu_done_absen == 2 :
                
                    print("Program keluar...")
                    print("Terima Kasih Telah Menggunakan Program Ini!")
                    break
                else :
                    
                    print("Input tidak benar \nProgram keluar...")
                    print("Terima Kasih Telah Menggunakan Program Ini!")
                    break
                #End Outputing kondisi bahan pas
        elif nama_bahan not in bahan :
            print("[]======================[]")
            print("Bukan Termasuk Bahan di List!")
            print("Program Mengulang...")
            continue   
    #End Manajemen Supply
    
    #Keluar
    elif select_input == 3 :
        print("[]======================[]")
        print("Terima Kasih Telah Menggunakan Program Ini!")
        break
    else :
        print("[]======================[]")
        print("Input tidak benar \nProgram keluar...")
        print("Terima Kasih Telah Menggunakan Program Ini!")
        break
#End Fitur