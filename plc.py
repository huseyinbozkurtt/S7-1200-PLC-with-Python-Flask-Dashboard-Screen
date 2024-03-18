
from time import sleep
import snap7
import snap7.client as c
from snap7.util import *
from snap7.types import *
import locale
locale.setlocale(locale.LC_ALL, '')
myplc = snap7.client.Client()
myplc.connect("192.168.1.99", 0, 1)
myplc.get_connected()
print(myplc.get_cpu_state())

def ReadMemorydb(plc, db, start,bit, tur):
    result = plc.read_area(Areas.DB,db,start,4)
    if tur=="real":
        return get_real(result,0)
    elif tur=="bit":
        return get_bool(result,0,bit)
    

def Writedb(plc, db, start,bit, value,tur):

            reading = plc.read_area(Areas.DB, db, start, 255)
            if tur=="bit":
                set_bool(reading,0,bit,value)
            elif tur=="real":
                 set_real(reading,0,value)
            plc.db_write(db, start, reading)
def deger_cek(byte,bit):
    nem=ReadMemorydb(myplc,25,byte,bit,'real')
    return nem
def deger_yaz(bit,sonuc):
    Writedb(myplc,25,0,bit,sonuc,'bit')

print(deger_cek(0,0))