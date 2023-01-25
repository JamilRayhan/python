myList = ["E","d","g","b","a","F","c"]
#myList.append("bd")
#myList.insert(3,"Jamil")
#myList.remove("f")
#myList.pop(0)
#myList.clear()
myList.sort(key=str.lower,reverse=True)
newList = myList[:]
print(newList)