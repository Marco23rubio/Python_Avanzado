import time

class Fiboiter():
    def __init__(self,max=int):
        self.max = max
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.count = 0
        self.num = 0
        return self
    
    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.n1
        elif self.count == 1:
            self.count += 1
            return self.n2
        else:
            self.num = self.n1 + self.n2
            if self.num >= self.max:
                raise StopIteration
            self.n1 , self.n2 = self.n2 , self.num 
            return self.num



if __name__ == "__main__":
    fibonacci = Fiboiter(5585)
    for element in fibonacci:
        print(element)
        time.sleep(0.3)