class HashBucket:
    def __init__(self, M, B):
        self.M = M              # table size
        self.T = [None] * M   # "empty table"
        self.Overflow = []     #overflow array
        self.Buckets = B #nro of buckets

    
    def insert(self, x):
        ascii_ = []
        sum_= 0
        for character in x:
            ascii_.append(ord(character))
        sum_ = sum(ascii_)
        self.asc = sum_
        
        i =   self.asc % self.Buckets    # new index

        if self.T[i] == None:
            self.T[i] = x
            return
        elif self.T[i] == x:
            return
        elif self.T[i] != None:
             if i%2 != 0:
                if self.T[i-1] == None:
                    self.T[i-1] = x
                    return
             else:
                 self.Overflow.append(x)
                
            
    def delete(self, x):
        for i in range(self.M-1):
            if self.T[i] == x:
                self.T[i] = None
        for i in range(len(self.Overflow)):
            if self.Overflow[i] == x:
                self.Overflow[i] = None

    def print(self):
        for x in self.T:
            if x != None:
                print(x,end=" ")

        for x in self.Overflow:
            if x != None:
                print(x,end=" ")
        print()

if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # BM40A1500 Bar1 10aaaa1
