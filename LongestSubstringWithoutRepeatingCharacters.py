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

# 1.檢查dict是否存在當前字符，如果存在更新pointer位置
# 2.計算max
# 3.更新dict
# https://www.youtube.com/watch?v=ZlCxw1VUYj0&t=316s&ab_channel=XiangyuCai
def lengthOfLongestSubstring(s):
    point = 0
    dic={}
    max = 0
    for i in range(len(s)):
        if (s[i] in dic):
            dic[s[i]] = i
            point = dic[s[i]]-1
        else:
            dic[s[i]] = i
            if ((i - point + 1)>max):
                max = i - point + 1
    return max

s = "abcabcbb"
print(lengthOfLongestSubstring(s))

