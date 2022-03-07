#import modul hashlib

import hashlib
import os
import sys

def kyuraz():
    print """
    _______________________________________
    _                                     _
    _          HASH ENCRYPTOR             _
    _       c0d3d by ./Serizawa           _
    _        thanks to Ago Oeng           _
    _______________________________________

    """

def banner():
    print "[1] MD5 "
    print "[2] MD4 "
    print "[3] SHA512 " 


def md5():
    masuk = raw_input("masukin md5 => ")
    md = hashlib.new('md5')
    md.update(masuk)
    print "md5 => ", md.hexdigest()
    dudung()



def md4():
    reks1 = raw_input("masukin md4 => ")
    md4 = hashlib.new('md4')
    md4.update(reks1)
    print "md4 => ", md4.hexdigest()
    dudung()



def sha():
    reks2 = raw_input("masukin sha512 => ")
    sha = hashlib.new('sha512')
    sha.update(reks2)
    print "sha512 => ", sha.hexdigest()
    dudung()





def dudung():
    kyuraz()
    banner()
    r = input ("choose ur number => ")
    if r == 1:
        md5()
    elif r == 2:
        md4()
    elif r == 3:
        sha()



if __name__ == "__main__":
    dudung()
