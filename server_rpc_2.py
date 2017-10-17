#Ahmad Rizal Muttaqin
#135150207111051

import xmlrpclib

from SimpleXMLRPCServer import SimpleXMLRPCServer



def penjumlahan(nilai_a,nilai_b):
    return (nilai_a + nilai_b)

def pengurangan(nilai_a,nilai_b):
    return (nilai_a - nilai_b)

def pembagian(nilai_a,nilai_b):
    return (nilai_a / nilai_b)

def perkalian (nilai_a,nilai_b):
    return (nilai_a * nilai_b)

ini_server = SimpleXMLRPCServer( ('',1112) )
print "server rpc 2 siap"

ini_server.register_function(penjumlahan, "penjumlahan")
ini_server.register_function(pengurangan, "pengurangan")
ini_server.register_function(pembagian, "pembagian")
ini_server.register_function(perkalian, "perkalian")
ini_server.serve_forever()