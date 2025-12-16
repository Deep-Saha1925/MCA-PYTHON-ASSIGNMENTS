dic1={1:10, 2:20,4:6}
dic2={3:30, 4:40,5:2}
dic3={5:50,6:60}
newDict = {}

def insertElem(dic):
    for d in dic.keys():
        if d not in newDict:
            newDict[d] = dic[d]
        else:
            newDict[d] += dic[d]
            
insertElem(dic1)
insertElem(dic2)
insertElem(dic3)

print(newDict)