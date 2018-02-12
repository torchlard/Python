import copy
class doublyll:
    def __init__(self):
        self.lists = []
    def insert_head(self,num):
        if self.lists:
            [num]+self.lists
        else:
            self.lists.append(num)
    def insert_tail(self,num):
        self.lists.append(num)
    def insert_k(self,num,k):
        tmp=[]
        if len(self.lists) > k:
            tmp=self.lists[:k-1]
            tmp.append(num)
            tmp.append(self.lists[k-1:])
            self.lists=copy.copy(tmp)
        elif len(self.lists)==k:
            self.lists.append(num)
        else:
            print "error"
    def search(self,num):
        for i in range(len(self.lists)):
            if self.lists[i]==num:
                return i
        return "not found"
    def remove_head(self):
        if self.lists:
            self.lists=self.lists[1:]
    def remove_tail(self):
        if self.lists:
            self.lists=self.lists[:-1]
    def remove_k(self):
        if self.lists[k-1]:
            tmp=[]
            tmp=self.lists[:k-1]
            for i in self.lists[k:]:
                tmp.append(i)
            self.lists.copy(tmp)
    def see(self):
        print self.lists