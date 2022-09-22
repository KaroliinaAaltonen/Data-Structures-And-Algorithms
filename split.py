import sys

def split(T):
    count=0
    i=0
    n = len(T)
    curr=T[0]
    biggest=0
    smallest =100

    for x in T:
        if isinstance(x, int) == False:
            sys.exit()
        if x<smallest:
            smallest=x

    for j in T:
        i+=1
        if j>biggest:
            biggest=j
            biggest_index = T.index(T[i-1])
                
    for idx in range(0, biggest_index):
        if T[-1]==smallest:
            break
        if T[idx] == biggest and T[idx] != T[-1]:
            break
        if T[idx-1]<T[idx] and T[idx] != T[0] and T[idx-1] != T[idx]:
            count+=1
        if T[-1]== biggest and T[idx-1] == T[-1]:
            count+=1
    
    return count

if __name__ == "__main__":
    print(split([1,2,3,4,5])) # 4
    print(split([5,4,3,2,1])) # 0
    print(split([2,1,2,5,7,6,9])) # 3
    print(split([1,2,3,1])) # 0
    print(split([3, 3, 3, 3, 1, 8, ...]))
