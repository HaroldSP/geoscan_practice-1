#calculating checksum for entire data
def calc(data):
    checksum = 0
    for b in data:
        checksum = _crc8_dvb_s2(checksum, b)
        
    return checksum


#calculating CRC8_DVB_S2
def _crc8_dvb_s2(crc, a):
    crc ^= a
    for _ in range(8):
        if crc & 0x80:
            crc = ((crc << 1) ^ 0xD5) % 256
        else:
            crc = (crc << 1) % 256
            
    return crc
