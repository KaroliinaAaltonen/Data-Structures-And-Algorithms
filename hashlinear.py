## DISCLAIMER ##
## I am not proud of this ##
## Every single line of code took years off my life-expectancy ##

class HashLinear:
    def __init__(self, M):
        self.M = M              # table size
        self.T = [None] * M   # "empty table"

    
    def insert(self, x):
        ascii_ = []
        sum_= 0
        for character in x:
            ascii_.append(ord(character))
        sum_ = sum(ascii_)
        self.asc = sum_
        
        i =   self.asc % self.M        # new index
        
        while True:
            if self.T[i] == None:
                self.T[i] = x
                return
            elif self.T[i] == x:
                return
            elif self.T[i] != None:
                probe = i
                for j in range(self.M):
                    if probe<self.M and self.T[probe] == None:
                        self.T[probe] = x
                        return
                    probe+=1
                    if probe >= self.M:
                        probe=0
            
            
    
    def delete(self, x):
        for i in range(self.M-1):
            if self.T[i] == x:
                self.T[i] = None

    def print(self):
        for i in range(self.M):
            if self.T[i] != None:
                print(self.T[i],end=" ")
        print()

if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1
