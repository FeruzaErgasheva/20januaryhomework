from random import randint
class Mylist(list):
    def random(self,n, min=randint(-100,100), max=randint(-100,100)):
        for i in range(n):
            self.append(randint(min,max))
lst=Mylist()
lst.random(7,-10,13)
print(lst)