s = "abcabcbb"
substrList = []
newList=[]
def findAllSubString(str):
    res = [str[i: j] for i in range(len(str)) 
          for j in range(i + 1, len(str) + 1)]
    return res

def instincStr(str):
    if (len(list(str))==len(set(str))):
        return 1            #無有重複字元
    else:
        return 0   
            

def findMax(list):
    maxLen = 0
    for i in list:
        if len(i)>maxLen:
            maxLen = len(i)
    return maxLen 
  
substrList = findAllSubString(s)
for i in substrList:
    if (instincStr(i)==1):
        newList.append(i)
    else:
        pass
print(findMax(newList))

