s = "abcabcbb"
substrList = []
newList=[]

"""""""""""Solution 1"""""""""""""""

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

"""""""""""Solution 2"""""""""""""""

def lengthOfLongestSubstring2(s):
      point =0
      index = 0
      d={}
      ans = 0
      while index < len(s):
         if s[index] not in d or point>d[s[index]]:
            ans = max(ans,(index-point+1))
            d[s[index]] = index
         else:
            point = d[s[index]]+1
            ans = max(ans,(index-point+1))
            index-=1
         #print(ans)
         index+=1
      return ans
print(lengthOfLongestSubstring("ABCABCBB"))

