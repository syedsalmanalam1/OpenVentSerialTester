import serial
import time

ser = serial.Serial('COM1', 115200, timeout=100)  # ttyACM1 for Arduino board

readOut = 0  # chars waiting from laser range finder

print("Starting up")
connected = False
crcCorrectCount = 0
crcInCorrectCount = 0


def rs232_checksum(the_bytes):
    return b'%02X' % (sum(the_bytes) & 0xFF)

xorValue = 109

# headerString = "244F5650"
# headerBytes = bytes.fromhex(headerString)
# for bytesData in headerBytes:
#     print(bytesData)
#     xorValue = xorValue ^ bytesData
#
# print("XOR Value is " + str(xorValue))




while True:
        crcCorrectCount = 0
        crcInCorrectCount = 0
        print(" --------------------------------------------------")
        readOut = ser.read(1470)  # 49 bytes x number of packets
        readData = str(readOut.hex()).upper()
        readData2 = readData.split('244F5650')
        if len(readData2[0]) == 0:
            del readData2[0]
        #print(readData2)        # for debugging
        for rdata in readData2:
            size = len(rdata)
            mod_string = rdata[:size - 4]
            crcChar = rdata[size - 4: size - 2]
            crcInt = int.from_bytes(bytes.fromhex(crcChar), "big")
            #print(crcInt)

            bytesWithoutHeaderAndCRC = bytes.fromhex(mod_string)
            xorValue = 109
            for bytesData in bytesWithoutHeaderAndCRC:
                # print(bytesData)
                xorValue = xorValue ^ bytesData
            # print(xorValue)
            if( xorValue == crcInt):
                crcCorrectCount = crcCorrectCount + 1
            else:
                crcInCorrectCount = crcInCorrectCount + 1

        print( "Number of headers Received = " + str(len(readData2)))
        print("Correct CRC = " + str(crcCorrectCount) + "  InCorrect CRC = " + str(crcInCorrectCount))
        ser.flush()

