'''
x_{n+1} = (a x_n + c) mod m

x_{n+1} - x_n = (a x_n + c) - (a x_{n-1} + c)) mod m
              = a (x_n - x_{n-1}) mod m

x_{n+1} = a (x_n - x_{n-1}) mod m + x_n  

x_3 - x_2 = a (x_2 - x_1) mod m 

x_4 = (a (x_3 - x_2) + x_3) mod m
'''

m = 121409833232633162281
x_1 = 65001687610455615650
x_2 = 880901038222735
x_3 = 16032398895653777

diff_2 = x_3 - x_2 #+ 
diff_1 = x_2 - x_1 #-

flag = 0
for a in range(-100000000, 100000000):
  if (a * diff_1) % m == diff_2:
    flag = (a * diff_2 + x_3) % m

print("flag: ", flag) 
  
    
    
    
