# first in first out
class stack:
    def __init__(self):
        self.lists = []
    def push(self,num):
        self.lists.append(num)
    def pop(self):
        if self.lists:
            num=self.lists[0]
            self.lists=self.lists[1:]
            return num
    def peek(self):
        if self.lists:
            return self.lists[0]
    def see(self):
        return self.lists
