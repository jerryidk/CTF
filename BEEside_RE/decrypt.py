
# secret.exe
# .data section
# VA: 0x409000 - 0x40a000 
# FO: 0x7a00 - 0x7e00

def get_mem(s: int, l: int) -> bytes:
    fb = 0x7a00
    vb = 0x409000
    offset_s = s - vb
    ret = b''
    with open('secret.exe', 'rb') as binary:
        addr = 0
        while (byte := binary.read(1)):
            if addr + 1 == fb + offset_s:
               ret = binary.read(l) 
               return ret
            addr += 1

# flag 4090e9 
# key 409000
flag = get_mem(0x4090e9, 100)
ooo_key = get_mem(0x409000, 0x20) # 0x1f+1 

decrypt = ''
for i in range(100):
    decrypt += chr(flag[i] ^ ooo_key[i & 0x1f])
 
print(decrypt)