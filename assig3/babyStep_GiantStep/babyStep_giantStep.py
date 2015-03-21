#Baby Step Giant Step DLP problem y = a**x mod n
#Author : Meet P Shah 
#Input: The Prime Number, the generator, the integer whose log is needed.
 
from datetime import datetime
import time 
import math
import matplotlib.pyplot as plt

#Example 70 = 2**x mod 131

def calculate_discrete_log(n_i,a_i,y_i): 
    n = int(n_i)
    a = int(a_i)
    y = int(y_i)
     
    s = math.floor(math.sqrt(n))
     
    A = []
    B = []
     
    for r in range(0,s):
        value = y*(a^r) % n
        A.append(value)
     
    for t in range(1,s+1):
        value = a^(t*s) % n
        B.append(value)
     
    #print(A)
    #print(B)
     
    x1,x2 =0,0
      
    for r in A:
        for t in B:
            if r == t:
                x1 = A.index(r)            
                x2 = B.index(t)
                #print(x1,x2)
                break
                      
    #print(((x2+1)*s - x1) % n )
    return ((x2+1)*s - x1) % n 

prime_list=[251,1021,4051,16007,64891,251903,611839] #[8,10,12,14,16,18,20bits]

prime_bit_list=[8,10,12,14,16,18,20]

input_list=[70,98,86,100,63,86,130]

output_list=[]
time_list=[]

for prime in prime_list:
    for input_no in input_list:
        startTime = time.time()
        temp_out = calculate_discrete_log(prime,2,input_no)
        time_taken= time.time() - startTime
        output_list.append(temp_out)
        time_list.append(float(str(time_taken)[0:6]))

print(output_list)
print(time_list)

#print(calculate_discrete_log(131,2,70))


