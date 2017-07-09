#reverse the strand of dna and find the complement of each ex- GATC - GCTA
#author- kavinaya july 2, 2017

import sys
x = "cats"
y = x[::-1]
#cool - looc
# Now print each character of x one line at a time
end = len(y)
#print(len(x))
#print(y)
# Run a For loop where i runs from 0 -> (end - 1)
    # Print Each character at i by usin x[i]

#if "A" in x:
    #x.replace("A", "T", end)
for i in range(0, end):
    print(i)
    print (y[i])
    y[i] = 'b'

print (y)

#for i in range(0, end):
#    if 'A' == x[0, end]:
#      new_string = y.replace("A", "T", end)
    #if ""
#    print(new_string[i])

#for i in range(0, end):
#    readingthelines = y.readlines()
#    if "A" in readingthelines:
#        new_string = y.replace("A" , "T" , end)






#python3 complementingastrandofdna.py





#from apcs import Window

#string = "cats"

#print (string[0 : ]);

#for i in string[]:
    #print(string[i])
