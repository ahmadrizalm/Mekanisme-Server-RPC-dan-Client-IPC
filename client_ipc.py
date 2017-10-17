#Ahmad Rizal Muttaqin
#135150207111051

import socket, json

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpsock.connect(('127.0.0.1',5555))

in_nilai_tipe = raw_input('masukan tipe pemrosesan :')
in_nilai_a = raw_input('masukan nilai a : ')
in_nilai_b = raw_input('masukan nilai b : ')


dictionary_nilai = {"tipe pemrosesan" : in_nilai_tipe,
                    "nilai a" : in_nilai_a,
                  "nilai b" : in_nilai_b,}

json_nilai = json.dumps(dictionary_nilai)
#dumps merubah json jadi string

print "Client mengirim  "+json_nilai

tcpsock.send(json_nilai)

data = tcpsock.recv(100)

print "Server mengirimkan " + data

tcpsock.close()
