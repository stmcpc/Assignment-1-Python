def myFunc(size):
  myString = ""
  for i in range(size):
    myString += str(i%2)
  return myString

myDict = {"Silk":50, "Shag":12, "Gold":150, "Human":25}

def myFunc2(l, w):
  msqrd = l*w
  for key,value in myDict.items():
    price = msqrd/5*value
    print("\nA {} carpet of area {}m^2 would cost ${}".format(key,msqrd,price))


print (myFunc2(5,5))