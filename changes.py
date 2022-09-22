def changes(A):
    count=0
    for x in range(len(A)-1):
        if A[x] == A[x+1]:
            A[x+1]=9
            count=count+1
            
    return count

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2
