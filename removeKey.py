thisdict = {
  "1": "C language",
  "2": "Java Language",
  "4": "Python Language",
  "3": "C++",
  "4": "Python Language",
  "3": "C++",
  "5": "C++",
}
#declare temp array
tempA = []  
uniqueDict = dict()
for key, val in thisdict.items():
    if val not in tempA:
        tempA.append(val)
        uniqueDict[key] = val

print(uniqueDict)