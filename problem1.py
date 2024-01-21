class Mylist(list):
    def save(self,value):
        i=len(self)
        for index in range(i-1,-1,-1):
            if self[index]!=value:
                self.remove(self[index])
                

lst=Mylist([1,2,3,4,5,6,2,3,42,2,2,2,2,3])
lst.save(2)
print(lst)