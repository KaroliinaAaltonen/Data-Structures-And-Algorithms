def pairs(s):
    arr=[]
    res=0
    k=0
    iterations=0

    for i in s:
        arr.append(int(i))
        if i == '1':
            k+=1
    for i in range(k):
        iterations+=k
    n = len(arr)
        
    for i in range(n,0,-1):
        for j in range(n-1):
            if arr[i-1] == 1 and arr[j]==1 and j != (i-1) and iterations>0:
                  iterations-=1
                  if (i-1)>j:
                      res= res+((i-1)-j)
                  
    return res
    
if __name__ == "__main__":
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    print(pairs("100100111001")) # 71
