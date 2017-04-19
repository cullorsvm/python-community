import numpy as np

#create a array of zero size 10 
Z = np.zeros(10)
print(Z)


#create an array of celcius temperture
cvalues = [25.3, 24.8, 26.9, 23.9]
Cel = np.array(cvalues)
print(Cel)

#turn the values into degrees Fahrenheit. 
print(Cel * 9 / 5 + 32)





#arange
a = np.arange(1, 10)
print(a)

# some more arange examples:
x = np.arange(10.4)
print(x)
x = np.arange(0.5, 10.4, 0.8)
print(x)
x = np.arange(0.5, 10.4, 0.8, int)
print(x)


#linspace example
# 50 values between 1 and 10:
print(np.linspace(1, 10))
# 7 values between 1 and 10:
print(np.linspace(1, 10, 7))
# excluding the endpoint:
print(np.linspace(1, 10, 7, endpoint=False))


#broadcasting
a = np.array([[ 0.0, 0.0, 0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])

b = np.array([1.0,2.0,3.0])

print ('First array:')
print (a)
print ('\n')

print ('Second array: ')
print (b)
print ('\n')

print ('First Array + Second Array')
print (a+b)
