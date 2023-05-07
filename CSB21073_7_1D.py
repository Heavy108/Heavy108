#1D PROBLEM
#Satyam sajal 
#csb21073


def Overlapping(str1, str2):   
    max_len = 0         #IT WILL STORE THE NUMBER OF OVERLAPPING BETWEEN PAIRS
    len1 = len(str1)
    len2 = len(str2)
    str_ = ""  
    for i in range(1, min(len1, len2)+1):     
        if str1[len1-i:] == str2[:i]:
            if max_len < i:                
                max_len = i
                str_ = str1 + str2[i:] 
    for i in range(1, min(len1, len2)+1):       
        if str1[:i] == str2[len2-i:]:           
            if max_len < i:               
                max_len = i
                str_ = str2 + str1[i:]  #IT STORES THE STRING WITH HIGHEST OVERLAPPING
    
    return max_len, str_


def ShortestSuperstring(arr, n):
   
    while n != 1:        
        max_len2 = 0       
        l, r = 0, 0      
        res_str = ""   
        for i in range(n):
            for j in range(i+1, n):
                str_ = ""              
                res, str_ = Overlapping(arr[i], arr[j])
                              
                if max_len2 < res:
                    max_len2 = res
                    res_str = str_
        
                    l, r = i, j  
                    
        # Ignore last element in next cycle               
        n -= 1       
        if max_len2 == 0:
            arr[0] += arr[n]
        else:
            # Copy resultant string to index l
            arr[l] = res_str
            # Copy string at last index to index r
            arr[r] = arr[n]
    
    return arr[0]



arr = ['GOYG','WGO','GOYW','YGGW','GWY','WYOG','OGOY']      #WHERE G =GREEN; O=ORANGE ; W=WHITE ;Y =YELLOW;
    
n = len(arr)
Z=ShortestSuperstring(arr, n)
# Function Call
print(f"The Shortest Superstring is {len(Z)} and the string is {Z}")
