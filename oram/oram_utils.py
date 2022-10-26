import binascii

def string_to_int(string):
    reg_int = int(binascii.hexlify(string.encode("utf-8")), 16)
    return reg_int

def int_to_string(integer):
    string = binascii.unhexlify(format(integer, "x").encode("utf-8")).decode("utf-8")
    return string

if __name__ == '__main__':
    pass