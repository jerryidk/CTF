
'''
Stack 

base: $rbp
base - 0x80 : Encrypted Input
base - 0xa0 : Encrypted Flag 
base - 0xa8 : Arr_1 -> int[2]{0x0, strlen/2}
base - 0xb0 : Arr_2 -> int[2]{strlen, strlen/2}
base - 0xb8 : Arr_3 -> int[2]{0x10, 0x18} <<< XOR first half string and second half string
''' 

flag = 'h_bO}EcDOR+G)uh(jl,vL' # <<< Get from x/s $rbp-0xa0
res = ''
key = 0x0
for i in range(len(flag)):
  if i < len(flag)/2-1:
    key = 0x10 
  else:
    key = 0x18
  res += chr(key ^ ord(flag[i]))

print("final flag: ", res)
