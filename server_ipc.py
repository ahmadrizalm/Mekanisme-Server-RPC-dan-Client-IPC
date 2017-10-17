#Ahmad Rizal Muttaqin
#135150207111051

import socket, json, xmlrpclib

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpsock.bind(('',5555))
port = 1111
tcpsock.listen(10)

while True :
    print "server sedang berjalan"
    koneksi, nilainya = tcpsock.accept()
    data = koneksi.recv(100)
    dictionary_nilai = json.loads(data)
    #loads merubah format data string menjadi json
    print "pemrosesan yang dipilih : "+ dictionary_nilai["tipe pemrosesan"]
    print "hasil nilai a : "+ dictionary_nilai["nilai a"]
    print "hasil nilai b : "+ dictionary_nilai["nilai b"]

    proxy = "http://127.0.0.1:"+ str(port)

    if port != 1113:
        proxynya = xmlrpclib.ServerProxy(proxy)
        port += 1

    else:
        proxynya = xmlrpclib.ServerProxy(proxy)
        port = 1111


    tipe_pemrosesan = dictionary_nilai['tipe pemrosesan']
    nilai_a = int(dictionary_nilai['nilai a'])
    nilai_b = int(dictionary_nilai['nilai b'])

    if tipe_pemrosesan == "penjumlahan":
        hasil_pemrosesan = proxynya.penjumlahan(nilai_a,nilai_b)
        print "mengirim = "+ str(hasil_pemrosesan)+ " ke client"
    elif tipe_pemrosesan == "pengurangan":
        hasil_pemrosesan = proxynya.pengurangan(nilai_a,nilai_b)
        print "mengirim = "+ str(hasil_pemrosesan)+ " ke client"
    elif tipe_pemrosesan == "pembagian":
        hasil_pemrosesan = proxynya.pembagian(nilai_a,nilai_b)
        print "mengirim = "+ str(hasil_pemrosesan)+ " ke client"
    elif tipe_pemrosesan == "perkalian":
        hasil_pemrosesan = proxynya.perkalian(nilai_a,nilai_b)
        print "mengirim = "+ str(hasil_pemrosesan)+ " ke client"
    else : hasil_pemrosesan = " peringatan..\nAnda memasukkan inputan yang salah !!"

    koneksi.send(str(hasil_pemrosesan))
    print ""
    koneksi.close()
