import serial
import time

ser = serial.Serial('COM2', 115200, timeout = 100) # ttyACM1 for Arduino board

readOut = 0   #chars waiting from laser range finder

print ("Starting up")
connected = False


raw = b'\x24\x4F\x56\x50\xCE\xFC\x01\x00\x76\x7B\x14\x5A\x10\x58\x42\x7A\xE1\x8C\x6B\x0D\xC2\x01\x37\x51\x21\x14\x23\x00\x46\xC0\x06\x69\x9E\x19\xEE\x56\x1E\x75\xD6\x00\xA9\x01\x00\x02\x1E\x8E\x8D\x09\x0D'
raw2 = b'\x24\x4F\x56\x50\xCE\xFC\x01\x00\x76\x7B\x14\x5A\x10\x58\x42\x7A\xE1\x8C\x6B\x0D\xC2\x01\x37\x21\x14\x23\x00\x46\xC0\x06\x69\x9E\x19\xEE\x56\x1E\x75\xD6\x00\xA9\x01\x00\x02\x1E\x8E\x8D\x09\x0D'
raw3 = b'\x24\x4F\x56\x50\xCE\xFC\x01\x00\x76\x14\x5A\x10\x58\x42\x7A\xE1\x8C\x6B\x0D\xC2\x01\x37\x51\x21\x14\x23\x00\x46\xC0\x06\x69\x9E\x19\xEE\x56\x1E\x75\xD6\x00\xA9\x01\x00\x02\x1E\x8E\x8D\x09\x0D'


while True:
    print("Sending Fake Packet")
    ser.write(raw)
    ser.flush()
    time.sleep(0.1)
    #time.sleep(1)
    ser.write(raw)
    ser.flush()
    time.sleep(0.1)
    ser.write(raw3)
    ser.flush()
    time.sleep(0.1)
