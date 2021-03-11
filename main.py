#Your task is to help me edit the function myFunc below.
#myFunc is meant to take in an integer 'size', and return a string of alternating 1's and 0s that is the same length as the size parameter. It doesn't work because I have poopoo brain, help me fix it

def myFunc(size):
  myString = "1010"
  for i in range(10):
    myString += str(i%3)
  return myString

print(myFunc(3))

#Your second task is to help me figure out how much money different carpets cost.
#The dictionary myDict stores the cost of each different material. 
#myFunc is supposed to calculate the area of the carpet using parametes, and then return how much it would cost to use each different material

#Price is for 5m^2 of each material
myDict = {"Silk":50, "Shag":12, "Gold":150, "Human":25}

def myFunc2(l, w):
  msqrd = l*w
  for key,value in myDict.items():
    price = msqrd/5*value
    print("\nA {} carpet of area {}m^2 would cost ${}".format(key,msqrd,price))


print (myFunc2(5,5))






