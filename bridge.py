from abc import ABC, abstractmethod


class Seria(ABC):
    @abstractmethod
    def first(self):
        pass


class fifthSeria(Seria):
    def first(self):
        return "50"
    
class forthSeria(Seria):
    def first(self):
        return "40"
    

class Model(ABC):
    def __init__(self, seria: Seria): #Мостик
        self.seria = seria 

    @abstractmethod
    def second(self):
        pass

class sixmod(Model):
    def second(self):
        print(f'Видюха {self.seria.first()}60')
    
class sevenmod(Model):
    def second(self):
        print(f'Видюха {self.seria.first()}70')
    

def main():
    f = fifthSeria()
    t = forthSeria()
    old = sixmod(t)
    new = sevenmod(f)
    mid1 = sixmod(f)
    mid2 = sevenmod(t)

    new.second()
    old.second()
    mid1.second()
    mid2.second()

if __name__ == "__main__":
    main()