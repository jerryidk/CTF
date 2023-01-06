# Brute Force

def get(addr, size):
  res = ''
  with open('main', 'rb') as f:
    f.read(addr)
    chunk = f.read(size)
    for b in chunk: 
      res += chr(b) 

  return res
    
def idx(flag):
  mapping = [1, 2, 1, 2, 2]
  ret = 0
  for i in range(len(flag)+1):
    l = mapping[i % 5] 
    ret += l
  return ret

def decrypt(flag, tbl): 
  s20 = 0
  s24 = 0
  ret = ''
  for c in flag:
    c = ord(c)
    s20 = s20 | c << (s24 & 0x1f)
    s24 += 8
    while s24  > 4:
      ret += tbl[(s20 & 0x1f)] 
      s20 = s20 >> 5
      s24 -= 5

  return ret

def force(flag, enc, table):
  ret = []
  for c in range(32, 127):
    inp = flag + chr(c)
    d = decrypt(inp, table)
    if d == enc: 
      ret.append(inp)
  return ret


enc_flag = get(0x9fc, 57) # encrypted flag
table = get(0x1000, 33) # encryption string

flag = input("enter initial flag ( CTFlearn{ ):")

while len(flag) <= 32:
  enc = enc_flag[:idx(flag)]  
  ret = force(flag, enc, table)
  if len(ret) == 0:
    print("not found: ")
    break
  elif len(ret) == 1:
    flag = ret[0]
  else: 
    print("found: ", ret)
    i = input("enter index: ")
    flag = ret[int(i)]
 






