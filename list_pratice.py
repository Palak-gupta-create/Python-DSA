L = [23, 35, 45, 65, 43, 33, 34]
key = int(input("Enter number to be searched :"))
found = False
for item in L:
  if item==key:
    found = True
    break
if(found==True):
  print("ELement is found")
else:
  print("Element is not found")
