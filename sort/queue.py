#first in last out
class queue:
    def __init__(self):
        self.lists = []
    def enqueue(self,num):
        self.lists.append(num)
    def dequeue(self):
        if self.lists:
            num=self.lists[len(self.lists)-1]
            self.lists=self.lists[:-1]
            return num
    def peek(self):
        if self.lists:
            return self.lists[0]
    def see(self):
        return self.lists  